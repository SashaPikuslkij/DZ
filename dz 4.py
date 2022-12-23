class Table:
    def __init__(self):
        super().init()
        self.material = "wood"
        self.fixed_clasps = "nails"


class Armchair:
    def __init__(self):
        super().init()
        self.material1 = "cloth"
        self.subject_of_support = "springs"


class Bed(Armchair, Table):
    def printer(self):
        print(self.material)
        print(self.fixed_clasps)


print(self.subject_of_support)
print(self.material1)

bed = Bed()
bed.printer()

import random

x = random.randit(0,99)
y = random.randit(0,99)

class Hidden_calculation:
    _calculation = (x-y)

    def Sum_printer(self):
        print(self._calculation)

calculation1 = Hidden_calculation()
calculation1.Sum_printer()