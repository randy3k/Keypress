import sublime


if sublime.platform() == "osx":
    os_keyname = {}

elif sublime.platform() == "windows":
    os_keyname = {}

elif sublime.platform() == "linux":
    os_keyname = {
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


def canonicalize_key(key):
    eachkey = key.split("+")
    if eachkey[-1] in os_keyname:
        eachkey[-1] = os_keyname[eachkey[-1]]

    return "+".join(eachkey)
