import sublime
import sublime_plugin
import subprocess

from .keys import canonicalize_key

if sublime.platform() == "osx":
    from .keys import osx_keycode
elif sublime.platform() == "windows":
    from . import keyboard
elif sublime.platform() == "linux":
    from xdotool import xdotool


class KeypressCommand(sublime_plugin.WindowCommand):
    def run(self, string=None, key=None):
        if not string and not key:
            return
        if key:
            key = canonicalize_key(key)

        if sublime.platform() == "osx":
            if string:
                script = """
                    tell application "System Events"
                        keystroke "{}"
                    end tell
                """.format(string.replace("\"", "\\\""))
            elif key:
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
                """.format(str(int(osx_keycode(key))), modifiers_str)

            args = ["osascript", "-e", script]
            subprocess.Popen(args)

        elif sublime.platform() == "windows":
            if string:
                keyboard.write(string)
            elif key:
                keyboard.press_and_release(key)

        elif sublime.platform() == "linux":
            if string:
                xdotool("type", string)
            elif key:
                xdotool("key", key)
