from collections import deque

class Messages(deque):

    def __init__(
        self, 
        history_limit: int = 10
    ):
        super().__init__()
        self.history_limit = history_limit
        self._context = ""

    
    def append(
        self, 
        message):
        if len(self) >= self.history_limit:
            self.popleft()
        super().append(message)