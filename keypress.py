import sublime
import sublime_plugin
import subprocess

if sublime.platform() == "linux":
    from xdotool import xdotool


class KeypressCommand(sublime_plugin.WindowCommand):
    def run(self, key=None):
        if sublime.platform() == "osx":
            script = """
                tell application "System Events"
                    keystroke "123"
                end tell
            """
            args = ["osascript", "-e", script]
            subprocess.Popen(args)
        elif sublime.platform() == "linux":
            xdotool("type", "123")
