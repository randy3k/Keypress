import subprocess

_osx_keycode = {
    'enter': 36,
    'tab': 48,
    'space': 49,
    'delete': 117,
    'escape': 53,
    'up': 126,
    'down': 125,
    'left': 123,
    'right': 124,
    'home': 115,
    'end': 119,
    'pageup': 116,
    'pagedown': 121,
    'backspace': 51
}


def osx_keycode(key):
    if key in _osx_keycode:
        return _osx_keycode[key]
    elif len(key) == 1 and ord(key) < 128:
        return ord(key)
    else:
        raise ValueError("Key '{}' not found.".format(key))


def write(string):
    script = """
        tell application "System Events"
            keystroke "{}"
        end tell
    """.format(string.replace("\"", "\\\""))
    args = ["osascript", "-e", script]
    subprocess.Popen(args)


def press(key):
    modifiers = []
    if "shift" in key:
        modifiers.append("shift down")
    if "ctrl" in key:
        modifiers.append("control down")
    if "alt" in key:
        modifiers.append("option down")
    if "super" in key:
        modifiers.append("command down")
    modifiers_str = "using {" + ",".join(modifiers) + "}" if modifiers else ""

    key = key.split("+")[-1]
    script = """
        tell application "System Events"
            key code {} {}
        end tell
    """.format(str(osx_keycode(key)), modifiers_str)

    args = ["osascript", "-e", script]
    subprocess.Popen(args)
