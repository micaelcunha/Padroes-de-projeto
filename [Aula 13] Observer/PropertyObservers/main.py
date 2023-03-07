from person import Person
from traffic_authority import TrafficAuthority

person = Person()
traffic_authority = TrafficAuthority(person)
for age in range(14, 20):
    print(f"Setting age to {age}")
    person.age = age
