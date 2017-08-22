import sublime_plugin

from . import platform_keypress


class KeypressCommand(sublime_plugin.WindowCommand):
    def run(self, string=None, key=None):
        """
        string: a string to write
        key: a string of keymap in Sublime Text style.
        """

        if not key and not string:
            raise ValueError("Need either `string` or `key` argument.")

        if string:
            platform_keypress.write(string)
        elif key:
            platform_keypress.press(key)
