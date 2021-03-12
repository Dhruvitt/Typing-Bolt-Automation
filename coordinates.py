import pyautogui as gui


CHROME = (118, 742)     # chrome icon in taskbar
TYPING_WINDOW = (117, 12)        # typing bolt tab in chrome
KEYBOARD = (696, 306)       # The white area above the virtual keyboard in typing bolt
SCROLLER_BAR_UP = (1357, 106)        # for top most scroll bar location
SCROLLER_BAR_DOWN = (1357, 693)     # for bottom most scroll bar location
PRACTICE_BUTTON = (767, 101)        # coordinate for practice button
PRAC_LOAD_TIME = 2         # time it takes to load the page after clicking practice button depending on the ping and speed.
RUN_N_TIMES = 1         # how much times you want to run it


def click_n_times(coord, n=10):
    '''
    coord takes an tuple of type, (x,y)
    '''
    gui.mouseUp()
    for _ in range(n):
        gui.click(coord)
    gui.mouseUp()
