from collections import deque

class Messages(deque):

    def __init__(
        self, 
    ):
        super().__init__()
        self._context = ""


    def inject_context(self, context: str):
        self._context = context