__author__ = 'Kelly'

def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:

    def __init__(self, n, d):
        self.num = n
        self.den = d

        assert n % 1 == 0, "Error! this is not an integer!"
        assert d % 1 == 0, "Error! this is not an integer!"



    def __repr__(self):
        return str(self.num) + '/' + str(self.den)



    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + otherfraction.num * self.den
        newden = self.den * otherfraction.den
        cd = gcd(newnum,newden)
        return Fraction(newnum//cd,newden//cd)

    def __sub__(self, otherfraction):
        newnum = self.num * otherfraction.den - self.den*otherfraction.num
        newden = self.den*otherfraction.den
        cd = gcd(newnum,newden)
        return Fraction(newnum//cd, newden//cd)

    def __mul__(self, otherfraction):

        newnum = (self.num * otherfraction.num)
        newden = self.den*otherfraction.den
        cd = gcd(newnum,newden)
        return Fraction(newnum//cd, newden//cd)


    def __truediv__(self, otherfraction):
        newnum = (self.num * otherfraction.den)
        newden = self.den * otherfraction.num
        cd = gcd(newnum,newden)
        return Fraction(newnum//cd, newden//cd)


    def __gt__(self, otherfraction):
        return(self.num > otherfraction.num and self.den > otherfraction.den)
    def __ge__(self, otherfraction):
        return(self.num >= otherfraction.num and self.den >= otherfraction.den)
    def __lt__(self, otherfraction):
        return(self.num < otherfraction.num and self.den < otherfraction.den)
    def __le__(self, otherfraction):
        return(self.num <= otherfraction.num and self.den <= otherfraction.den)
    def __ne__(self, otherfraction):
        return(self.num != otherfraction.num and self.den != otherfraction.den)

    def __eq__(self, otherfraction):
        return(self.num == otherfraction.num and self.den == otherfraction.den)

f1 = Fraction(1,4)
f2 = Fraction(1,2)




f3 = f1 + f2
f4 = f1 - f2
f5 = f1 * f2
f6 = f1 / f2

a = str(f1)
b = str(f2)
add = str(f3)
sub = str(f4)
mult = str(f5)
div = str(f6)

print(a + " + " + b + " = " + add)
print(a + " - " + b + " = " + sub)
print(a + " * " + b + " = " + mult)
print(a + " / " + b + " = " + div)


