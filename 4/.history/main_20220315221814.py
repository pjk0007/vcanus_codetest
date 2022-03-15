import math
from re import A

class LargeNumber{
    def setLargeNumber(self, A, B):
        self.A = A
        self.B = B
}

def exponent(n):
    left = 0.5 * math.log10(2*math.pi*n)
    right = n * math.log10*(n / math.e)

    return left + right

