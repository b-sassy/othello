from typing import Protocol


class IO(Protocol):
    def receive_coordinates(self, stone):
        pass