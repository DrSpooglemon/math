from math import sqrt

class Calculator:
    def __init__(self,_string):
        self.equation = _string
        self.operators = ['*','/','+','-']
        self.powers = ['⁰','¹','²','³','⁴','⁵','⁶','⁷','⁸','⁹']
        self.imaginary_numbers = []
        self.are_parentheses = None
        self.are_operators = None
        self.are_square_roots = None

    def __str__(self):
        return self.equation

    def _calculate(self):
        _string = self.equation
        while True:
            string_a,string_b,string_c = self._in_parentheses(_string)
            if string_b == _string:
                self.are_parentheses = False
            _list = self._parse_operators(string_b)
            _list = self._get_negatives(_list)
            _list = self._sqrt(_list)
            if _list == 'Error':
                return 'Error'
            for item in _list:
                if '|' in item:
                    return 'Error'
            _list = self._pow(_list)
            for o in self.operators:
                _list = self._oper(_list,o)
                if _list == 'Error':
                    return 'Error'
            answer = _list[0]
            if self.are_parentheses == False and len(_list) == 1:
                self.are_operators = False
            if self.are_operators == False and self.are_square_roots != True:
                return float(answer)
            _string = string_a+answer+string_c

    def _oper(self,_list,o):
        new_list = []
        while True:
            new_list.clear()
            if o in _list:
                i = _list.index(o)
                N1 = float(_list[i-1])
                N2 = float(_list[i+1])
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
                new_list.extend([str(Nr)])
                try:
                    new_list.extend(_list[i+1:])
                except:
                    pass
                _list.clear()
                _list.extend(new_list)
            else:
                return _list

    def _get_negatives(self,_list):
        new_list = []
        index_list = []
        for i,item in enumerate(_list):
            if item == '√' and _list[i+1] == '-':
                index_list.extend([i+1])
        for i in index_list:
            n = -float(_list[i+1])
            new_list.extend(_list[:i])
            new_list.extend([str(n)])
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
                new_list.extend([str(-float(_list[i+2]))])
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

                        is_in_item = True
                if is_in_item == True:
                    continue
                else:
                    break
        return _list

    def _sqrt(self,_list):
        new_list = []
        while True:
            self.sqare_roots = None
            new_list.clear()
            for i,item in enumerate(_list):
                if '√' in item:
                    self.square_roots = True
                    if len(item)>1:
                        n = item.partition('√')[2]
                        for p in self.powers:
                            if p in n:
                                n = n.partition(p)[0]
                                break
                            else:
                                p = None
                        try:
                            new_list.extend(_list[:i])
                        except:
                            pass
                        try:
                            r = str(sqrt(float(n)))
                            if p != None:
                                r += p
                            new_list.extend([r])
                        except:
                            return 'Error'
                        try:
                            new_list.extend(_list[i+1:])
                        except:
                            pass
                    if len(new_list) > 0:
                        _list.clear()
                        _list = new_list
                        break
                
            return _list

    def _pow(self,_list):
        for i,item in enumerate(_list):
            for j,p in enumerate(self.powers):
                if p in item:
                    n = item.partition(p)[0]
                    _list.remove(item)
                    _list.insert(i,str(float(n)**j))
        return _list
