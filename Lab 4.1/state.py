class CombinationLock:
    def __init__(self, combination):
        self.status = 'LOCKED'
        self.combination = combination
        self.digits = []
    
    def enter_digit(self, digit):
        self.digits.append(digit)
        slicedcombination = self.combination[:len(self.digits)]
        
        if self.digits == self.combination:
            self.status = 'OPEN'
        elif self.digits == slicedcombination:
            self.status = "".join(str(d) for d in self.digits)
        else:
            self.status = 'ERROR'


cl = CombinationLock([1, 2, 3, 4, 5])
print(cl.status)

cl.enter_digit(1)
print(cl.status)

cl.enter_digit(2)
print(cl.status)

cl.enter_digit(3)
print(cl.status)

cl.enter_digit(4)
print(cl.status)

cl.enter_digit(5)
print(cl.status)