import math

class LargeNumber{
    def set_LargeNumber(self, A, B):
        self.A = A
        self.B = B
}

def exponent(n):
    left = 0.5 * math.log10(2*math.pi*n)
    right = n * math.log10*(n / math.e)

    return left + right

