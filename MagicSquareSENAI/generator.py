from random import randint


class Generator:
    def generate(self, count):
        return [randint(1, 9) for x in range(count)]
