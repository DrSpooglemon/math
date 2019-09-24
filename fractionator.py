class Fraction:
    def __init__(self,frac,unit=0):
        assert type(frac[0]) == int and type(frac[1]) == int and type(unit) == int
        top = frac[0]
        bottom = frac[1]
        for i in reversed(range(2,11)):
            while top != 0 and bottom != 0 and top % i == 0 and bottom % i == 0:
                top /= i
                bottom /= i
        if unit < 0:
            top = -top
        while top > bottom:
            top -= bottom
            unit += 1
        while -top > bottom:
            top += bottom
            unit -= 1
        self.num = int(top)
        self.denom = int(bottom)
        self.unit = int(unit)

    def __str__(self):
        if self.num != 0 and self.denom != 0:
            if self.unit == 0:
                return str(self.num) + "/" + str(self.denom)
            else:
                if self.num < 0:
                    self.num = -self.num
                return str(self.unit) + " " + str(self.num) + "/" + str(self.denom)
        else:
            return str(self.unit)


    def __add__(self,other):
        top = self.num*other.denom + other.num*self.denom
        bottom = self.denom*other.denom
        unit = self.unit + other.unit

        return Fraction((int(top),int(bottom)),unit)

    def __sub__(self,other):
        unit = self.unit-other.unit
        if unit != 0 and other.num/other.denom > self.num/self.denom:
            n = unit*other.denom - other.num
            top = self.num*other.denom + n*self.denom
            bottom = self.denom*other.denom
            unit = 0
        else:
            top = self.num*other.denom - other.num*self.denom
            bottom = self.denom*other.denom

        return Fraction((int(top),int(bottom)),unit)

    def __mul__(self,other):
        if self.unit != 0:
            top_a = self.unit*self.denom + self.num
        else:
            top_a = self.num
        bottom_a = self.denom
        if other.unit != 0:
            top_b = other.unit*other.denom + other.num
        else:
            top_b = other.num
        bottom_b = other.denom
        top = top_a * top_b
        bottom = bottom_a * bottom_b

        return Fraction((int(top),int(bottom)))

    def __div__(self,other):
        if self.unit != 0:
            top_a = self.unit*self.denom + self.num
        else:
            top_a = self.num
        bottom_a = self.denom
        if other.unit != 0:
            top_b = other.unit*other.denom + other.num
        else:
            top_b = other.num
        bottom_b = other.denom
        top = top_a * bottom_b
        bottom = bottom_a * top_b

        return Fraction((int(top),int(bottom)))


    def __float__(self):

        return self.unit+self.num/self.denom

    def inverse(self):
        if self.unit != 0:
            self.num += self.denom*self.unit
            self.unit == 0
        return Fraction((self.denom,self.num))

