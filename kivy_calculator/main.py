# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 13:08:47 2019

@author: jj
"""

from calculator import Calculator
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class CalculatorApp(App):
    def build(self):
        self.inp = ''
        self.n_dec = 8
        self.dec = False
        self.sqrt = False
        self.sqr = False
        self.oper = None
        self.is_result = False
        self.operators = ['×','÷','+','−']
        self.eop = ['*','/','+','-']
        parent = BoxLayout(orientation='vertical')
        self.display_1 = Label(text='0',size_hint_y=1)
        self.display_2 = Label(text='',size_hint_y=0.8)
        button_labels = ['7','8','9','×',
                         '4','5','6','÷',
                         '1','2','3','+',
                         '.','0','del','−',
                         '()²','√','C','=',
                          ]
        button_grid = GridLayout(cols=4,size_hint_y=4.2)
        for label in button_labels:
            button = Button(text=label)
            button.bind(on_press=self.callback)
            button_grid.add_widget(button)
        parent.add_widget(self.display_2)
        parent.add_widget(self.display_1)
        parent.add_widget(button_grid)

        return parent

    def _display_update(self,display_1,display_2=None):
        if display_1 == '':
            display_1 = '0'
        self.display_1.text = display_1
        if display_2 != None:
            self.display_2.text = display_2

    def _cancel(self):
        self.inp = ''
        self.dec = False
        self.sqrt = False
        self.sqr = False
        self.oper = None
        self._display_update(display_1='0',display_2='')

    def _del(self,last,pop):
        if last == '²':
            self.sqr = False
        elif last == '√':
            self.sqrt = False
        elif last in self.operators:
            self.oper = None
        elif last == '.':
            self.dec = False
        self.inp = pop

    def _sqrt(self,inp):
        if self.oper == None:
            self.inp = inp+self.inp
            self.sqrt = True
        else:
            p = self.inp.partition(self.oper)
            self.inp = p[0]+p[1]+inp+p[2]
            self.equ = p[0]+p[1]+inp+p[2]
            self.sqrt = True

    def _num(self,inp,pop):
        if self.sqr == True:
            self.inp = pop
            self.equ = pop
            self.sqr = False
        self.inp += inp

    def _dec(self,inp):
        if self.oper == None:
            if self.sqrt == False and len(self.inp) == 0:
                self.inp += '0'
            elif self.sqrt == True and len(self.inp) == 1:
                self.inp += '0'
        else:
            p = self.inp.partition(self.oper)
            if self.sqrt == False and len(p[2]) == 0:
                self.inp += '0'
            elif self.sqrt == True and len(p[2]) == 1:
                self.inp += '0'
        self.inp += inp
        self.dec = True

    def _sqr(self,inp,last,pop):
        if  last == '.':
            self.dec = False
            self.inp = pop
        elif last in self.operators:
            self.oper = None
            self.inp = pop
        if self.oper == None:
            if self.sqrt == False:
                if len(self.inp) > 0:
                    self.inp += inp
                    self.sqr = True
            else:
                if len(self.inp) > 1:
                    self.inp += inp
                    self.sqr = True
        else:
            p = self.inp.partition(self.oper)
            if self.sqrt == False:
                if len(p[2]) > 0:
                    self.inp += inp
                    self.sqr = True
            else:
                if len(p[2]) > 1:
                    self.inp += inp
                    self.equ += inp
                    self.sqr = True

    def _oper(self,inp,last,pop):
        if last == '.':
            self.inp = pop
        if len(self.inp) != 0:
            self.inp += inp
            self.oper = inp
            self.sqrt = False
            self.dec = False
            self.sqr = False
        else:
            if inp == '−':
                self.inp = inp

    def _parse(self,_string):
        for i,o in enumerate(self.operators):
            if o != '+':
                while True:
                    if o in _string:
                        _string = _string[:_string.index(o)]+self.eop[i]+_string[_string.index(o)+1:]
                    else:
                        break
        return _string

    def _reset_with_error(self):
        self._display_update('Error',self.inp)
        self.inp = ''
        self.dec = False
        self.sqrt = False
        self.sqr = False
        self.oper = None

    def _get_result(self):
        self.equ = self._parse(self.inp)
        result = Calculator(self.equ)._calculate()
        if result == 'Error':
            self._reset_with_error()
        else:
            if result - int(result) == 0:
                result = int(result)
            else:
                result = round(result,self.n_dec)
                self.dec = True
            self.result = str(result)
            self._display_update(self.result,self.inp)
            self.inp = ''
            self.sqrt = False
            self.sqr = False
            self.oper = None
            self.is_result = True

    def callback(self,instance):
        inp = instance.text
        if self.is_result == True:
            self._switch(inp)
        last = self.inp[:len(self.inp)-2:-1]
        pop = self.inp[:len(self.inp)-1:]

        if inp == 'C':
            self._cancel()
        elif inp == '=':
            if last in self.operators or last == '.':
                self.inp = pop
            if last == '√':
                self.inp = pop[:len(pop)-1:]
            self._get_result()
        else:
            if inp.isdigit():
                self._num(inp,pop)
            elif inp == '√' and self.sqrt == False:
                self._sqrt(inp)
            elif inp == '.' and self.dec == False:
                self._dec(inp)
            elif inp == '()²' and self.sqr == False:
                inp = '²'
                self._sqr(inp,last,pop)
            elif inp in self.operators:
                if self.oper != None and last not in self.operators:
                    self._get_result()
                    self._switch(inp)
                self._oper(inp,last,pop)
            elif inp == 'del':
                self._del(last,pop)

            self._display_update(self.inp)

    def _switch(self,inp):
        if not inp.isdigit():
            self.inp = self.result
            self._display_update(self.inp)
        else:
            self._display_update(self.inp,self.result)
        self.is_result = False


if __name__ == '__main__':
    CalculatorApp().run()
