from enum import Enum, auto


class EventType(Enum):
    INPUT = auto(),
    UPDATE = auto()
    UPDATED = auto()


class Event:
    def __init__(self, evtype):
        self.type = evtype


class InputEvent(Event):
    def __init__(self, vec):
        Event.__init__(self, EventType.INPUT)
        self.vec = vec
