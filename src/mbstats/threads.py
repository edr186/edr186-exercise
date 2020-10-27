import requests


class Threads:
    """
    Singleton class for loading Threads from API
    """
    _threads: dict = {}

    _threads_url: str

    _is_loaded: bool = False
    _is_error: bool = False

    _error: Exception

    @staticmethod
    def set_url(url: str):
        Threads._threads_url = url

    @staticmethod
    def load_threads():
        """
        - Calls API to retrieve all threads in JSON format
        - Encapsulates in local dictionary using Singleton pattern
        """
        if Threads._is_loaded:
            return

        if Threads._is_error:
            raise Threads._error

        try:
            response = requests.get(Threads._threads_url)

            if response.status_code != 200:
                raise Exception(
                    "[Threads.load_threads()] "
                    f"Error calling API, HTTP Status Code = {response.status_code}"
                )
        except Exception as ex:
            Threads._is_error = True
            Threads._error = ex

            raise Threads._error

        Threads._threads = response.json()

    @staticmethod
    def get_all_threads() -> dict:
        """
        Returns dict with all threads
        """
        Threads.load_threads()

        return Threads._threads

    @staticmethod
    def get_num_threads() -> int:
        """
        Returns the total number of threads
        """
        Threads.load_threads()

        return len(Threads._threads)
