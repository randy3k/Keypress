import sublime
import sublime_plugin
import subprocess

if sublime.platform() == "linux":
    from xdotool import xdotool

if sublime.platform() == "windows":
    import win32com.client


class KeypressCommand(sublime_plugin.WindowCommand):
    def run(self, string=""):
        if sublime.platform() == "osx":
            script = """
                tell application "System Events"
                    keystroke "{}"
                end tell
            """.format(string.replace("\"", "\\\""))
            args = ["osascript", "-e", script]
            subprocess.Popen(args)
        elif sublime.platform() == "linux":
            xdotool("type", string)
        elif sublime.platform() == "windows":
            shell = win32com.client.Dispatch("WScript.Shell")
            shell.SendKeys(string)
