from random import randint, choice
from tkinter import Tk, Canvas
from time import time


size = 20
cellSize = 20
vis = []



def suits(x, y):
    if (x, y) in vis:
        return False

    if y+1 < size:
        if arr[y+1][x] == 1:
            return False

    if y-1 >= 0:
        if arr[y-1][x] == 1:
            return False
    
    if x+1 < size:
        if arr[y][x+1] == 1:
            return False

    if x-1 >= 0:
        if arr[y][x-1] == 1:
            return False

    return True


def genFrom(x, y):
    vis.append((x, y))
    arr[y][x] = 2
    av        = []

    if x+1 < size:
        if suits(x+1, y):
            av.append((x+1, y))

    if x-1 > 0:
        if suits(x-1, y):
            av.append((x-1, y))

    if y+1 < size:
        if suits(x, y+1):
            av.append((x, y+1))

    
    if y-1 > 0:
         if suits(x, y-1):
            av.append((x, y-1))

    arr[y][x] = 1

    if len(av) == 0:
        return

    to = choice(av)

    X = to[0]
    Y = to[1]

    arr[y][x] = 1

    genFrom(X, Y)

arr = [[0 for i in range(size)] for i in range(size)]
vis = []
now = time()
genFrom(0, 0)

for i in range(size**2):
    cell = choice(vis)
    x = cell[0]
    y = cell[1]
    genFrom(x, y)

print(time()- now)

root = Tk()
canv = Canvas(root, width = cellSize*size, height = cellSize*size, bg = 'black')

for x in range(size):
    for y in range(size):
        if arr[y][x] == 1:
            color = 'black'

        if arr[y][x] == 0:
            color = 'white'

        canv.create_rectangle(x*cellSize, y*cellSize,
                              x*cellSize+cellSize, y*cellSize+cellSize, fill = color)

vis.sort()
print(len(vis))

for i in vis:
    n = vis.count(i)
    while vis.count(i) > 1:
        del vis[vis.index(i)]

    print(i, n)

print(len(vis))
canv.pack()
root.mainloop()


