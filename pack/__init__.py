# ;)
# ! {<J>}
# ! author: Julio C. Moreira
# ! made between 02/26/2022 to 02/27/2022

# * LIBS {
from random import randint
# * }

# * FUNCTIONS {
def colors(color='',bold=0):
    """function to put colors in sentences

    color: color parameter w:white r:red g:green y:yellow
    b:blue p:purple c:cyan '' or "": random

    bold: parameter to control bold 0:normal 1:bold
    """
    try:
        if color == '' or color == "":
            color_op = ['r','w','g','y','b','p','c']
            color_randint = randint(0,7)
            color_random = color_op[color_randint] # random 
            bol = bold
            return colors(color=color_random,bold=bol) # return the color randomized
    except:
        colors(color=color,bold=bold) # if the randomization is greater than the list resets

    col = {'white': ['\033[30m','\033[1;30m'] , 'red': ['\033[31m','\033[1;31m'] ,
                'green': ['\033[32m','\033[1;32m'] , 'yellow': ['\033[33m','\033[1;33m'] , 
                'blue': ['\033[34m','\033[1;34m'] , 'purple': ['\033[35m','\033[1;35m'],
                'cyan': ['\033[36m','\033[1;36m']}
    
    if bold == 0:
        if color == 'w':
            return col['white'][0]
        elif color == 'r':
            return col['red'][0]
        elif color == 'g':
            return col['green'][0]
        elif color == 'y':
            return col['yellow'][0]
        elif color == 'b':
            return col['blue'][0]
        elif color == 'p':
            return col['purple'][0]
        elif color == 'c':
            return col['cyan'][0]
    if bold == 1:
        if color == 'w':
            return col['white'][1]
        elif color == 'r':
            return col['red'][1]
        elif color == 'g':
            return col['green'][1]
        elif color == 'y':
            return col['yellow'][1]
        elif color == 'b':
            return col['blue'][1]
        elif color == 'p':
            return col['purple'][1]
        elif color == 'c':
            return col['cyan'][1]


def hed(txt='TEXT',sty='a',colorr="",boldd=0):
    """function to make beautiful headers
    
    txt: text to use in header
    sty: style text a: random

    colorr: color parameter w:white r:red g:green y:yellow
    b:blue p:purple c:cyan '' or "": random

    bold: parameter to control bold 0:normal 1:bold
    """
    try:
        if sty == 'a':
            styl = ['/','~','=','-','*','.','`',"'",'"']
            sla = randint(0,8)
            len_txt = len(txt)+4
            shuf = str(styl[sla]) # random
            print(colors(color=colorr,bold=boldd),shuf*len_txt,'\n',f'  {txt}','\n',shuf*len_txt)
        else:
            len_txt = len(txt)+4
            print(colors(color=colorr,bold=boldd),sty*len_txt,'\n',f'  {txt}','\n',sty*len_txt)
    except:
        hed(txt=txt,sty=sty,colorr=colorr,boldd=boldd) # if the randomization is greater than the list resets
# * }
