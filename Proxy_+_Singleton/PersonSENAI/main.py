from person import Person
from responsible_person import ResponsiblePerson

responsible_person = ResponsiblePerson(Person(18))
print(responsible_person.drink())
print(responsible_person.drive())
print(responsible_person.drink_and_drive())