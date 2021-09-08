import os, time

class Window:
    def __init__(self, w:int, h:int):
        self.width = w
        self.height = h
        self.display = arr = [[' ' for i in range(w)] for j in range(h)]

        os.system(f"mode con: cols={w} lines={h}") #makes the window lolol stackoverflow moment lodfsdl
        
    def update(self):
        for r in self.display:
            for c in r:
                print(c, end='')
            print('\r')


    def dot(self, x:int, y:int, c='#'):
        '''
            puts the character {c} into the coords. Default is # but it shouldn't happen
        '''
        self.display[y][x] = c

    def dotMul(self, startx, y, char, l):
        '''
            puts chars repeatedly on a row, not sure if its useful''' 

        for x in range(l):
            self.display[y][x+startx] = char

Screen = Window(40,30)



def Main():
    i = 0
    Screen.dot(5, 10,'o')
    Screen.dot(5, 11, 'B')

    while True:
        i += 1
            
            
        Screen.dotMul(10, 9+i, 'a', 5)

        Screen.update()

        time.sleep(0.5)

if __name__ == "__main__":
    Main()
