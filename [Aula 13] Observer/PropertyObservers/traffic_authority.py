from person import Person


class TrafficAuthority:
    def __init__(self, person: Person) -> None:
        self.person = person
        person.property_changed.append(self.person_changed)

    def person_changed(self, name: str, value: int):
        if (name == "age"):
            if (value < 16):
                print("Sorry, you sill cannot drive.")
            else:
                print("Okay, you can drive now")
                self.person.property_changed.remove(
                    self.person_changed
                )