JSON_TOPIC_ID = "id"
JSON_TOPIC_TITLE = "title"


class CalcTopicStats:
    """
    Helper class to calculate statistics and expose them
    """
    _init: bool = False

    _topics: dict = {}

    _threads_per_topic: dict = {}
    _messages_per_topic: dict = {}

    @staticmethod
    def parse_topics(topics: dict):
        CalcTopicStats._topics = topics

    @staticmethod
    def increment_thread_cnt(topic_id: int, cnt: int):
        if topic_id in CalcTopicStats._threads_per_topic:
            CalcTopicStats._threads_per_topic[topic_id] += cnt
        else:
            CalcTopicStats._threads_per_topic[topic_id] = cnt

    @staticmethod
    def get_thread_cnt(topic_id: int) -> int:
        if topic_id in CalcTopicStats._threads_per_topic:
            return CalcTopicStats._threads_per_topic[topic_id]
        else:
            return 0

    @staticmethod
    def increment_message_cnt(topic_id: int, cnt: int):
        if topic_id in CalcTopicStats._messages_per_topic:
            CalcTopicStats._messages_per_topic[topic_id] += cnt
        else:
            CalcTopicStats._messages_per_topic[topic_id] = cnt

    @staticmethod
    def get_message_cnt(topic_id: int) -> int:
        if topic_id in CalcTopicStats._messages_per_topic:
            return CalcTopicStats._messages_per_topic[topic_id]
        else:
            return 0

    @staticmethod
    def print_topic_stats():
        print(f"Threads per Topic : {CalcTopicStats._threads_per_topic}")
        print(f"Messages per Topic: {CalcTopicStats._messages_per_topic}")

    @staticmethod
    def get_avg_num_msg_thread_topic() -> dict:
        avg_num_msg_thread_topic: dict = {}

        for topic in CalcTopicStats._topics:
            topic_id = topic[JSON_TOPIC_ID]
            topic_title = topic[JSON_TOPIC_TITLE]

            nbr_threads = CalcTopicStats.get_thread_cnt(topic_id)
            nbr_messages = CalcTopicStats.get_message_cnt(topic_id)

            avg_num_msg_thread = nbr_messages / nbr_threads

            avg_num_msg_thread_topic[topic_title] = avg_num_msg_thread

        return avg_num_msg_thread_topic

