import pygame as py
from math import sqrt


screen_height = 800
screen_width = round(screen_height*0.8)

bgcolor = (60,60,90)
lncolor = (0,0,0)

#------lines---------------------------------
line_coords = []
line_widths = []

lw1 = round(screen_height/140)
lw2 = round(lw1*0.6)

ly1 = round(screen_height*0.25)
r = screen_height-ly1+lw1*0.5
f = r/5
ly2 = round(ly1+f)
ly3 = round(ly2+f)
ly4 = round(ly3+f)
ly5 = round(ly4+f)
lx1 = round(screen_width*0.25)
lx2 = lx1*2
lx3 = lx1*3

line_coords.append([(0,ly1),(screen_width,ly1)])
line_coords.append([(0,ly2),(screen_width,ly2)])
line_coords.append([(0,ly3),(screen_width,ly3)])
line_coords.append([(0,ly4),(screen_width,ly4)])
line_coords.append([(0,ly5),(screen_width,ly5)])
line_coords.append([(lx1,ly1),(lx1,screen_height)])
line_coords.append([(lx2,ly1),(lx2,screen_height)])
line_coords.append([(lx3,ly1),(lx3,screen_height)])

line_widths.extend([lw1])
for i in range(len(line_coords)-1):
    line_widths.extend([lw2])
#----------------------------------------------

#------boxes--------------------------------
bx1 = round(lx1*0.2)
by1 = round(ly1-ly1*0.1)
by2 = round((ly1*0.5)-ly1*0.1)

display_box1 = (bx1,by1)
display_box2 = (bx1,by2)

display_rect = (0,0,screen_width,ly1)
font2 = round(screen_height/20)
font1 = round(font2*1.8)

#----------------
keypad_boxes = []

kx1 = round(lx1/2)
kx2 = kx1 + lx1
kx3 = kx2 + lx1
kx4 = kx3 + lx1
ly_diff = round((ly2-ly1)/2)
ky1 = ly1 + ly_diff
ky2 = ly2 + ly_diff
ky3 = ly3 + ly_diff
ky4 = ly4 + ly_diff
ky5 = ly5 + ly_diff

keypad_boxes.extend([(kx1,ky1)])
keypad_boxes.extend([(kx2,ky1)])
keypad_boxes.extend([(kx3,ky1)])
keypad_boxes.extend([(kx4,ky1)])
keypad_boxes.extend([(kx1,ky2)])
keypad_boxes.extend([(kx2,ky2)])
keypad_boxes.extend([(kx3,ky2)])
keypad_boxes.extend([(kx4,ky2)])
keypad_boxes.extend([(kx1,ky3)])
keypad_boxes.extend([(kx2,ky3)])
keypad_boxes.extend([(kx3,ky3)])
keypad_boxes.extend([(kx4,ky3)])
keypad_boxes.extend([(kx1,ky4)])
keypad_boxes.extend([(kx2,ky4)])
keypad_boxes.extend([(kx3,ky4)])
keypad_boxes.extend([(kx4,ky4)])
keypad_boxes.extend([(kx1,ky5)])
keypad_boxes.extend([(kx2,ky5)])
keypad_boxes.extend([(kx3,ky5)])
keypad_boxes.extend([(kx4,ky5)])

box_labels = ['7','8','9','×','4','5','6','÷','1','2','3','+','.','0','del','−','()²','√','C','=']


#---------------------------------------------

def draw_lines(surf,color,c,w):
    for i in range(len(c)):
        py.draw.line(surf,color,c[i][0],c[i][1],w[i])

def text_objects(text,font):
    text_surf = font.render(text, True, (0,0,0))

    return text_surf, text_surf.get_rect()

def fill_keypad_boxes(font,boxes,labels):
    for i in range(len(boxes)):
        text_font = py.font.Font('freesansbold.ttf',font)
        text_surf, text_rect = text_objects(labels[i], text_font)
        text_rect.center = boxes[i]
        screen_surf.blit(text_surf, text_rect)


def update_display(text_1,text_2,font1,font2,xy1,xy2):
    py.draw.rect(screen_surf,bgcolor,display_rect)
    py.draw.line(screen_surf,lncolor,(0,ly1),(screen_width,ly1),lw1)
    text_font = py.font.Font('freesansbold.ttf',font1)
    text_surf, text_rect = text_objects(text1, text_font)
    text_rect.bottomleft = xy1
    screen_surf.blit(text_surf, text_rect)
    text_font = py.font.Font('freesansbold.ttf',font2)
    text_surf, text_rect = text_objects(text2, text_font)
    text_rect.bottomleft = xy2
    screen_surf.blit(text_surf, text_rect)
    screen.update()


#------------------------------------

#-----initiate pygame--------------
py.init()

screen = py.display
screen_surf = screen.set_mode((screen_width,screen_height))

screen_surf.fill(bgcolor)
draw_lines(screen_surf,lncolor,line_coords,line_widths)
fill_keypad_boxes(font1,keypad_boxes,box_labels)
screen.update()

