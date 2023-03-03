from database import Database

class Main:
    def __init__(self):
        self.datab1 = Database()
        self.datab2 = Database()


main = Main()

print(main.datab1 == main.datab2) 