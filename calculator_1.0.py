class CalculatorBase:

    def __init__(self):
        self.operators = {
                'root': self.root, 'pow': self.pow,
                '*': self.mult, '/': self.div,
                '+': self.add, '-': self.sub,
                }

    def solve(self, l):
        l = self.in_paretheses(l)
        for op in self.operators:
            l = self.operate(l, op)
        answer = l[0]
        if answer - int(answer) == 0:
            answer = int(answer)
        return answer

    def in_paretheses(self, l):
        new_list = []
        for item in l:
            if type(item) is list:
                item = self.solve(item)
            new_list.append(item)
        return new_list

    def operate(self, l, op):
        new_list = []
        for i, item in enumerate(l):
            if item == op:
                a = new_list.pop()
                l.pop(i)
                b = l[i]
                item = self.operators[op](a, b)
            new_list.append(item)
        return new_list

    def pow(self, a, b):
        return a ** b

    def root(self, a, b):
        return b ** (1 / a)

    def mult(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b


class Calculator(CalculatorBase):

    def __init__(self):
        super().__init__()
        self.key_to_string = {
                'root': self.root_to_string,
                'pow' : self.pow_to_string,
                'op'  : self.op_to_string,
                'num' : self.num_to_string,
                'neg' : self.neg_to_string,
                }
        self.new()

    def new(self):
        self.list_dict = {0: []}
        self.nest = {}
        self.current = 0
        self.section = self.list_dict[0]

    def __str__(self):
        return(self.list_to_string(self.list_dict[0]))

    def list_to_string(self, l):
        string = ''
        for item in l:
            if type(item) is list:
                item = '(' + self.list_to_string(item) + ')'
            elif type(item) is dict:
                key = list(item.keys())[0]
                item = self.key_to_string[key](item)
            string += item + ' '
        return string

    def root_to_string(self, d):
        root = d['root']
        if root == 'n':
            root = '2'
        return root + 'root'

    def pow_to_string(self, d):
        _pow = d['pow']
        if _pow == 'n':
            _pow = '2'
        return 'pow' + _pow

    def op_to_string(self, d):
        return d['op']

    def num_to_string(self, d):
        return d['num']

    def neg_to_string(self, d):
        return '-' + d['neg']

    def append_digit(self, n):
        last = len(self.section) -1
        if last == -1:
            self.section.append({'num': n})
        else:
            item = self.section[last]
            if type(self.section[last]) is dict:
                key = list(item.keys())[0]
                if key == 'op' or key == 'root':
                    self.section.append({'num': n})
                elif key == 'num' or key == 'neg':
                    item[key] += n

    def append_negative(self):
        last = len(self.section) -1
        if last == -1:
            self.section.append({'neg': ''})
        else:
            item = self.section[last]
            if type(self.section[last]) is dict:
                key = list(item.keys())[0]
                if key == 'op' or key == 'root':
                    self.section.append({'neg': ''})

    def append_decimal(self):
        last = len(self.section) -1
        if last == -1:
            self.section.append({'num': '0.'})
        else:
            item = self.section[last]
            if type(self.section[last]) is dict:
                key = list(item.keys())[0]
                if key == 'op' or key == 'root':
                    self.section.append({'num': '0.'})
                elif key == 'num' or key == 'neg':
                    item[key] += '.'

    def append_operator(self, o):
        last = len(self.section) -1
        if last == -1 and o == '-':
            self.append_negative()
        if last > -1:
            item = self.section[last]
            if type(item) is list:
                self.section.append({'op': o})
            elif type(item) is dict:
                key = list(item.keys())[0]
                if key == 'num' or key == 'neg' or key == 'pow':
                    self.section.append({'op': o})
                elif o == '-':
                    self.append_negative()

    def append_root(self):
        last = len(self.section) -1
        if last == -1:
            self.section.append({'root': 'n'})
            return True
        else:
            item = self.section[last]
            if type(item) is dict:
                key = list(item.keys())[0]
                if key == 'op':
                    self.section.append({'root': 'n'})
                    return True
                elif key == 'num' or key == 'neg':
                    self.section.insert(last, {'root': 'n'})
                    return True

    def append_pow(self):
        last = len(self.section) -1
        if last > -1:
            item = self.section[last]
            if type(item) is list:
                self.section.append({'pow': 'n'})
                return True
            elif type(item) is dict:
                key = list(item.keys())[0]
                if key == 'num' or key == 'neg':
                    self.section.append({'pow': 'n'})
                    return True

    def set_value_of_n(self, num):
        last = len(self.section) -1
        if last > -1:
            i = 0
            self.num_to_n(last, num, i)

    def num_to_n(self, last, num, i):
        item = self.section[last]
        if type(item) is dict:
            key = list(item.keys())[0]
            if item[key] == 'n':
                item[key] = num
            elif last > 0 and key != 'root' and key != 'pow' and i == 0:
                last -= 1
                i += 1
                self.num_to_n(last, num, i)

    def open_parentheses(self):
        last = len(self.section) -1
        if last == -1:
            self._open_parentheses()
        else:
            item = self.section[last]
            if type(item) is dict:
                key = list(item.keys())[0]
                if key == 'root' or key == 'op':
                    self._open_parentheses()

    def _open_parentheses(self):
        c = self.current
        self.current = len(self.list_dict)
        self.nest.update({self.current: c})
        self.list_dict.update({self.current: []})
        self.section.append(self.list_dict[self.current])
        self.section = self.list_dict[self.current]

    def close_parentheses(self):
        last = len(self.section) -1
        if last > -1 and self.current > 0:
            item = self.section[last]
            if type(item) is dict:
                key = list(item.keys())[0]
                if key == 'num' or key == 'neg' or key == 'pow':
                    self.current = self.nest[self.current]
                    self.section = self.list_dict[self.current]

    def delete_parentheses(self):
        c = self.current
        self.current = self.nest[c]
        self.list_dict[self.current].remove(self.list_dict[c])
        self.list_dict.pop(c)
        self.section = self.list_dict[self.current]

    def back_space_into_list(self, l):
        for item in self.list_dict:
            key = list(item.keys())[0]
            if l == item[key]:
                self.current = key
                self.section = self.list_dict[self.current]

    def delete_from_dict(self, item):
        key = list(item.keys())[0]
        if key == 'op' or key == 'root'  or key == 'pow':
            self.section.pop()
        elif key == 'num' or key == 'neg':
            l = len(item[key])
            if l > 1:
                item[key] = item[key][:l -1]
            else:
                self.section.pop()

    def delete(self):
        last = len(self.section) -1
        if last > -1:
            item = self.section[last]
            if type(item) is list:
                self.back_space_into_list(item)
            if type(item) is dict:
                self.delete_from_dict(item)
        elif self.current > 0:
            self.delete_parentheses()

    def parse_out_dicts(self, l):
        new_list = []
        for i, item in enumerate(l):
            if type(item) is list:
                item = [self.parse_out_dicts(item)]
            elif type(item) is dict:
                key = list(item.keys())[0]
                if key == 'num' or key == 'neg':
                    item = [self.string_to_num(item[key], key)]
                elif key == 'root' or key == 'pow' or key == 'op':
                    item = self.parse_operator(item[key], key)
            new_list.extend(item)
        return new_list

    def string_to_num(self, n, key):
        if n.isdigit():
            n = int(n)
        elif '.' in n:
            n = float(n)
        if key == 'neg':
            n = -n
        return n

    def num_from_val(self, val):
        if val == 'n':
            return 2
        return int(val)

    def parse_operator(self, val, key):
        l = []
        if key == 'root':
            l.extend([self.num_from_val(val), key])
        elif key == 'pow':
            l.extend([key, self.num_from_val(val)])
        elif key == 'op':
            l.append(val)
        return l

    def solve(self):
        e = self.list_dict[0]
        e = self.parse_out_dicts(e)
        self.new()
        return super().solve(e)