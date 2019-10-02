from calculator_app import CalculatorApp

class Calculator(CalculatorApp):
        
    def build(self):
        self._display_update('','')
        return self.parent
    
    def callback(self,instance):
        inp = instance.text
        if inp.isdigit():
            if self.is_result == True:
                self._display_update('',self.result)
                self.is_result = False
            self._num(inp)
        elif 'X' in inp:
            if self.is_result == True:
                self.inp.extend(self.result)
                self.is_result = False
            self._exp(inp)
        elif inp == '.':
            if self.is_result == True:
                self.inp.extend(self.result)
                self.is_result = False
            self._dec()
        elif inp == self.sqrt:
            self._sqrt(self.sqrt)
            if self.is_result == True:
                self.inp.extend(self.result)
                self.is_result = False
        elif inp in self.display_operators:
            if self.is_result == True:
                self.inp.extend(self.result)
                self.is_result = False
            self._oper(inp)
        elif inp == '(' or inp == ')':
            self._parentheses(inp)
            if self.is_result == True and inp == '(':
                self.inp.extend(self.result)
                self.is_result = False
        elif inp == 'del':
            if self.is_result == True:
                self.inp.extend(self.result)
                self.is_result = False
            self._del()
        elif inp == 'C':
            self._cancel()
        elif inp == '=':
            l = len(self.inp)
            if l > 1 and list(self.inp[l-1].items())[0][0] != 'oper':
                self._get_result()
                return None
        if self.is_result == False:
            self._display_update(self.inp)

if __name__ == '__main__':
    Calculator().run()