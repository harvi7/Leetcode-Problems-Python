class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._msg_dict = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if not message in self._msg_dict or 10 <= timestamp - self._msg_dict[message]:
            self._msg_dict[message] = timestamp
            return True
        return False
