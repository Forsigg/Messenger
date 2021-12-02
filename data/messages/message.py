from dataclasses import dataclass


@dataclass
class Message:
    text: str
    author: str
    receiver: str



