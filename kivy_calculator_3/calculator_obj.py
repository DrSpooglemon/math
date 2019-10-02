from math import sqrt

class Calculator:
    def __init__(self,_list):
        self.equation = _list
        self.operators = ['*','/','+','-']
        self.imaginary_numbers = []

    def __str__(self):
        _string = ''
        exp = ['⁰','¹','²','³','⁴','⁵','⁶','⁷','⁸','⁹']
        for item in self.equation:
            item = list(item.items())[0]
            if item[0] == 'exp':
                for i in range(len(item[1])):
                    _string += exp[int(item[1][i:i+1])]
            else:
                _string += item[1]
        return _string

    def _calculate(self):
        _list = self.equation
        while True:
            list_a,list_b,list_c = self._in_parentheses(_list)
            _list = self._get_floats(list_b)
            _list = self._sqrt(_list)
            if _list == 'Error':
                return 'Error'
            _list = self._pow(_list)
            _list = self._oper(_list)
            if _list == 'Error':
                return 'Error'
            _list = list_a+_list+list_c
            if len(_list) == 1:
                return _list[0]

    def _in_parentheses(self,_list):
        list_a,list_c = [],[]
        for i,item in enumerate(_list):
            if type(item) == dict:
                key = list(item.items())[0][0]
                if key == 'close_par':
                    list_c = _list[i+1:]
                    _list = _list[:i]
                    _list = _list[::-1]
                    for i,item in enumerate(_list):
                        if type(item) is dict:
                            key = list(item.items())[0][0]
                            if key == 'open_par':
                                list_a.extend(_list[i+1:])
                                list_a = list_a[::-1]
                                _list = _list[:i]
                                _list = _list[::-1]
                                return list_a,_list,list_c
        return list_a,_list,list_c
    
    def _get_floats(self,_list):
        while True:
            neg = None
            for i,item in enumerate(_list):
                if type(item) == dict:
                    item = list(item.items())[0]
                    if item[0] == 'neg':
                        neg = True
                    elif item[0] == 'num':
                        n = float(item[1])
                        if neg == True:
                            _list[i] = -n
                            _list.pop(i-1)
                            break
                        else:
                            _list[i] = n
            if neg != True:
                break
        return _list

    def _sqrt(self,_list):
        while True:
            root = None
            for i,item in enumerate(_list):
                if type(item) == dict:
                    item = list(item.items())[0]
                    if item[0] == 'sqrt':
                        try:
                            _list[i] = sqrt(_list[i+1])
                        except:
                            return 'Error'
                        _list.pop(i+1)
                        root = True
                        break
            if root != True:
                break
        return _list
               
    def _pow(self,_list):
        while True:
            exp = None
            for i,item in enumerate(_list):
                if type(item) == dict:
                    item = list(item.items())[0]
                    if item[0] == 'exp':
                        e = float(item[1])
                        n = _list[i-1]**e
                        _list[i-1] = n
                        _list.pop(i)
                        exp = True
                        break
            if exp != True:
                break
        return _list
                    
    def _oper(self,_list):
        for o in self.operators:
            while True:
                is_o = None
                for i,item in enumerate(_list):
                    if type(item) == dict:
                        val = list(item.items())[0][1]
                        if val == o:
                            n1 = _list[i-1]
                            n2 = _list[i+1]
                            if o == '*':
                                a = n1*n2
                            elif o == '/':
                                a = n1/n2
                            elif o == '+':
                                a = n1+n2
                            else:
                                a = n1-n2
                            _list[i-1] = a
                            _list.pop(i)
                            _list.pop(i)
                            is_o = True
                            break
                if is_o != True:
                    break
        return _list