clock = py.time.Clock()

fps = 50
#---------------------------------------

button_clicked = False
mouse_pos = None
text1 = '0'
text2 = ''
point1 = ''
point2 = ''
enter = False
shift = False
N1 = 0
N2 = ''
decimal = 0
is_decimal = False
point = False
num = None
func = None
is_func = False
do_func = None
result = False
square = False
root = False
back_space = False
cancel = False

#----main loop----------------------
while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            quit()
        if event.type == py.MOUSEBUTTONDOWN:
            button_clicked = True
            mouse_pos = py.mouse.get_pos()
        if event.type == py.KEYDOWN:
            if event.key == py.K_ESCAPE:
                py.quit()
                quit()
            if event.key == py.K_RSHIFT or event.key == py.K_LSHIFT:
                shift = True
            if event.key == py.K_PERIOD or event.key == py.K_KP_PERIOD:
                if is_decimal == False:
                    is_decimal = True
                    point = True
                    result = False
            if event.key == py.K_0 or event.key == py.K_KP0:
                num = 0
            if event.key == py.K_1 or event.key == py.K_KP1:
                num = 1
            if event.key == py.K_2 or event.key == py.K_KP2:
                num = 2
            if event.key == py.K_3 or event.key == py.K_KP3:
                num = 3
            if event.key == py.K_4 or event.key == py.K_KP4:
                num = 4
            if event.key == py.K_5 or event.key == py.K_KP5:
                num = 5
            if event.key == py.K_6 or event.key == py.K_KP6:
                num = 6
            if event.key == py.K_7 or event.key == py.K_KP7:
                num = 7
            if event.key == py.K_8:
                if shift == False:
                    num = 8
                else:
                    func = '×'
            if event.key == py.K_KP8:
                num = 8
            if event.key == py.K_9 or event.key == py.K_KP9:
                num = 9
            if event.key == py.K_ASTERISK or event.key == py.K_KP_MULTIPLY:
                func = '×'
            if event.key == py.K_SLASH or event.key == py.K_KP_DIVIDE:
                func = '÷'
            if event.key == py.K_PLUS or event.key == py.K_KP_PLUS:
                func = '+'
            if event.key == py.K_MINUS or event.key == py.K_KP_MINUS:
                func = '−'
            if event.key == py.K_EQUALS:
                if shift == False:
                    func = '='
                    equals = True
                else:
                    func = '+'
            if event.key == py.K_KP_EQUALS:
                enter = True
            if event.key == py.K_RETURN or event.key == py.K_KP_ENTER:
                enter = True

        if event.type == py.KEYUP:
            if event.key == py.K_RSHIFT or event.key == py.K_LSHIFT:
                shift = False

    if button_clicked == True:
        x,y = mouse_pos[0],mouse_pos[1]
        if x > 0 and x < lx1:
            if y > ly1 and y < ly2:
                num = 7
            elif y > ly2 and y < ly3:
                num = 4
            elif y > ly3 and y < ly4:
                num = 1
            elif y > ly4 and y < ly5:
                if is_decimal == False:
                    is_decimal = True
                    point = True
                    result = False
            elif y > ly5 and y < screen_height:
                square = True
        elif x > lx1 and x < lx2:
            if y > ly1 and y < ly2:
                num = 8
            elif y > ly2 and y < ly3:
                num = 5
            elif y > ly3 and y < ly4:
                num = 2
            elif y > ly4 and y < ly5:
                num = 0
            elif y > ly5 and y < screen_height:
                root = True
        elif x > lx2 and x < lx3:
            if y > ly1 and y < ly2:
                num = 9
            elif y > ly2 and y < ly3:
                num = 6
            elif y > ly3 and y < ly4:
                num = 3
            elif y > ly4 and y < ly5:
                back_space = True
            elif y > ly5 and y < screen_height:
                cancel = True
        elif x > lx3 and x < screen_width:
            if y > ly1 and y < ly2:
                func = '×'
            elif y > ly2 and y < ly3:
                func = '÷'
            elif y > ly3 and y < ly4:
                func = '+'
            elif y > ly4 and y < ly5:
                func = '−'
            elif y > ly5 and y < screen_height:
                enter = True
        button_clicked = False
    #----------------------------------
    #--------------------------------------
    if text1 == 'Fart':
        bgcolor = 100,50,0
    elif text2 == 'Fart':
        bgcolor = 80,55,45
    else:
        bgcolor = 60,60,90

    #------input to dsplay----------------
    #-----------------------------
    if is_decimal == True:
        if is_func == True:
            if type(N2) is str:
                N2 = 0
                text1 += str(N2)
    if point == True:
        if type(N1) is str:
            N1 = 0
            text1 = str(N1)
        if result == True:
            result = False
        text1 += '.'
        point = False
    #----------------------------
    if square == True:
        if type(N2) is str:
            if type(N1) is str:
                text2 = text1
            else:
                text2 = str(N1)+'²'+' ='
                N1 = round((N1**2),8)
                text1 = str(N1)
                decimal = text1[::-1].find('.')
                if decimal < 1:
                    decimal = 0
                    is_decimal = False
                else:
                    is_decimal = True
            result = True
        square = False
    #-------------------------
    if root == True:
        if type(N2) is str:
            if type(N1) is str:
                text2 = text1
            else:
                text2 = '√'+str(N1)+' ='
                N1 = round((sqrt(N1)),8)
                if N1 - int(N1) == 0:
                    N1 = int(N1)
                text1 = str(N1)
                decimal = text1[::-1].find('.')
                if decimal < 1:
                    decimal = 0
                    is_decimal = False
                else:
                    is_decimal = True
            result = True
        root = False
    #--------------------------
    if back_space == True:
        if type(N1) is str:
            N1 = 0
            text1 = str(N1)
            text2 = 'Fart'
        else:
            if type(N2) is str:
                if do_func != None:
                    do_func = None
                    is_func = False
                else:
                    if decimal == 0:
                        N1 = int(N1/10)
                    else:
                        N1 = int(N1*(10**(decimal-1)))
                        N1 = round((N1*(10**(-decimal+1))),8)
                        decimal -= 1
                        if decimal == 0:
                            is_decimal = False
                text1 = str(N1)
            else:
                if decimal == 0:
                    if N2 == 0:
                        N2 = ''
                    else:
                        N2 = int(N2/10)
                        print(N2)
                else:
                    if decimal == 1 and N2 - int(N2) == 0:
                        N2 = int(N2)
                    else:
                        N2 = int(N2*(10**(decimal-1)))
                        N2 = round((N2*(10**(-decimal+1))),8)
                        decimal -= 1
                        if decimal == 0:
                            is_decimal = False
                text1 = str(N1)+do_func
                if N2 == 0:
                    N2 = ''
                if type(N2) is not str:
                    text1 += str(N2)
        back_space = False
    #--------------------------------
    if cancel == True:
        is_decimal = False
        decimal = 0
        func = None
        do_func = None
        is_func = False
        N1 = 0
        N2 = ''
        text1 = '0'
        text2 = ''
        cancel = False
    #------------------------------
    if num != None:
        if do_func == None:
            if result == False:
                if is_decimal == True:
                    N1 += num*(10**(-decimal-1))
                    decimal += 1
                else:
                    N1 *= 10
                    N1 += num
            else:
                is_decimal = False
                decimal = 0
                text2 = text1
                N1 = num

                result = False

            N1 = round(N1,decimal)
        else:
            if type(N2) is str:
                N2 = num
                decimal = 0
                is_decimal = False
            else:
                if is_decimal == True:
                    N2 += num*(10**(-decimal-1))
                    decimal += 1
                else:
                    N2 *= 10
                    N2 += num

            N2 = round(N2,decimal)
        text1 = str(N1)
        if type(N2) is not str:
            text1 += do_func
            text1 += str(N2)
        num = None
    #------------------------------------
    if func != None:
        if type(N1) is str:
            text2 = text1
            N1 = 0
            text1 = str(N1)
        if is_decimal == True:
            is_decimal = False
            decimal = 0
        if is_func == False:
            text1 = str(N1)+func
            is_func = True
            do_func = func
            func = None
        else:
            if type(N2) is str:
                text1 = str(N1)+func
            else:
                text2 = text1+' ='
                if do_func == '×':
                    N1 *= N2
                elif do_func == '÷':
                    N1 /= N2
                elif do_func == '+':
                    N1 += N2
                elif do_func == '−':
                    N1 -= N2
                result = True
                do_func = func
                N2 = ''
                text1 = str(N1)+func
                func = None
    #------------------------------
    if enter == True:
        if type(N2) is not str:
            text2 = str(N1)+do_func+str(N2)+' ='
            if do_func == '×':
                N1 *= N2
            elif do_func == '÷':
                if N2 == 0:
                    N1 = 'Fart'
                else:
                    N1 /= N2
            elif do_func == '+':
                N1 += N2
            elif do_func == '−':
                N1 -= N2
            N2 = ''
        else:
            text2 = str(N1)+' ='
        if N1 == 'Fart':
            text1 = N1
            decimal = 0
            is_decimal = False
        else:

            if N1 - int(N1) == 0:
                N1 = int(N1)
            N1 = round(N1,8)
            text1 = str(N1)
            decimal = text1[::-1].find('.')
            if decimal < 1:
                decimal = 0
                is_decimal = False
            else:
                is_decimal = True
        is_func = False
        do_func = None
        func = None
        result = True
        enter = False
    #-----------------------------

    xy1 = display_box1
    xy2 = display_box2
    if len(text1) > 500:
        N1 = 'Fart'
        N2 = ''
        do_func = None
        is_func = False
        is_decimal = False
        decimal = 0
        text1 = N1
    update_display(text1,text2,font1,font2,xy1,xy2)

    clock.tick(fps)
