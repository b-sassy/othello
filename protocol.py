from typing import Protocol


class IO(Protocol):
    def coordinate(self, stone):
        pass