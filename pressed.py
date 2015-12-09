import curses
stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

stdscr.refresh()

key = ''
while key != ord('q'):
    key = stdscr.getch()
    stdscr.addch(0,0,key)
    # stdscr.refresh()
    if key == curses.KEY_UP:
        stdscr.addstr(0, 10, "Up")
    elif key == curses.KEY_DOWN: 
    	print "DOWN"
    	curses.endwin()
        stdscr.addstr(0, 10, "Down")

curses.endwin()