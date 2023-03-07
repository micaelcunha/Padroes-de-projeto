from property_observable import PropertyObservable


class Person(PropertyObservable):
    def __init__(self, age: int = 0) -> None:
        super().__init__()
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value: int):
        if self._age == value:
            return
        self._age = value
        self.property_changed("age", value)
