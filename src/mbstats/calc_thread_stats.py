from src.mbstats.calc_topic_stats import CalcTopicStats

JSON_THREAD_ID = "id"
JSON_THREAD_TOPIC_ID = "topic"


class CalcThreadStats:
    """
    Helper class to calculate statistics and expose them
    """
    _init: bool = False

    _messages_per_thread: dict = {}

    @staticmethod
    def parse_threads(threads: dict):
        """
        Parses the threads to calculate statistics
         - Stores the statistics in internal variables
        """
        if CalcThreadStats._init:
            return

        # Loop through each thread, increment stats on the topic
        for thread in threads:
            thread_id: int = thread[JSON_THREAD_ID]
            topic_id: int = thread[JSON_THREAD_TOPIC_ID]

            cnt = CalcThreadStats.get_message_cnt(thread_id)

            CalcTopicStats.increment_thread_cnt(topic_id, 1)
            CalcTopicStats.increment_message_cnt(topic_id, cnt)

        CalcThreadStats._init = True

    @staticmethod
    def increment_message_cnt(thread_id: int, cnt: int):
        if thread_id in CalcThreadStats._messages_per_thread:
            CalcThreadStats._messages_per_thread[thread_id] += cnt
        else:
            CalcThreadStats._messages_per_thread[thread_id] = cnt

    @staticmethod
    def get_message_cnt(thread_id: int) -> int:
        if thread_id in CalcThreadStats._messages_per_thread:
            return CalcThreadStats._messages_per_thread[thread_id]
        else:
            return 0

    @staticmethod
    def print_thread_stats():
        print(CalcThreadStats._messages_per_thread)
