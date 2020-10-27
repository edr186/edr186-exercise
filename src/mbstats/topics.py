import requests


class Topics:
    """
    Singleton class for loading Topics from API
    """
    _topics: dict = {}

    _topics_url: str

    _is_loaded: bool = False
    _is_error: bool = False

    _error: Exception

    @staticmethod
    def set_url(url: str):
        Topics._topics_url = url

    @staticmethod
    def load_topics():
        """
        - Calls API to retrieve all topics in JSON format
        - Encapsulates in local dictionary using Singleton pattern
        """
        if Topics._is_loaded:
            return

        if Topics._is_error:
            raise Topics._error

        try:
            response = requests.get(Topics._topics_url)

            if response.status_code != 200:
                raise Exception(
                    "[Topics.load_topics()] "
                    f"Error calling API, HTTP Status Code = {response.status_code}"
                )
        except Exception as ex:
            Topics._is_error = True
            Topics._error = ex

            raise Topics._error

        Topics._topics = response.json()

    @staticmethod
    def get_all_topics() -> dict:
        """
        Returns dict with all threads
        """
        Topics.load_topics()

        return Topics._topics

    @staticmethod
    def get_num_topics() -> int:
        """
        Returns the total number of threads
        """
        Topics.load_topics()

        return len(Topics._topics)
