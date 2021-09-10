#This class i made is too cool to be deleted.

'''class Window:
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
            print('\n')'''