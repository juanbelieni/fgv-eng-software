from typing import Literal
from collections import defaultdict

Type = Literal["success", "failure"]


class NotificationObserver:
    subscribers: list

    def __init__(self):
        self.subscribers = defaultdict(list)

    def subscribe(self, type: Type, fn):
        self.subscribers[type].append(fn)

    def unsubscribe(self, type: Type, fn):
        self.subscribers[type].remove(fn)

    def notify(self, type: Type, message: str):
        for fn in self.subscribers[type]:
            fn(message)


notification_observer = NotificationObserver()
