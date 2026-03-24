from interfaces import Printer, Scanner, Fax

class MyPrinter(Printer):
    def print(self, document):
        print(f"Printing: {document}")

class Photocopier(Printer, Scanner):
    def print(self, document):
        print(f"Photocopying: {document}")

    def scan(self, document):
        print(f"Scanning: {document}")

class MultiFunctionMachine(Printer, Scanner):

    def __init__(self, printer, scanner):
        self.printer = printer
        self.scanner = scanner

    def print(self, document):
        print(f"Printing: {document}")

    def scan(self, document):
        print(f"Scanning: {document}")