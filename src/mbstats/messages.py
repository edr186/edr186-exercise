import requests


class Messages:
    """
    Singleton class for loading Messages from API
    """
    _messages: dict = {}

    _messages_url: str

    _is_loaded: bool = False
    _is_error: bool = False

    _error: Exception

    @staticmethod
    def set_url(url: str):
        Messages._messages_url = url

    @staticmethod
    def load_messages():
        """
        - Calls API to retrieve all messages in JSON format
        - Encapsulates in local dictionary using Singleton pattern
        """
        if Messages._is_loaded:
            return

        if Messages._is_error:
            raise Messages._error

        try:
            response = requests.get(Messages._messages_url)

            if response.status_code != 200:
                raise Exception(
                    "[Messages.load_messages()] "
                    f"Error calling API, HTTP Status Code = {response.status_code}"
                )
        except Exception as ex:
            Messages._is_error = True
            Messages._error = ex

            raise Messages._error

        Messages._messages = response.json()

    @staticmethod
    def get_all_messages() -> dict:
        """
        Returns dict with all messages
        """
        Messages.load_messages()

        return Messages._messages

    @staticmethod
    def get_num_messages() -> int:
        """
        Returns the total number of messages
        """
        Messages.load_messages()

        return len(Messages._messages)
