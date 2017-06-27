from graphics import *
import math
sz=650
win = GraphWin(width=sz, height=sz)
##Put whatever you want to encode in the string
string="500 at the beginning, 500 at the end, 5 in the middle is seen, The first of all letters, the first of all figures Take up their stations between, String them all together, and you will see The name of an ancient king"

##This is not annotated yet, but most of it is pretty self-explanitory

def drawLine(p1,p2):
    line = Line(p1,p2)
    return line.draw(win)

def pt(x,y):
    point = Point(x,y)
    return point

def drawCircle(c,r):
    cir = Circle(c,r)
    return cir.draw(win)

def shift(x,y):
    center = sz/2
    newx = center+x
    newy = center+y
    return pt(newx,newy)

def pol2cart(r,a):
    y=r*math.sin(a-math.pi/2)
    x=r*math.cos(a-math.pi/2)
    return shift(x,y)

def prepCode(l):
    a=0
    pi=math.pi
    plotList=[]
    n=len(l)
    b=float(2*pi/n)
    for j in range(len(l)):
        for i in range(len(l[j])):
            if i==0 or i==1:
                r=130-(24*l[j][i]*math.pow(-1,i))
            elif i==2 or i==3:
                r=250-(24*l[j][i]*math.pow(-1,i))
            plotList.append(pol2cart(r,a))
        a+=b
    return plotList

def drawCode(plist):
    for i in range(len(plist)):
        if (i%2)==0:
            drawLine(plist[i],plist[i+1])
        pt=Circle(plist[i],5)
        pt.draw(win)
        pt.setFill('black')
    return True

def dec2tri(num, concat=1): #The graph will not draw properly unless concat is set to zero
    cub=0
    squ=0
    lin=0
    con=0
    valid=True
    while num>0:
        if num>=27:
            cub=int(num/27)
            num=num%27
            if cub>2:
                valid=False
        elif num>=9:
            squ=int(num/9)
            num=num%9
        elif num>=3:
            lin=int(num/3)
            num=num%3
        else:
            con=num
            num=0
    if valid==False:
        return "ERROR"
    elif concat==0:
        return [cub,squ,lin,con]
    else:
        return 1000*cub+100*squ+10*lin+con
    
def char2int(char):
    char=char.upper()
    num=ord(char)-64
    if num<0:
        num+=64
    if char=='{' or char=='}' or char=='|' or char=='~':
        num+=5
    elif char=='@':
        num=68
    return num

def CALLTHIS(codeList):
    drawCircle(pt(sz/2,sz/2),130)
    drawCircle(pt(sz/2,sz/2),250)
    return drawCode(prepCode(codeList))

alph=[' ',',','.','1','2','3','+','=','-','a','z']
chars=[]
codeList=[]
##string="abcdefghijklmnopqrstuvwxyz"
string="caleb goerzen"
slist=list(string)
for c in slist:
    codeList.append(dec2tri(char2int(c),0))


CALLTHIS(codeList)
print(codeList)

