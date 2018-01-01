# some behaviour that I want to implement
# write some __function__ -> these are data model methods
# top level functions or top level syntax -> corresponding __
# x + y     ->      __add__
# init x    ->      __init__
# x()       ->      __call__
# PROTOCOL VIEW OF PYTHON
# #1 PYTHON OBJECT ORIENTED DESIGN PATTERN

class Polynomial:
    def __init__(self, *coeffs):
        self.coeffs = coeffs

    # representation
    def __repr__(self):
        return "Polynomial(*{!r})".format(self.coeffs)

    def __add__(self, other):
        return Polynomial(*(x + y for x, y in zip(self.coeffs, other.coeffs)))

    def __len__(self):
        return len(self.coeffs)


p1 = Polynomial(1, 2, 3) #  x2 + 2x + 3
p2 = Polynomial(3, 4, 3) # 3x2 + 4x + 3