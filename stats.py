import json
import requests
import re

from src.mbstats.topics import Topics
from src.mbstats.threads import Threads
from src.mbstats.messages import Messages

from src.mbstats.calc_topic_stats import CalcTopicStats
from src.mbstats.calc_thread_stats import CalcThreadStats
from src.mbstats.calc_message_stats import CalcMessageStats


URL_GET_ALL_TOPICS = "http://localhost:8080/api/topics/?format=json"
URL_GET_ALL_THREADS = "http://localhost:8080/api/threads/?format=json"
URL_GET_ALL_MESSAGES = "http://localhost:8080/api/messages/?format=json"

FILE_NAME_MESSAGE_BOARD_JSON = "message_board.json"

LBL_TOTAL_NBR_MESSAGES: str = "Total number of messages"
LBL_MOST_COMMON_WORD: str = "Most common word"
LBL_AVG_NBR_WORDS: str = "Avg. number of words per sentence"
LBL_AVG_NBR_MESSAGES: str = "Avg. number of messages per thread, per topic"
LBL_MESSAGE_BOARD_WRITTEN: str = "Message Board written to '" + FILE_NAME_MESSAGE_BOARD_JSON + "'"

LBL_OCCURRENCES = "occurrences"

ERR_MSG_GENERIC: str = "[ERROR]"
ERR_MSG_NOT_IMPLEMENTED: str = "[NOT IMPLEMENTED]"
ERR_MSG_OUT_OF_MEMORY: str = "[OUT OF MEMORY]"


def check_valid_chars(messages: dict):
    """
    Find out what special characters are being used in content
    Will use this info to optimize algorithms
     - Results:
        : space - ' '
        : period - '.'
    """
    char_map: dict[str,int] = {}

    regex = re.compile("[a-zA-Z]")

    for message in messages:
        content: str = message["content"]
        special_chars = regex.sub('', content)

        for char in list(special_chars):
            if char in char_map:
                char_cnt: int = char_map[char]
                char_map[char]: int = char_cnt + 1
            else:
                char_map[char]: int = 1

    print(char_map)


class MessageBoardAPIWrapper:
    """
    Wrapper around the messageboard API

    http://localhost:8080/api/
    """

    _topics: dict
    _threads: dict
    _messages: dict

    def __init__(self):
        pass

    @staticmethod
    def _create_thread_topic_dict() -> dict:
        """
        Create a lookup dictionary to find Topic ID for a Thread ID
        """
        thread_topic_dict: dict = {}

        for thread in MessageBoardAPIWrapper._threads:
            thread_id = thread["id"]
            topic_id = thread["topic"]

            thread_topic_dict[thread_id] = topic_id

        return thread_topic_dict

    def _as_dict(self) -> dict:
        """
        Returns the entire messageboard as a nested dictionary.
        """
        message_board: dict = {"topics": {}}

        # Create a lookup dictionary to find Topic ID from Thread ID
        thread_topic_dict: dict = MessageBoardAPIWrapper._create_thread_topic_dict()

        for topic in MessageBoardAPIWrapper._topics:
            topic_id = topic["id"]
            topic["threads"] = {}

            message_board["topics"][topic_id] = topic

        for thread in MessageBoardAPIWrapper._threads:
            thread_id = thread["id"]
            topic_id = thread["topic"]
            thread["messages"] = {}

            message_board["topics"][topic_id]["threads"][thread_id] = thread

        for message in MessageBoardAPIWrapper._messages:
            message_id = message["id"]
            thread_id = message["thread"]

            # Lookup Topic ID from Thread ID
            topic_id = thread_topic_dict[thread_id]

            message_board["topics"][topic_id]["threads"][thread_id]["messages"][message_id] = message

        return message_board

    def to_json(self) -> None:
        """
        Dumps the entire messageboard to a JSON file.
        """
        with open(FILE_NAME_MESSAGE_BOARD_JSON, "w") as f:
            f.write(json.dumps(self._as_dict(), indent=4))


