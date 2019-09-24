from calculator_app import CalculatorApp
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class Calculator(CalculatorApp):
    def build(self):
        self.open_parentheses = 0
        self.end = ''
        self.powers = ['⁰','¹','²','³','⁴','⁵','⁶','⁷','⁸','⁹']
        self.is_power = False
        self.pow = False
        self.button_labels = ['7','8','9','C','×',
                              '4','5','6','√','÷',
                              '1','2','3','Xʸ','+',
                              '.','0','(',')','−',
                              ]
        super().build()
        self.button_grid.cols = 5
        self.grid2 = GridLayout(cols=5)
        self.grid2.add_widget(Button(text='<',on_press=self.callback))
        self.grid2.add_widget(Button(text='>',on_press=self.callback))
        self.grid2.add_widget(Button(text='del',on_press=self.callback))
        self.grid2.add_widget(Button(text='=',size_hint_x=2,on_press=self.callback))
        self.parent.add_widget(self.grid2)
        
        return self.parent
    
    def _display_update(self,display_1,display_2=None):
        display_1 += self.end
        super()._display_update(display_1,display_2)
    
    def _cancel(self):
        self.is_power = False
        self.pow = False
        super()._cancel()
        
    def _del(self,last,pop):
        if self.pow == True:
            self.pow = False
        super()._del(last,pop)
    
    def _num(self,inp,pop):
        if self.is_power == True:
            inp = self.powers[int(inp)]
            self.pow = True
            self.is_power = False
        elif self.pow == True:
            self.inp = pop
            self.inp += inp
            self.pow = False
        super()._num(inp,pop)
        self.oper = None
        
    def _oper(self,inp,last,pop):
        if self.pow == True:
            self.pow = False
        super()._oper(inp,last,pop)
        
    def _sqrt(self,inp,last):
        if last in self.operators or last == '(' or self.inp == '':
            self.inp += inp
        elif self.is_result == True:
            self.inp = inp+self.result
            self.is_result = False
        
    def _back_space(self,last):
        if len(self.inp) > 1:
            self.end = last+self.end
            self.inp = self.inp[:len(self.inp)-1]
        else:
            self.end = self.inp+self.end
            self.inp = ''
        
    def _forward_space(self):
        if len(self.end) > 1:
            self.inp += self.end[0]
            self.end =  self.end[1:]
        else:
            
            self.inp += self.end
            self.end = ''
        
    def _get_parentheses(self,par,last):
        if par == '(':
            if self.is_result == True:
                self.inp = '('+self.result
                self.is_result = False
                self.open_parentheses += 1
            elif last in self.operators or self.inp == '' or self.inp == '√' or last == '√':
                self.inp += '('
                self.open_parentheses += 1
        elif par == ')' and self.open_parentheses > 0 and last not in self.operators:
            self.inp += ')'
            self.open_parentheses -= 1
    
    def _par_parse(self):
        _string = self.inp[::-1]
        while self.open_parentheses > 0:
            _string.remove('(')
        self.inp = _string[::-1]
        
    def _get_result(self):
        self.inp += self.end
        self.end = ''
        if self.open_parentheses > 0:
            self._par_parse()
        super()._get_result()

    def callback(self,instance):
        inp = instance.text
        last = self.inp[:len(self.inp)-2:-1]
        if inp == '<':
            self._back_space(last)
        if inp == '>':
            self._forward_space()
        if inp == '(':
            self._get_parentheses('(',last)
            self._display_update(self.inp)
        if inp == ')':
            self._get_parentheses(')',last)
            self._display_update(self.inp)
        if inp == 'Xʸ':
            if self.pow == False and self.oper == None:
                self.is_power = True
        if inp == '=':
            if self.pow == True:
                self.pow = False
            elif self.is_power == True:
                self.is_power = False
            self._get_result()
        elif inp == '√':
            self._sqrt(inp,last)
            self._display_update(self.inp)
        else:
            super().callback(instance)
        

if __name__ == '__main__':
    Calculator().run()