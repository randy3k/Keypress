canonical_names = {
    'escape': 'esc',
    'return': 'enter',
    'del': 'delete',
    'control': 'ctrl',
}

_osx_keycode = {
    'enter': 0x24,
    'tab': 0x30,
    'space': 0x31,
    'delete': 0x33,
    'esc': 0x35,
    'up': 0x7E,
    'down': 0x7D,
    'left': 0x7B,
    'right': 0x7C,
    'home': 0x73,
    'end': 0x77,
    'page up': 0x74,
    'page down': 0x79,
    }


def osx_keycode(key):
    key = key.lower()
    if key in canonical_names:
        key = canonical_names[key]
    if key in _osx_keycode:
        return _osx_keycode[key]
    elif len(key) == 1 and ord(key) < 128:
        return ord(key)
    else:
        raise ValueError("Key '{}' not found.".format(key))
