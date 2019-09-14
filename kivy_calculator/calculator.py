# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 22:19:46 2019

@author: jj
"""
from math import sqrt

class Calculator:
    def __init__(self,_string):
        self.equation = _string
        self.operators = ['*','/','+','-']
        self.imaginary_numbers = []

    def _calculate(self):
        _string = self.equation
        no_more_parentheses = None
        no_more_operators = None
        while True:
            string_a,string_b,string_c = self._in_parentheses(_string)
            if string_b == _string:
                no_more_parentheses = True
            _list = self._parse_operators(string_b)
            _list = self._sqrt(_list)
            if _list == 'Error':
                return 'Error'
            for item in _list:
                if '|' in item:
                    return 'Error'
            _list = self._sqr(_list)
            _list = self._strings_to_floats(_list)
            _list = self._get_negatives(_list)
            for o in self.operators:
                _list = self._oper(_list,o)
                if _list == 'Error':
                    return 'Error'
            answer = _list[0]
            if answer - int(answer) == 0:
                answer = int(answer)
            if no_more_parentheses == True and len(_list) == 1:
                no_more_operators = True
            if no_more_parentheses == True and no_more_operators == True:
                return answer
            _string = string_a+str(answer)+string_c

    def _oper(self,_list,o):
        new_list = []
        while True:
            new_list.clear()
            if o in _list:
                i = _list.index(o)
                N1 = _list[i-1]
                N2 = _list[i+1]
                if o == '*':
                    Nr = N1*N2
                elif o == '/':
                    if N2 == 0:
                        return 'Error'
                    else:
                        Nr = N1/N2
                elif o == '+':
                    Nr = N1+N2
                else:
                    Nr = N1-N2
                new_list.extend(_list[:i-1])
                new_list.extend([Nr])
                try:
                    new_list.extend(_list[i+2:])
                except:
                    pass
                _list.clear()
                _list.extend(new_list)
            else:
                return _list

    def _strings_to_floats(self,_list):
        for i,item in enumerate(_list):
            try:
                f = float(item)
                _list.remove(item)
                _list.insert(i,f)
            except:
                pass
        return _list

    def _get_negatives(self,_list):
        new_list = []
        index_list = []
        for i,item in enumerate(_list):
            if item == '√' and _list[i+1] == '-':
                index_list.extend([i+1])
        for i in index_list:
            n = -_list[i+1]
            new_list.extend(_list[:i])
            new_list.extend([n])
            try:
                new_list.extend(_list[i+2:])
            except:
                pass
            _list.clear()
            _list.extend(new_list)
        while True:
            new_list.clear()
            if '' in _list:
                i = _list.index('')
                try:
                    new_list.extend(_list[:i])
                except:
                    pass
                new_list.extend([-_list[i+2]])
                try:
                    new_list.extend(_list[i+3:])
                except:
                    pass
                _list.clear()
                _list.extend(new_list)

            else:
                return _list

    def _in_parentheses(self,_string):
        if '(' in _string:
            c = _string.find(')')
            o = _string[:c].rfind('(')
            return _string[:o],_string[o+1:c],_string[c+1:]
        else:
            return '',_string,''

    def _parse_operators(self,_string):
        _list = [_string]
        for o in self.operators:
            while True:
                is_in_item = None
                for i,item in enumerate(_list):
                    if len(item) > 1 and o in item:
                        p = item.partition(o)
                        _list.remove(item)
                        _list.insert(i,p[0])
                        _list.insert(i+1,p[1])
                        _list.insert(i+2,p[2])

                    is_in_string = True
                if is_in_item == True:
                    continue
                else:
                    break
        return _list

    def _sqrt(self,_list):
        new_list = []
        while True:
            is_in_list = None
            new_list.clear()
            for i,item in enumerate(_list):
                if item == '√':
                    try:
                        new_list.extend(_list[:i])
                    except:
                        pass
                    try:
                        new_list.extend([str(sqrt(float(_list[i+1])))])
                    except:
                        return 'Error'
                    try:
                        new_list.extend(_list[i+2:])
                    except:
                        pass
                elif type(item) is str and '√' in item:
                    try:
                        new_list.extend(_list[:i])
                    except:
                        pass
                    new_list.extend([str(sqrt(float(item[1:])))])
                    try:
                        new_list.extend(_list[i+1:])
                    except:
                        pass
                if len(new_list) > 0:
                    _list.clear()
                    _list.extend(new_list)
                    break
            return _list

    def _sqr(self,_list):
        for i,item in enumerate(_list):
            if '²' in item:
                n = item.partition('²')[0]
                _list.remove(item)
                _list.insert(i,str(float(n)**2))
        return _list
