import sublime
from unittesting import DeferrableTestCase


class TestKeypress(DeferrableTestCase):

    def setUp(self):
        self.view = sublime.active_window().new_file()
        # make sure we have a window to work with
        s = sublime.load_settings("Preferences.sublime-settings")
        s.set("close_windows_when_empty", False)

    def tearDown(self):
        if self.view:
            self.view.set_scratch(True)
            self.view.window().focus_view(self.view)
            self.view.window().run_command("close_file")

    def test_keypress_123(self):
        self.view.window().run_command("keypress")
        yield 1000
        self.assertEqual(self.view.substr(sublime.Region(0, self.view.size())), "123")
