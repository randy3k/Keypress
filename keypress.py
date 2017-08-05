import sublime
import sublime_plugin

if sublime.platform() == "osx":
    from . import osx_keypress
elif sublime.platform() == "windows":
    from . import windows_keypress
elif sublime.platform() == "linux":
    from xdotool import xdotool


class KeypressCommand(sublime_plugin.WindowCommand):
    def run(self, string=None, key=None):
        """
        string: a string to write
        key: a string of keymap in Sublime Text style.
        """

        if not key and not string:
            raise ValueError("Need either `string` or `key` argument.")

        if sublime.platform() == "osx":
            if string:
                osx_keypress.write(string)
            elif key:
                osx_keypress.press(key)

        elif sublime.platform() == "windows":
            if string:
                windows_keypress.write(string)
            elif key:
                windows_keypress.press(key)

        elif sublime.platform() == "linux":
            if string:
                xdotool("type", string)
            elif key:
                xdotool("key", key)
