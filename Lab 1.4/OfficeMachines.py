class Machine:

    def print(self, document):
        raise NotImplementedError("Print method not implemented")

    def fax(self, document):
        raise NotImplementedError("Fax method not implemented")

    def scan(self, document):
        raise NotImplementedError("Scan method not implemented")

class MultiFunctionPrinter(Machine):

    def print(self, document):
        print(f"Printing: {document}")

    def fax(self, document):
        print(f"Faxing: {document}")

    def scan(self, document):
        print(f"Scanning: {document}")

class OldFashionedPrinter(Machine):

    def print(self, document):
        print(f"Printing: {document}")

    def fax(self, document):
        pass

    def scan(self, document):
        raise NotImplementedError("Printer cannot scan")
    

"""Test the machines"""

printer = MultiFunctionPrinter()

printer.print("Hello world")
printer.fax("Test document")
printer.scan("Important document")

printer = OldFashionedPrinter()
try:
    printer.print("Hello world")
    printer.fax("Test document") 
    printer.scan("Important document")
except NotImplementedError as e:
    print(e)