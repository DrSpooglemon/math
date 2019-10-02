from calculator_obj import Calculator
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.utils import platform

class CalculatorApp(App):
    def __init__(self):
        super(CalculatorApp,self).__init__()
        self.inp = []
        self.equation = ''
        self.result = []
        self.n_dec = 8
        self.auto_close_par = []
        self.is_exp = False
        self.is_result = False
        self.display_operators = ['×','÷','+','−']
        self.operators = ['*','/','+','-']
        self.sqrt = '√'
        self.sqr = 'X²'
        self.cube = 'X³'
        self.parent = BoxLayout(orientation='vertical')
        self.display_1 = Label(text='',size_hint_y=1.2)
        self.display_2 = Label(text='',size_hint_y=1)
        self.superscripts = ['⁰','¹','²','³','⁴','⁵','⁶','⁷','⁸','⁹']
        self.button_labels = ['7','8','9','×','C',
                              '4','5','6','÷','√',
                              '1','2','3','+','X²',
                              '.','0','del','−','Xʸ',
                              ]
        self.button_grid = GridLayout(cols=5,size_hint_y=3.8)
        for label in self.button_labels:
            button = Button(text=label)
            button.bind(on_press=self.callback)
            self.button_grid.add_widget(button)
        self.grid2 = GridLayout(cols=3)
        self.grid2.add_widget(Button(text='(',on_press=self.callback,size_hint_x=1))
        self.grid2.add_widget(Button(text=')',on_press=self.callback,size_hint_x=1))
        self.grid2.add_widget(Button(text='=',on_press=self.callback,size_hint_x=3))
        self.parent.add_widget(self.display_2)
        self.parent.add_widget(self.display_1)
        self.parent.add_widget(self.button_grid)
        self.parent.add_widget(self.grid2)
        
    def _display_update(self,display_1,display_2=None):
        if type(display_1) is str:
            _string = display_1
        else:
            _string = ''
            for item in display_1:
                item = list(item.items())[0]
                if item[0] == 'exp':
                    for l in range(len(item[1])):
                        _string += self.superscripts[int(item[1][l:l+1])]
                elif item[0] == 'oper':
                    _string += self.display_operators[self.operators.index(item[1])]
                else:
                    _string += item[1]
            if len(self.auto_close_par) > 0:
                _string += ' '
                for item in self.auto_close_par:
                    _string += ')'
        if _string == '':
            _string = '0'
        self.display_1.text = _string
        if display_2 != None:
            if type(display_2) is str:
                _string = display_2
                for i,o in enumerate(self.operators):
                    for _ in range(str(_string).count(o)):
                        p = _string.partition(o)
                        _string = p[0]+self.display_operators[i]+p[2]
            elif type(display_2) is list:
                _string = ''
                for item in display_2:
                    _string += list(item.items())[0][1]
            self.display_2.text = _string
            
    def _num(self,inp):
        pos = len(self.inp)-1
        if pos == -1:
            self.inp.extend([{'num':inp}])
        else:
            key = list(self.inp[pos].keys())[0]
            if self.is_exp == False:
                if 'num' in key or 'exp' in key:
                    self.inp[pos][key] += inp
                elif 'oper' in key or 'sqrt' in key or 'open_par' in key or 'neg' in key:
                    self.inp.extend([{'num':inp}])
            else:
                if 'num' in key or 'close_par' in key: 
                    self.inp.extend([{'exp':inp}])
                    self.is_exp = False
            
    def _dec(self):
        pos = len(self.inp)-1
        if pos == -1:
            self.inp.extend([{'num':'0'+'.'}])
        else:
            key = list(self.inp[pos].keys())[0]
            if 'num' in key:
                if '.' not in self.inp[pos][key]:
                    self.inp[pos]['num'] += '.'
            else:
                self.inp.extend([{'num':'0'+'.'}])  
                    
    def _sqrt(self,inp):
        pos = len(self.inp)-1
        if pos == -1:
            self.inp.extend([{'sqrt':inp}])
        else:
            key = self.inp[pos].keys()
            if 'num' in key:
                place_b4 = self.inp[pos-1].keys()
                if 'sqrt' not in place_b4 and 'neg' not in place_b4:
                    self.inp.insert(pos,{'sqrt':inp})
                elif 'neg' in place_b4 and 'sqrt' not in self.inp[pos-2].keys():
                    self.inp.insert(pos-1,{'sqrt':inp})
            elif 'exp' in key and 'sqrt' not in self.inp[pos-2].keys():
                self.inp.insert(pos-1,{'sqrt':inp})
            elif 'oper' in key or 'open_par' in key:
                self.inp.extend([{'sqrt':inp}])
                
    def _oper(self,inp):
        o = self.operators[self.display_operators.index(inp)]
        pos = len(self.inp)-1
        if pos == -1:
            if o == '-':
                self.inp.extend([{'neg':'-'}])
        else:
            key = self.inp[pos].keys()
            if 'num' in key or 'exp' in key or 'close_par' in key:
                self.inp.extend([{'oper':o}])
            elif 'open_par' in key or 'sqrt' in key:
                if o == '-':
                    self.inp.extend([{'neg':'-'}])
                    self.curson += 1
            elif 'neg' in key and 'oper' in self.inp[pos-1].keys():
                self.inp.pop()
                key = self.inp[pos-1].keys()
            if 'oper' in key:
                if o == '-':
                    self.inp.extend([{'neg':'-'}])
                else:
                    self.inp[pos]['oper'] = o
                    
    def _exp(self,inp):
        pos = len(self.inp)-1
        if pos > -1:
            key = self.inp[pos].keys()
            if 'num' in key or 'close_par' in key:
                self.is_exp = True
                if self.superscripts[2] in inp:
                    self._num('2')
                elif self.superscripts[3] in inp:
                    self._num('3')
                
    def _parentheses(self,inp):
        pos = len(self.inp)-1
        if inp == '(':
            if pos == -1:
                self.inp.extend([{'open_par':inp}])
                self.auto_close_par.extend([{'close_par':')'}])
            else:
                key = self.inp[pos].keys()
                if 'oper' in key or 'sqrt' in key:
                    self.inp.extend([{'open_par':inp}])
                    self.auto_close_par.extend([{'close_par':')'}])
        elif inp == ')':
            if len(self.auto_close_par) > 0:
                key = list(self.inp[pos].items())[0][0]
                if key == 'num' or key == 'exp' or key == 'close_par':
                    self.inp.extend([{'close_par':')'}])
                    self.auto_close_par.pop()
                
    def _del(self):
        pos = len(self.inp)-1
        if pos > -1:
            item = list(self.inp[pos].items())[0]
            l = len(item[1])
            if l > 1:
                self.inp[pos][item[0]] = item[1][:l-1] 
            else:
                self.inp.pop(pos)
                if item[0] == 'close_par':
                    self.auto_close_par.extend([{'close_par':')'}])
                elif item[0] == 'open_par':
                    self.auto_close_par.pop()   
                    
    def _cancel(self,error=False):
        self.inp.clear()
        self.auto_close_par.clear()
        self.is_exp = False
        self.is_result = False
        if error == False:
            self._display_update(display_1='')
        else:
            self._display_update(display_1='Error',display_2=self.equation)
        
    def _parse(self):
        end = list(self.inp[len(self.inp)-1].items())[0][0]
        if end == 'oper' or end == 'sqrt':
            self.inp.pop()
        for par in self.auto_close_par:
            self.inp.extend([par])
        self.auto_close_par.clear()
        
    def _get_result(self):
        self.result.clear()
        self._parse()
        equation = Calculator(self.inp)
        self.equation = str(equation)
        result = equation._calculate()
        if result == 'Error':
            self._cancel(error=True)
            self.is_result = False
        else:
            result = round(result,self.n_dec)
            if result - int(result) == 0:
                result = int(result)
            if result < 0:
                self.result.extend([{'neg':'-'}])
                result = -result
            self.result.extend([{'num':str(result)}])
            self._display_update(self.result,self.equation)
            self.inp.clear()
            self.is_exp = False
            self.is_result = True
            
    def callback(self,instance):
        pass
