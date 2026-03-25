def is_singleton(factory):
    object1 = factory()
    object2 = factory()
    return object1 is object2


class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"{self.id} - {self.name}"

class PersonFactory:
    def __init__(self):
        self.current_id = 0

    def create_person(self, name):
        value = Person(self.current_id, name)
        self.current_id += 1
        return value

factory = PersonFactory()

print(is_singleton(lambda: factory.create_person("John")))
