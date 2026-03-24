from Relationship import Relationship

class Research:
    def __init__(self, Browser):
        for child in Browser.find_all_children_of("John"):
            print(f"John has a child called {child}")