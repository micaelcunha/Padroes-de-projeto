class Event(list):
    def __call__(self, *args, **kwargs) -> None:
        for item in self:
            self.tuple = args
            item(*args, **kwargs)