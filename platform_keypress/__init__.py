import sublime


if sublime.platform() == "osx":
    from .osx_keypress import write, press
elif sublime.platform() == "windows":
    from .windows_keypress import write, press
elif sublime.platform() == "linux":
    from .linux_keypress import write, press
