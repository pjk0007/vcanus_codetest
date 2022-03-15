import math

class LargeNumber:
    def __str__(self):
        return self.A + ' *  10^' + self.B

    def set_LargeNumber(self, A, e):
        self.A = A
        self.e= e

    def exponent(self, num):
        left = 0.5 * math.log10(2*math.pi*num)
        right = num * math.log10(num / math.e)

        return left + right

    def factorial(self, num):
        self.e = round(self.exponent(num))
        self.A = self.exponent(num) - round(self.exponent(num))

large_number = LargeNumber()
print(large_number.factorial(1000000))