import pyautogui as pyt
import d3dshot as ss
from PIL import Image
import math
import keyboard
pyt.PAUSE = 0
pyt.FAILSAFE = True
d = ss.create(capture_output="numpy")


def colorMouse():
    x, y = pyt.position()
    positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
    pixelColor = pyt.screenshot().getpixel((x, y))
    positionStr += ' RGB: (' + str(pixelColor[0]).rjust(3)
    positionStr += ', ' + str(pixelColor[1]).rjust(3)
    positionStr += ', ' + str(pixelColor[2]).rjust(3) + ')'
    print(positionStr)

# color = [82,85,79]
# color = [255,255,255]
color = [235,86,92]
x = 0.0
y = 0
midX = 960
midY = 540

def locateHead(img,xx,yy):
    print(str(xx)+" " + str(yy))
    for x in range(xx-60,xx+2,3):
        for y in range(yy+6,yy-2, -1):
            if((img[y,x,0] == color[0])):
                if((img[y,x,1] == color[1])):
                    return(x,y)
                    # return ((math.degrees(math.asin((x/960)-1))),(math.degrees(math.asin((y/540)-1))))
    return("head not found", "rip")

def find():
    screen = d.screenshot()
    print("searching")
    for x in range(0,1920,10):
        for y in range(0,1080, 5):
            if((screen[y,x,0] == color[0])):
                if((screen[y,x,1] == color[1])):
                    print("found")
                    return locateHead(screen,x,y)
                    # print("found at (" + str(x) + ", " + str(y) + ")")
                    # print((math.degrees(math.acos((x/960)-1))-90)*-1)
                    # global yy = y
                    # return ((math.degrees(math.acos((x/960)-1))-90)*-1,(math.degrees(math.acos((x/960)-1))-90)*-7.27)
    return("head not found", "rip")
while (True):
    colorMouse()
    if(keyboard.is_pressed('2')):
        x, y = find()
        if (x != "head not found"):
            print("found at: " + str(x-midX) + ", " + str(y-midY) + "from the center")
            pyt.moveRel((x-midX)/2.2, (y-midY)/2.2)
    # x+=10
    # pyt.moveRel(-10,0,0.2)
    # print(x)
    # if(x>2618):
        # x=0

    # colorMouse()
    # for i in range(360):
        # pyt.moveRel(math.cos(math.radians(i))*5,math.sin(math.radians(i))*5)
