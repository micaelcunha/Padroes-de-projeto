class Event(list):
    def __call__(self, *args, **kwds) -> None:
        for item in self:
            item(*args, **kwds)