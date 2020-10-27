from src.mbstats.calc_thread_stats import CalcThreadStats

JSON_MESSAGE_CONTENT = "content"
JSON_MESSAGE_THREAD_ID = "thread"


class CalcMessageStats:
    """
    Helper class to calculate statistics and expose them
    """
    _init: bool = False

    # Initialize variables to store statistics
    _num_words = 0
    _num_sentences = 0
    _most_common_word: str = "[N/A]"
    _most_common_word_cnt: int = 0

    @staticmethod
    def parse_messages(messages: dict):
        """
        Parses the messages to calculate statistics
         - Stores the statistics in internal variables
        """
        if CalcMessageStats._init:
            return

        # Create a dictionary with a list of words and counts
        word_map: dict = {}

        # Loop through each message, parse the 'content' field
        for message in messages:
            thread_id: int = message[JSON_MESSAGE_THREAD_ID]
            CalcThreadStats.increment_message_cnt(thread_id, 1)

            content: str = message[JSON_MESSAGE_CONTENT]

            for word in content.split():
                CalcMessageStats._num_words += 1

                # Standardize words using lower-case
                word = word.lower()

                # Check for end-of-sentence
                if word[-1] in {'.', '!', '?'}:
                    CalcMessageStats._num_sentences += 1
                    word = word[:-1]

                # If 'word' exists in the map, increment the counter
                if word in word_map:
                    word_cnt = word_map[word] + 1
                    word_map[word] = word_cnt

                    # Check to see if this is the most common word
                    if word_cnt > CalcMessageStats._most_common_word_cnt:
                        # print(f"Most common word -- ")
                        # print(f"{CalcMessageStats.most_common_word}:{CalcMessageStats.most_common_word_cnt}")

                        CalcMessageStats._most_common_word = word
                        CalcMessageStats._most_common_word_cnt = word_cnt

                # Else if 'word' is not in the map yet, then add it with count=1
                else:
                    word_map[word]: int = 1

        CalcMessageStats._init = True

    @staticmethod
    def get_most_common_word() -> str:
        if not CalcMessageStats._init:
            raise Exception(
                "[CalcMessageStats.get_most_common_word()] "
                "Error - statistics not calculated yet"
            )

        return CalcMessageStats._most_common_word

    @staticmethod
    def get_most_common_word_cnt() -> int:
        if not CalcMessageStats._init:
            raise Exception(
                "[CalcMessageStats.get_most_common_word_cnt()] "
                "Error - statistics not calculated yet"
            )

        return CalcMessageStats._most_common_word_cnt

    @staticmethod
    def get_num_words() -> int:
        if not CalcMessageStats._init:
            raise Exception(
                "[CalcMessageStats.get_num_words()] "
                "Error - statistics not calculated yet"
            )

        return CalcMessageStats._num_words

    @staticmethod
    def get_num_sentences() -> int:
        if not CalcMessageStats._init:
            raise Exception(
                "[CalcMessageStats.get_num_sentences()] "
                "Error - statistics not calculated yet"
            )

        return CalcMessageStats._num_sentences

    @staticmethod
    def get_avg_num_words_per_sentence() -> float:
        if not CalcMessageStats._init:
            raise Exception(
                "[CalcMessageStats.get_avg_num_words_per_sentence()] "
                "Error - statistics not calculated yet"
            )

        avg_num_words_per_sentence = CalcMessageStats._num_words / CalcMessageStats._num_sentences

        return avg_num_words_per_sentence
