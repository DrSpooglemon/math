from math import sqrt

class Calculator:
    def __init__(self,string):
        if '×' in string:
            e = string.partition('×')
            N1 = e[0]
            f = e[1]
            N2 = e[2]
        elif '÷' in string:
            e = string.partition('÷')
            N1 = e[0]
            f = e[1]
            N2 = e[2]
        elif '+' in string:
            e = string.partition('+')
            N1 = e[0]
            f = e[1]
            N2 = e[2]
        elif '−' in string:
            e = string.partition('−')
            N1 = e[0]
            f = e[1]
            N2 = e[2]
        else:
            N1 = string
            f = None
            N2 = None
        if '√' in N1:
            r1 = True
            N1 = N1.partition('√')[2]
        else:
            r1 = False
        if '²' in N1:
            if r1 == False:
                s1 = True
            else:
                r1 = False
                s1 = False
            N1 = N1.partition('²')[0]
        else:
            s1 = False
        if N2 != None:
            if '√' in N2:
                r2 = True
                N2 = N2.partition('√')[2]
            else:
                r2 = False
            if '²' in N2:
                if r2 == False:
                    s2 = True
                else:
                    r2 = False
                    s2 = False
                N2 = N2.partition('²')[0]
            else:
                s2 = False
        if '.' in N1:
            self.N1 = float(N1)
            if self.N1 - int(self.N1) == 0:
                self.N1 = int(self.N1)
        else:
            self.N1 = int(N1)
        self.sqrt1 = r1
        self.sq1 = s1
        self.oper = f
        if N2 != None:
            if '.' in N2:
                self.N2 = float(N2)
                if self.N2 - int(self.N2) == 0:
                    self.N2 = int(self.N2)
            else:
                self.N2 = int(N2)
            self.sqrt2 = r2
            self.sq2 = s2
        else:
            self.N2 = N2
            self.sqrt2 = None
            self.sq2 = None

    def __str__(self):
        if self.sqrt1 == True:
            e = '√' + str(self.N1)
        elif self.sq1 == True:
            e = str(self.N1) + '²'
        else:
            e = str(self.N1)
        if self.N2 == None:
            e += '='
        else:
            e += self.oper
            if self.sqrt2 == True:
                e += '√' + str(self.N2) + '='
            elif self.sq2 == True:
                e += str(self.N2) + '²' + '='
            else:
                e += str(self.N2) + '='

        return e

    def calculate(self):
        N1 = self.N1
        N2 = self.N2
        f = self.oper
        if N1 != None:
            if self.sqrt1 == True:
                N1 = sqrt(N1)
            elif self.sq1 == True:
                N1 = N1**2
            if self.N2 != None:
                if self.sqrt2 == True:
                    N2 = sqrt(N2)
                elif self.sq2 == True:
                    N2 = N2**2
                if f == '×':

                    return N1*N2
                elif f == '÷':
                    if N2 == 0:
                        return 'Error: division by zero'
                    else:
                        return N1/N2
                elif f == '+':

                    return N1+N2
                elif f == '−':

                    return N1-N2
            else:

                return N1


