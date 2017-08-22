from xdotool import xdotool


linux_keyname = {
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
    xdotool("type", string)


def press(key):
    eachkey = key.split("+")
    if eachkey[-1] in linux_keyname:
        eachkey[-1] = linux_keyname[eachkey[-1]]

    key = "+".join(eachkey)
    xdotool("key", key)
