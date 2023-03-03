from person import Person


class ResponsiblePerson:
    def __init__(self, person: Person):
        self.person = person
        self.muito_jovem = "Too new"

    def drink(self) -> str:
        if (self.person.age < 18):
            return self.muito_jovem
        else:
            return self.person.drink()
        
    def drive(self) -> str:
        if (self.person.age < 16):
            return self.muito_jovem
        else:
            return self.person.drive()
        
    def drink_and_drive(self) -> str:
        return "Dead"