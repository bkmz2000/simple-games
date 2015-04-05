from tkinter import *
from random import *
from tkinter.messagebox import *
from time import *

Width  = 200
Height = 200 

class Enemy:
    def __init__(self, x, y, width):
        self.x = x
        self.y = y

        self.color = choice(['red',
                             'green',
                             'yellow',
                             'blue',
                             'cyan',
                             'magenta'])

        self.width = width

    def fall(self):
        self.y += int(self.width/5)

    def draw(self, canv):
        x = self.x
        y = self.y

        color = self.color

        canv.create_rectangle(self.x,
                              self.y,
                              self.x + self.width,
                              self.y + self.width,
                              fill = self.color)
        canv.update()

        
class player:
    def __init__(self, width, height):
        self.x = randint(width/4, width-width/4)
        self.y = randint(height/4, height-height/4)
        self.width = 10
        
    def draw(self, canv):
        x = self.x
        y = self.y
        width = self.width
        
        canv.create_rectangle(x,
                              y,
                              x+self.width,
                              y+self.width,
                              fill = 'white')
        canv.update()
    
        
    def move(self, d):
        if d == 'w':
            self.y-=1

        if d == 'd':
            self.x+=1

        if d == 'a':
            self.x-=1

        if d == 's':
            self.y+=1
            
def genEnemies():
    enemies = []
    y = 0
    for i in range(10):
        width = randint(5, 20)

        en = Enemy(x = randint(0, 200-width), y=y, width = width)

        enemies.append(en)
        y-=10
    del y
    return enemies

def setUp(pl):
    root = Tk()
    canv = Canvas(width = Width, height = Height, bg = 'black')

    root.bind('w', lambda a:pl.move('w'))
    root.bind('d', lambda a:pl.move('d'))
    root.bind('a', lambda a:pl.move('a'))
    root.bind('s', lambda a:pl.move('s'))

    return {'root': root, 'canv': canv}
   


def startGame():
    enemies = genEnemies()
    pl = player(Width, Height)
    game = setUp(pl)
    
    canv = game['canv']
    root = game['root']

    canv.pack()
     
    alive = True
    
    while alive:    
        for en in enemies:
            en.draw(canv)
            en.fall()
            
            if en.y>200:
                width = randint(5, 20)
                enemies[enemies.index(en)] = Enemy(x = randint(0, 200-width), y=0, width = width)

            if pl.y <= en.y+en.width and pl.y >= en.y:
                if pl.x > en.x and pl.x < en.x + en.width:
                    alive = False

                if pl.x + pl.width >= en.x and pl.x + pl.width <= en.x + en.width:
                    alive = False

                    
        pl.draw(canv)
        sleep(0.05)
        canv.delete(ALL)

startGame()
