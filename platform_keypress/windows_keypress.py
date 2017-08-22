from . import keyboard


win_keyname = {
    'enter': "Return",
    'tab': "Tab",
    'space': "Space",
    'delete': "Delete",
    'escape': 'Escape',
    'up': 'Up',
    'down': 'Down',
    'left': 'Left',
    'right': 'Right',
    'home': 'Home',
    'end': 'End',
    'pageup': 'Prior',
    'pagedown': 'Next',
    'backspace': "Backspace"
}


def write(string):
    keyboard.write(string)


def press(key):
    eachkey = key.split("+")
    if eachkey[-1] in win_keyname:
        eachkey[-1] = win_keyname[eachkey[-1]]

    key = "+".join(eachkey)
    keyboard.press_and_release(key)