def main():
    """
    Returns information about the message_board application
    """
    message_board = MessageBoardAPIWrapper()

    debug_flg: bool = False

    # ---------------------------------------------------------------------------
    # Initialize Topics Singleton class and load all topics
    # ---------------------------------------------------------------------------
    try:
        Topics.set_url(URL_GET_ALL_TOPICS)
        MessageBoardAPIWrapper._topics = Topics.get_all_topics()

        if debug_flg:
            print("Successfully retrieved all topics")
    except Exception as ex:
        print(
            "[MessageBoardAPIWrapper.main] "
            "Error while retrieving topics -- \n"
            f"{ex}\n"
        )

    # ---------------------------------------------------------------------------
    # Initialize Threads Singleton class and load all threads
    # ---------------------------------------------------------------------------
    try:
        Threads.set_url(URL_GET_ALL_THREADS)
        MessageBoardAPIWrapper._threads = Threads.get_all_threads()

        if debug_flg:
            print("Successfully retrieved all threads")
    except Exception as ex:
        print(
            "[MessageBoardAPIWrapper.main] "
            "Error while retrieving threads -- \n"
            f"{ex}\n"
        )

    # ---------------------------------------------------------------------------
    # Initialize Messages Singleton class and load all messages
    # ---------------------------------------------------------------------------
    try:
        Messages.set_url(URL_GET_ALL_MESSAGES)
        MessageBoardAPIWrapper._messages = Messages.get_all_messages()

        if debug_flg:
            print("Successfully retrieved all messages")
    except Exception as ex:
        print(
            "[MessageBoardAPIWrapper.main] "
            "Error while retrieving messages -- \n"
            f"{ex}\n"
        )

    # ---------------------------------------------------------------------------
    # Test code for finding all characters being used in the data set
    # ---------------------------------------------------------------------------
    # check_valid_chars(Messages.get_all_messages())
    # return

    # ---------------------------------------------------------------------------
    # Calculate all the statistics
    # ---------------------------------------------------------------------------
    try:
        CalcMessageStats.parse_messages(MessageBoardAPIWrapper._messages)
        CalcThreadStats.parse_threads(MessageBoardAPIWrapper._threads)
        CalcTopicStats.parse_topics(MessageBoardAPIWrapper._topics)
    except Exception as ex:
        print(
            "[MessageBoardAPIWrapper.main] "
            "Error while calculating statistics -- \n"
            f"{ex}\n"
        )

    # ---------------------------------------------------------------------------
    # Total number of messages
    # ---------------------------------------------------------------------------
    try:
        print(f"{LBL_TOTAL_NBR_MESSAGES}: {Messages.get_num_messages()}")
    except NotImplementedError:
        print(f"{LBL_TOTAL_NBR_MESSAGES}: {ERR_MSG_NOT_IMPLEMENTED}")
    except:
        print(f"{LBL_TOTAL_NBR_MESSAGES}: {ERR_MSG_GENERIC}")

    # ---------------------------------------------------------------------------
    # Most common word
    # ---------------------------------------------------------------------------
    try:
        print(
            f"{LBL_MOST_COMMON_WORD}: "
            f"{CalcMessageStats.get_most_common_word()}"
            f" ({CalcMessageStats.get_most_common_word_cnt()} {LBL_OCCURRENCES})"
        )
    except NotImplementedError:
        print(f"{LBL_MOST_COMMON_WORD}: {ERR_MSG_NOT_IMPLEMENTED}")
    except:
        print(f"{LBL_MOST_COMMON_WORD}: {ERR_MSG_GENERIC}")

    # ---------------------------------------------------------------------------
    # Avg. number of words per sentence
    # ---------------------------------------------------------------------------
    try:
        print(f"{LBL_AVG_NBR_WORDS}: {CalcMessageStats.get_avg_num_words_per_sentence():.3f}")
    except NotImplementedError:
        print(f"{LBL_AVG_NBR_WORDS}: {ERR_MSG_NOT_IMPLEMENTED}")
    except:
        print(f"{LBL_AVG_NBR_WORDS}: {ERR_MSG_GENERIC}")

    # ---------------------------------------------------------------------------
    # Avg. number of messages per thread, per topic
    # ---------------------------------------------------------------------------
    try:
        print(
            f"{LBL_AVG_NBR_MESSAGES}: "
            f"{CalcTopicStats.get_avg_num_msg_thread_topic()}"
        )
    except NotImplementedError:
        print(f"{LBL_AVG_NBR_MESSAGES}: {ERR_MSG_NOT_IMPLEMENTED}")
    except:
        print(f"{LBL_AVG_NBR_MESSAGES}: {ERR_MSG_GENERIC}")

    # ---------------------------------------------------------------------------
    # Write out entire message board JSON data to file
    # ---------------------------------------------------------------------------
    try:
        message_board.to_json()
        print(f"{LBL_MESSAGE_BOARD_WRITTEN}")
    except NotImplementedError:
        print(f"{LBL_MESSAGE_BOARD_WRITTEN}: {ERR_MSG_NOT_IMPLEMENTED}")
    except Exception as ex:
        print(f"{LBL_MESSAGE_BOARD_WRITTEN}: {ERR_MSG_GENERIC}")

    return


if __name__ == "__main__":
    main()
