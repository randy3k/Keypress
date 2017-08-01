import sublime
import sublime_plugin
import subprocess


if sublime.platform() == "osx":
    from .code import osx_keycode
else:
    from . import keyboard


class KeypressCommand(sublime_plugin.WindowCommand):
    def run(self, string=None, key=None):
        if not string and not key:
            return

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

        else:
            if string:
                keyboard.write(string)
            elif key:
                keyboard.press_and_release(key)
