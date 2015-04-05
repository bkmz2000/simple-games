from tkinter import *
from random import *
from time import *

root = Tk()
canv = Canvas(root, width = 400, height = 400, bg = 'black')
canv.pack()

def draw(arr, canv):
    canv.delete(ALL)
    for x in range(4):
        for y in range(4):
            if str(arr[y][x]) == '0':
                color = 'red'
            else:
                color = 'white'
            canv.create_text(x*100+50,
                             y*100+50,
                             text = str(arr[y][x]),
                             fill = color,
                             font = ('Consolas', 30))


    canv.update()

def move(arr, d, canv):
    global x, y
    oldX = x
    oldY = y
    
    if d == 's':
        if y+1 < 4:
            y+=1

    if d == 'w':
        if y-1 >=0:
            y-=1

    if d == 'd':
        if x+1 < 4:
            x+=1

    if d == 'a':
        if x-1 >=0:
            x-=1

    if x == oldX and y == oldY:
        return False

    arr[oldY][oldX] = arr[y][x]
    arr[y][x] = 0

    draw(arr, canv)

    return True

def shuffle(arr, canv):
    for i in range(40):
        if move(arr, choice(['w', 'd', 's', 'a']), canv):
            sleep(0.2)

    
arr = []

c = 0
for x in range(4):
    buff = []

    for y in range(4):
        buff.append(c)
        c+=1

    arr.append(buff)


x = 0
y = 0

root.bind('w', lambda a: move(arr, 'w', canv))
root.bind('s', lambda a: move(arr, 's', canv))
root.bind('a', lambda a: move(arr, 'a', canv))
root.bind('d', lambda a: move(arr, 'd', canv))

shuffle(arr, canv)

draw(arr, canv)
