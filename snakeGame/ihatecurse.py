import os
import curses

HEIGHT = 30
WIDTH = 40
os.system(f"mode con: cols={WIDTH+1} lines={HEIGHT}")

def Main(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)

    #windows
    window = curses.newwin(HEIGHT, WIDTH)
    window.keypad(1)

    window.border(0)
    window.timeout(0)#wait what is this

    #this lib has so much shit

    snake = [(15,20), (16,20), (17,20)]
    y = 15
    x = 20
    direction = 0
    isBlocked = False
    length = len(snake)

    #print("Init completed.\n")

    while True:
        key = window.getch()
        if key == ord('e'):
            break
        if key == ord('a'):
            length += 1
        
        if key != -1:#change dir
            if key == curses.KEY_UP and direction != 2 :#up when not facing down
                y -= 1
                direction = 0
                isBlocked = False
            elif key == curses.KEY_RIGHT and direction != 3:#right when not facing 
                x += 1
                direction = 1
                isBlocked = False
            elif key == curses.KEY_DOWN and direction != 0:#down when not facing up
                y += 1
                direction = 2
                isBlocked = False
            elif key == curses.KEY_LEFT and direction != 1:#left when not facing right
                x -= 1
                direction = 3
                isBlocked = False
            else:
                isBlocked = True

        else:#move forward

            print((x, y))
            


        window.clear()
        
        for pos in range(len(snake)):
            window.addch(snake[pos][0], snake[pos][1], 'o')

        window.addnstr(HEIGHT - 3, 0, str(snake) + ' ' + str(isBlocked), WIDTH, curses.A_STANDOUT)
        window.addstr('', curses.A_REVERSE)

        window.refresh()
    curses.napms(1000)

if __name__ == "__main__":
    curses.wrapper(Main)
    curses.endwin()
