import os, time

width = 40
height = 30
isBlocked = "Not blocked"
class Window:
    def __init__(self, w:int, h:int):
        self.width = w
        self.height = h + 10
        self.display = [[' ' for i in range(w)] for j in range(h)]

        os.system(f"mode con: cols={width} lines={height}") #makes the window lolol stackoverflow moment lodfsdl
        
    def dot(self, x:int, y:int, c='#'):
        '''
            adds the character {c} into the coords array. Default is # but it shouldn't happen.
            Requires update() to actually print them out. lol
        '''
        self.display[y-1][x-1] = c

    def dotMul(self, startx, y, char, l):
        '''
            puts chars repeatedly on a row, not sure if its useful''' 

        for x in range(l):
            self.display[y][x+startx] = char
            
    def update(self):
        print('\r')
        for r in self.display:
            for c in r:
                print(c, end='')
            print('\n')

class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dir = 0 #up, right, down, left
        self.headpos = [x,y]
        self.allpos = [tuple(self.headpos[:])]
        
    def move(self, direction):
        global isBlocked
        if direction == '0' and self.dir != 2:#up when not facing down
            self.headpos = [self.headpos[0], self.headpos[1]-1]
            self.allpos.append((self.headpos[0], self.headpos[1]))
            self.dir = 0
            isBlocked = "Not blocked"

        elif direction == '1' and self.dir != 3:#right when not facing 
            self.headpos = [self.headpos[0]+1, self.headpos[1]]
            self.allpos.append((self.headpos[0], self.headpos[1]))
            self.dir = 1
            isBlocked = "Not blocked"

        elif direction == '2' and self.dir != 0:#down when not facing up
            self.headpos = [self.headpos[0], self.headpos[1]+1]
            self.allpos.append((self.headpos[0], self.headpos[1]))
            self.dir = 2
            isBlocked = "Not blocked"

        elif direction == '3' and self.dir != 1:#left when not facing right
            self.headpos = [self.headpos[0]-1, self.headpos[1]]
            self.allpos.append((self.headpos[0], self.headpos[1]))
            self.dir = 3
            isBlocked = "Not blocked"

        else:
            isBlocked = "Blocked"
        

Screen = Window(width,height)
player = Snake(int(width/2), int(height/2))

def Main():
    print(f"All pos: {player.allpos}")
    print(f"Current pos: {player.headpos}")

    while True:
        cin = input()

        player.move(cin) 

        


        for pos in player.allpos:
            Screen.dot(pos[0], pos[1], 'o')
        Screen.dot(player.headpos[0], player.headpos[1], '+')

        Screen.update()

        print(isBlocked)
        print(f"All pos: {player.allpos}")
        print(f"Current pos: {player.headpos}")

if __name__ == "__main__":
    Main()
