import math

class LargeNumber:
    def __str__(self):
        return str(self.A) + ' * 10^' + str(self.e)

    def set_LargeNumber(self, A, e):
        self.A = A
        self.e= e

    def exponent(self, num):
        left = 0.5 * math.log10(2*math.pi*num)
        right = num * math.log10(num / math.e)

        return left + right

    def factorial(self, num):
        self.e = math.floor(self.exponent(num))
        self.A = 10**(self.exponent(num) - self.e)

        return self

large_number = LargeNumber().factorial(1000000)
print(large_number)