from mediator import Mediator


class ComponenteBase:
    def __init__(self, mediator: Mediator = None) -> None:
        self.mediator = mediator