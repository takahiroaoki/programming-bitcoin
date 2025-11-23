class FieldElement:
    def __init__(self, num: int, prime: int):
        if num > prime or num < 0:
            error = f'Num {num} not in field range 0 to {prime - 1}'
            raise ValueError(error)
        self.num = num
        self.prime = prime

    def __repr__(self) -> str:
        return f'FieldElement_{self.num}({self.prime})'

    def __eq__(self, other: __build_class__) -> bool:
        if other is None:
            return False
        return self.num == other.num and self.prime == other.prime
    
    def __ne__(self, other: __build_class__) -> bool:
        return not self.__eq__(other)

    def __add__(self, other: __build_class__) -> __build_class__:
        if self.prime != other.prime:
            raise TypeError('Cannot add two numbers in different Fields')
        num = (self.num + other.num) % self.prime
        return self.__class__(num, self.prime)

    def __sub__(self, other: __build_class__) -> __build_class__:
        if self.prime != other.prime:
            raise TypeError('Cannot add two numbers in different Fields')
        num = (self.num - other.num) % self.prime
        return self.__class__(num, self.prime)

    def __pow__(self, exponent: int) -> __build_class__:
        exp = exponent % (self.prime - 1)
        num = pow(self.num, exp, self.prime)
        return self.__class__(num, self.prime)

    def __mul__(self, other: __build_class__) -> __build_class__:
        if self.prime != other.prime:
            raise TypeError('Cannot add two numbers in different Fields')
        num = (self.num * other.num) % self.prime
        return self.__class__(num, self.prime)
    
    def __truediv__(self, other: __build_class__) -> __build_class__:
        if self.prime != other.prime:
            raise TypeError('Cannot add two numbers in different Fields')
        inv_other = other ** (self.prime - 2)
        return self * inv_other
