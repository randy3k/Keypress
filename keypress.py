import sublime
import sublime_plugin

if sublime.platform() == "osx":
    from . import osx_keypress as kp
elif sublime.platform() == "windows":
    from . import windows_keypress as kp
elif sublime.platform() == "linux":
    from . import linux_keypress as kp


class KeypressCommand(sublime_plugin.WindowCommand):
    def run(self, string=None, key=None):
        """
        string: a string to write
        key: a string of keymap in Sublime Text style.
        """

        if not key and not string:
            raise ValueError("Need either `string` or `key` argument.")

        if string:
            kp.write(string)
        elif key:
            kp.press(key)
