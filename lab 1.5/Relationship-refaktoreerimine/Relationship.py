from enum import Enum
from abc import ABC, abstractmethod

class Relationship(Enum):
    Parent = 0
    Child = 1
    Sibling = 2

class Person:
    def __init__(self, name):
        self.name = name

class Browser(ABC):
    @abstractmethod
    def find_all_children_of(self, name):
        pass

class Relationships(Browser):
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.Parent, child))
        self.relations.append((child, Relationship.Child, parent))

    def find_all_children_of(self, name):
        for relation in self.relations:
            if relation[0].name == name and relation[1] == Relationship.Parent:
                yield relation[2].name