import random


class Database:
    _instance = None

    def __init__(self) -> None:
        print("Call second.")
        self.id = random.randint(1, 101)
        print('Generated an id of ', self.id)
        print('Loading database from file')

    def __new__(cls, *args, **kwargs):
        print("Call first.")
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)

        return cls._instance
