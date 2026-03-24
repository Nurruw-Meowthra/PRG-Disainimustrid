from enum import Enum

class Person:
    def __init__(self, name):
        self.name = name

class Relationship(Enum):
    Parent = 0
    Child = 1
    Sibling = 2

class Relationships:
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.Parent, child))
        self.relations.append((child, Relationship.Child, parent))

class Research:
    def __init__(self, Relationships):
        for relation in Relationships.relations:
            if relation[0].name == "John" and relation[1] == Relationship.Parent:
                print(f"John has a child called {relation[2].name}")


"""Test functions"""
parent = Person("John")
child1 = Person("Chris")
child2 = Person("Matt")

relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

Research(relationships)