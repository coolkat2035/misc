import os, time
from collections import deque
import curses #add a module not found failproof here idk

WIDTH = 40
HEIGHT = 30

os.system(f"mode con: cols={WIDTH} lines={HEIGHT}")

menu = ["play", "options"]

class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.length = 3
        self.dead = False
        
        self.dir = 0 #up, right, down, left
        self.headpos = [x,y]
        self.allpos = deque([tuple(self.headpos[:])])
        
    def move(self):
        if self.dir == 0:#up
            self.allpos.appendleft((self.headpos[0], self.headpos[1]-1))
        elif self.dir == 1:#right
            self.allpos.appendleft((self.headpos[0]+1, self.headpos[1]))
        elif self.dir == 2:#down
            self.allpos.appendleft((self.headpos[0], self.headpos[1]+1))
        elif self.dir == 3:#left
            self.allpos.appendleft((self.headpos[0]-1, self.headpos[1]))

player = Snake(WIDTH // 2, HEIGHT // 2)

def startMenu(screen):
    height, width = screen.getmaxyx()
    for count, item in enumerate(menu):
        x = (width - len(item))//2
        y = height//2 + count 
        screen.addstr(y, x, item)


def Main(screen):
    curses.use_default_colors()

    def dotScr(x:int, y:int, c):#I hate my life
        screen.addstr(y, x, c)

    #startMenu(screen)

    while True:
        cin = screen.getch()

        if player.dead or cin == 101:#e key or die to quit
            screen.erase()
            screen.addstr(HEIGHT // 2, WIDTH // 2,"You died!")
            print("Game over!")
            time.sleep(0.5)
            exit()
        
        if cin == curses.KEY_UP and player.dir != 2 :#up when not facing down
            player.headpos = [player.headpos[0], player.headpos[1]-1]
            player.dir = 0
            player.isBlocked = "Not blocked"
        elif cin == curses.KEY_RIGHT and player.dir != 3:#right when not facing 
            player.headpos = [player.headpos[0]+1, player.headpos[1]]
            player.dir = 1
            player.isBlocked = "Not blocked"
        elif cin == curses.KEY_DOWN and player.dir != 0:#down when not facing up
            player.headpos = [player.headpos[0], player.headpos[1]+1]
            player.dir = 2
            player.isBlocked = "Not blocked"
        elif cin == curses.KEY_LEFT and player.dir != 1:#left when not facing right
            player.headpos = [player.headpos[0]-1, player.headpos[1]]
            player.dir = 3
            player.isBlocked = "Not blocked"
        else:
            player.isBlocked = "Blocked"

        player.move()

        while len(player.allpos) > player.length:
            player.allpos.pop()

#####################################################################################
        screen.erase()#cleear

        #draw snake body
        for pos in player.allpos:
            dotScr(pos[0], pos[1], 'o')

        #draw head
        dotScr(player.headpos[0], player.headpos[1], '+')

        screen.refresh()

        #antibug
        print(player.isBlocked)
        print(f"All pos: {player.allpos}")
        print(f"Current pos: {player.headpos}\n")

if __name__ == "__main__":
    curses.wrapper(Main)
