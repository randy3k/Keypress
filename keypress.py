import sublime
import sublime_plugin

from .keys import canonicalize_key

if sublime.platform() == "osx":
    from . import osx_keypress
elif sublime.platform() == "windows":
    from . import keyboard
elif sublime.platform() == "linux":
    from . import xdo


class KeypressCommand(sublime_plugin.WindowCommand):
    def run(self, string=None, key=None):
        """
        string: a string to write
        key: a string of keymap in Sublime Text style.
        """

        if key:
            key = canonicalize_key(key)
        elif string:
            pass
        else:
            raise ValueError("Need either `string` or `key` argument.")

        if sublime.platform() == "osx":
            if string:
                osx_keypress.write(string)
            elif key:
                osx_keypress.press(key)

        elif sublime.platform() == "windows":
            if string:
                keyboard.write(string)
            elif key:
                keyboard.press_and_release(key)

        elif sublime.platform() == "linux":
            xintance = xdo.Xdo()
            if string:
                xintance.enter_text_window(xdo.CURRENTWINDOW, string)
            elif key:
                xintance.send_keysequence_window(xdo.CURRENTWINDOW, key)
