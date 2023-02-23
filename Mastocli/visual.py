import curses
from colorama import Fore, Back
import default

def generate_cool_message():
    messages = [
        "Stay cool and keep rockin' it!",
        "You're cooler than a penguin's toes!",
        "Don't be a fool, stay cool!",
        "Coolio, my friend!",
        "You're so cool, you could freeze lava!",
        "Chill out and enjoy life!",
        "Coolness runs in your veins!",
        "Keep calm and stay cool!",
        "You're cooler than a cucumber in a snowstorm!",
        "Ice, ice, baby! You're super cool!",
    ]
    return random.choice(messages)

def main(stdscr):
    logo = '''
    ███    ███  █████  ███████ ████████  ██████   ██████ ██      ██ 
    ████  ████ ██   ██ ██         ██    ██    ██ ██      ██      ██ 
    ██ ████ ██ ███████ ███████    ██    ██    ██ ██      ██      ██ 
    ██  ██  ██ ██   ██      ██    ██    ██    ██ ██      ██      ██ 
    ██      ██ ██   ██ ███████    ██     ██████   ██████ ███████ ██ 
                                                                    
                                                                
    
    '''
    # turn off cursor display
    curses.curs_set(0)
    
    # clear screen
    stdscr.clear()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    # print header
    stdscr.keypad(True)
    curses.start_color()
    stdscr.addstr(0, 0, (logo), curses.color_pair(1))
    stdscr.addstr(8, 0, "Press q to exit")
    stdscr.addstr(10, 0, "Press t to view your timeline")



    while True:
        # refresh the screen
        stdscr.refresh()

        # get user input
        c = stdscr.getch()

        # check if t key is pressed
        if c == ord('t'):
            print("\n\n")
            # Place a method to handle F1 key press here
            default.tl()
        
        # check if F2 key is pressed
        # elif c == ord('s'):
        #     mesg = input("Draft: ")
        #     default.toot(mesg)
        
        # check if F3 key is pressed
        elif c == curses.KEY_F3:
            # Place a method to handle F3 key press here
            stdscr.addstr(6, 0, "F3 key is pressed")
        
        # check if F4 key is pressed
        elif c == curses.KEY_F4:
            # Place a method to handle F4 key press here
            stdscr.addstr(7, 0, "F4 key is pressed")
        
        # check if F5 key is pressed
        elif c == curses.KEY_F5:
            # Place a method to handle F5 key press here
            stdscr.addstr(8, 0, "F5 key is pressed")
        
        # check if F6 key is pressed
        elif c == curses.KEY_F6:
            # Place a method to handle F6 key press here
            stdscr.addstr(9, 0, "F6 key is pressed")
        
        # check if F7 key is pressed
        elif c == curses.KEY_F7:
            # Place a method to handle F7 key press here
            stdscr.addstr(10, 0, "F7 key is pressed")
        
        # check if F8 key is pressed
        elif c == curses.KEY_F8:
            # Place a method to handle F8 key press here
            stdscr.addstr(11, 0, "F8 key is pressed")
        
        # check if F9 key is pressed
        elif c == curses.KEY_F9:
            # Place a method to handle F9 key press here
            stdscr.addstr(12, 0, "F9 key is pressed")
        
        # check if F10 key is pressed
        elif c == curses.KEY_F10:
            # Place a method to handle F10 key press here
            stdscr.addstr(13, 0, "F10 key is pressed")
        
        # check if 'q' key is pressed
        elif c == ord('q'):
            # exit the program if 'q' is pressed
            break

if __name__ == '__main__':
    # initialize curses
    stdscr = curses.initscr()
    curses.wrapper(main)
