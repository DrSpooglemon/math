# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 22:19:46 2019

@author: jj
"""

import pygame as py
from calculator import Calculator

screen_height = 800
screen_width = round(screen_height*0.8)

bgcolor = (60,60,90)
lncolor = (0,0,0)
clicked_color = (0,255,0)
line_width_1 = round(screen_height/140)
line_width_2 = round(line_width_1*0.6)
font_size_1 = round(screen_height/11.1)
font_size_2 = round(font_size_1*0.65)
size1 = (screen_width,int(screen_height*0.25))
size2 = (int((screen_width-(line_width_2))/4),int(((screen_height-size1[1]-(line_width_2))/5)))

xy = [(0,0),
      (0,size1[1]),
      (0,size1[1]+size2[1]),
      (0,size1[1]+size2[1]*2),
      (0,size1[1]+size2[1]*3),
      (0,size1[1]+size2[1]*4),
      (size2[0],size1[1]),
      (size2[0],size1[1]+size2[1]),
      (size2[0],size1[1]+size2[1]*2),
      (size2[0],size1[1]+size2[1]*3),
      (size2[0],size1[1]+size2[1]*4),
      (size2[0]*2,size1[1]),
      (size2[0]*2,size1[1]+size2[1]),
      (size2[0]*2,size1[1]+size2[1]*2),
      (size2[0]*2,size1[1]+size2[1]*3),
      (size2[0]*2,size1[1]+size2[1]*4),
      (size2[0]*3,size1[1]),
      (size2[0]*3,size1[1]+size2[1]),
      (size2[0]*3,size1[1]+size2[1]*2),
      (size2[0]*3,size1[1]+size2[1]*3),
      (size2[0]*3,size1[1]+size2[1]*4),
      ]

labels = [None,'7','4','1','.','()²','8','5','2','0','√','9','6','3','del','C','×','÷','+','−','=']


box_values = [[(0,0),size1,bgcolor,lncolor,lncolor,0,font_size_1,None]]

for i in range(len(xy[1:])):
    box_values.append([xy[i+1],size2,bgcolor,lncolor,lncolor,
                       line_width_2,font_size_1,labels[i+1]
                       ])

class Box:
    def __init__(self,xy,size,bg_clr,ln_clr,txt_clr,ln_width,font_size,label):
        self.color = bg_clr
        self.line_color = ln_clr
        self.text_color = txt_clr
        self.line_width = ln_width
        self.image = py.Surface(size)
        self.image.fill(self.line_color)
        self.rect = (self.line_width,self.line_width,size[0],size[1])
        py.draw.rect(self.image,self.color,self.rect)
        self.font = py.font.Font('freesansbold.ttf',font_size)
        self.font2 = py.font.Font('freesansbold.ttf',round(font_size_1*0.65))
        if label != None:
            self.label = self.font.render(label,True,self.text_color)
            self.label_rect = self.label.get_rect()
            self.label_rect.center = (int(size[0]/2+self.line_width),
                                      int(size[1]/2+self.line_width))
            self.image.blit(self.label,self.label_rect)
        self.l = xy[0]
        self.t = xy[1]
        self.r = self.l+size[0]
        self.b = self.t+size[1]
        self.is_clicked = False

    def clicked(self,bg_clr):
        self.image.fill(self.line_color)
        py.draw.rect(self.image,bg_clr,self.rect)
        self.image.blit(self.label,self.label_rect)

    def not_clicked(self):
        self.image.fill(self.line_color)
        py.draw.rect(self.image,self.color,self.rect)
        self.image.blit(self.label,self.label_rect)

    def update(self,text1,text2):
        self.image.fill(self.line_color)
        py.draw.rect(self.image,self.color,self.rect)
        self.text1 = self.font.render(text1,True,self.line_color)
        self.text1_rect = self.text1.get_rect()
        self.text1_rect.bottomleft = (int(self.rect[2]*0.05),
                                      int(self.rect[3]*0.9))
        self.image.blit(self.text1,self.text1_rect)

        self.text2 = self.font2.render(text2,True,self.line_color)
        self.text2_rect = self.text2.get_rect()
        self.text2_rect.bottomleft = (int(self.rect[2]*0.05),
                                      int(self.rect[3]*0.45))
        self.image.blit(self.text2,self.text2_rect)

def spawn_boxes():
    n = 0
    boxes = []
    for box in box_values:
        boxes.extend([''])
        xy = box[0]
        s = box[1]
        bc = box[2]
        lc = box[3]
        tc = box[4]
        lw = box[5]
        f = box[6]
        l = box[7]
        boxes[n] = Box(xy,s,bc,lc,tc,lw,f,l)
        screen_surf.blit(boxes[n].image,xy)
        n += 1

    return boxes

#------------------------------------------------------------
py.init()
clock = py.time.Clock()
screen = py.display
screen_surf = screen.set_mode((screen_width,screen_height))
screen_surf.fill((0,0,0))
boxes = spawn_boxes()
display = boxes[0]
screen.update()
fps = 50
#-------------------------------------------------------------

button_clicked = False
button_is_clicked = False
c = 0
cancel = True

while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            quit()
        if event.type == py.MOUSEBUTTONDOWN:
            button_clicked = True
            mouse_pos = py.mouse.get_pos()
        if event.type == py.KEYDOWN:
            shift = False
            if event.key == py.K_ESCAPE:
                py.quit()
                quit()
            if event.key == py.K_RSHIFT or event.key == py.K_LSHIFT:
                shift = True
            if event.key == py.K_PERIOD or event.key == py.K_KP_PERIOD:
                decimal = True
            if event.key == py.K_0 or event.key == py.K_KP0:
                num = '0'
            if event.key == py.K_1 or event.key == py.K_KP1:
                num = '1'
            if event.key == py.K_2 or event.key == py.K_KP2:
                num = '2'
            if event.key == py.K_3 or event.key == py.K_KP3:
                num = '3'
            if event.key == py.K_4 or event.key == py.K_KP4:
                num = '4'
            if event.key == py.K_5 or event.key == py.K_KP5:
                num = '5'
            if event.key == py.K_6 or event.key == py.K_KP6:
                num = '6'
            if event.key == py.K_7 or event.key == py.K_KP7:
                num = '7'
            if event.key == py.K_8:
                if shift == False:
                    num = '8'
                else:
                    oper = '×'
            if event.key == py.K_KP8:
                num = '8'
            if event.key == py.K_9 or event.key == py.K_KP9:
                num = '9'
            if event.key == py.K_ASTERISK or event.key == py.K_KP_MULTIPLY:
                oper = '×'
            if event.key == py.K_SLASH or event.key == py.K_KP_DIVIDE:
                oper = '÷'
            if event.key == py.K_PLUS or event.key == py.K_KP_PLUS:
                oper = '+'
            if event.key == py.K_MINUS or event.key == py.K_KP_MINUS:
                oper = '−'
            if event.key == py.K_EQUALS:
                if shift == False:
                    enter = True
                else:
                    oper = '+'
            if event.key == py.K_KP_EQUALS:
                enter = True
            if event.key == py.K_RETURN or event.key == py.K_KP_ENTER:
                enter = True

        if event.type == py.KEYUP:
            if event.key == py.K_RSHIFT or event.key == py.K_LSHIFT:
                shift = False
    #--------------------------------------------------------
    if button_is_clicked == True:
        if count_down > 0:
            count_down -= 1
        else:
            boxes[c].not_clicked()
            screen_surf.blit(b[c].image,xy[c])
            button_is_clicked = False

    if button_clicked == True:
        x,y = mouse_pos[0],mouse_pos[1]
        b = boxes
        c = 0
        if x > b[1].l and x < b[1].r:
            if y > b[1].t and y < b[1].b:
                num = '7'
                c = 1
            elif y > b[2].t and y < b[2].b:
                num = '4'
                c =2
            elif y > b[3].t and y < b[3].b:
                num = '1'
                c = 3
            elif y > b[4].t and y < b[4].b:
                decimal = True
                c = 4
            elif y > b[5].t and y < b[5].b:
                sqr = True
                c = 5
        elif x > b[6].l and x < b[6].r:
            if y > b[6].t and y < b[6].b:
                num = '8'
                c = 6
            elif y > b[7].t and y < b[7].b:
                num = '5'
                c = 7
            elif y > b[8].t and y < b[8].b:
                num = '2'
                c = 8
            elif y > b[9].t and y < b[9].b:
                num = '0'
                c = 9
            elif y > b[10].t and y < b[10].b:
                root = True
                c = 10
        elif x > b[11].l and x < b[11].r:
            if y > b[11].t and y < b[11].b:
                num = '9'
                c = 11
            elif y > b[12].t and y < b[12].b:
                num = '6'
                c = 12
            elif y > b[13].t and y < b[13].b:
                num = '3'
                c = 13
            elif y > b[14].t and y < b[14].b:
                back_space = True
                c = 14
            elif y > b[15].t and y < b[15].b:
                cancel = True
                c = 15
        elif x > b[16].l and x < b[16].r:
            if y > b[16].t and y < b[16].b:
                oper = '×'
                c = 16
            elif y > b[17].t and y < b[17].b:
                oper = '÷'
                c = 17
            elif y > b[18].t and y < b[18].b:
                oper = '+'
                c = 18
            elif y > b[19].t and y < b[19].b:
                oper = '−'
                c = 19
            elif y > b[20].t and y < b[20].b:
                enter = True
                c = 20
        if c > 0 :
            b[c].clicked(clicked_color)
            screen_surf.blit(b[c].image,xy[c])
            button_is_clicked = True
            count_down = 5
        button_clicked = False
    #------------------------------------------------------
    if cancel == True:
        equation = ''
        text2 = ''
        num = None
        root = False
        sqr = False
        oper = None
        decimal = False
        back_space = False
        enter = False
        result = False
        error = False
        cancel = False

    if num != None:
        if result == True:
            equation = ''
            text2 = ''
            error = False
            result = False
        l = len(equation)
        if l > 1:
            t = equation[l-1:]
            if t !=  '²':
                equation += num
        elif equation == '' or equation == '0':
            equation = num
        else:
            equation += num
        num = None

    if decimal == True:
        l = len(equation)
        t = equation[l-1:]
        if t == '×' or t == '÷' or t == '+' or t == '−' or t == '√':
            equation += '0'
            equation += '.'
        elif '×' in equation or '÷' in equation or '+' in equation or '−' in equation:
            if equation.count('.') < 2:
                equation += '.'
        elif equation.count('.') == 0:
            if error == True or equation == '':
                equation = '0'
                if error == True:
                    text2 = ''
                    error = False
            equation += '.'
            result = False
        decimal = False

    if root == True:
        if result == True:
            if error == True:
                equation = '√'
                text2 = ''
                error = False
            else:
                equation = '√'+equation
            result = False
        l = len(equation)
        t = equation[l-1:]
        if l == 0 or t == '×' or t == '÷' or t == '+' or t == '−':
            equation += '√'
        root = False

    if sqr == True:
        l = len(equation)
        if l > 0 and error == False:
            t = equation[l-1:]
            if t != '×' and t != '÷' and t != '+' and t != '−' and t != '√' and t != '²':
                if t == '.':
                    equation = equation[:l-1]
                result = False
                equation += '²'
        sqr = False

    if oper != None:
        result = False
        l = len(equation)
        if l == 0:
            equation = '0'
            l = len(equation)
        t = equation[l-1:]
        if t == '.':
            equation = equation[:l-1]
            l = len(equation)
            t = equation[l-1:]
        if '×' in equation or '÷' in equation or '+' in equation or '−' in equation:
            if t == '×' or t == '÷' or t == '+' or t == '−' :
                equation = equation[:l-1]
                if t == '√':
                    l = len(equation)
                    equation = equation[:l-1]
                equation += oper

            else:
                equation += oper
                enter = True
        elif t.isdigit() == True or t == '²':
            equation += oper
        oper = None

    if back_space == True:
        result = False
        equation = equation[:len(equation)-1]
        back_space = False

    if enter == True:
        l = len(equation)
        t = equation[l-1:]
        if t == '×' or t == '÷' or t == '+' or t == '−':
            print(equation)
            equation = equation[:l-1]
            if '×' in equation or '÷' in equation or '+' in equation or '−' in equation:
                oper = t
        elif t == '.':
            equation = equation[:l-1]
        equation = Calculator(equation)
        text2 = equation.__str__()
        equation = equation.calculate()
        if type(equation) is str:
            error = True
            equation = 'Fart'
        else:
            if type(equation) is float and equation - int(equation) == 0:
                equation = int(equation)
            equation = round(equation,8)
            equation = str(equation)
        result = True
        enter = False

    if len(equation) > 0:
        text1 = equation
    else:
        text1 = '0'
    if error == True:
        display.color = (60,30,0)
    else:
        display.color = bgcolor
    display.update(text1,text2)
    screen_surf.blit(display.image,(0,0))
    py.draw.line(screen_surf,lncolor,(0,size1[1]),(size1[0],size1[1]),line_width_1)
    screen.update()

    clock.tick(fps)


