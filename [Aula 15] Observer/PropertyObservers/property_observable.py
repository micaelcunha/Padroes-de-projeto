from event import Event


class PropertyObservable:
    def __init__(self) -> None:
        self.property_changed = Event()
