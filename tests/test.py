import sublime
from unittesting import DeferrableTestCase


class TestKeypress(DeferrableTestCase):

    def setUp(self):
        self.view = sublime.active_window().new_file()
        yield 2000

    def tearDown(self):
        if self.view:
            self.view.set_scratch(True)
            self.view.window().focus_view(self.view)
            self.view.window().run_command("close_file")

    def test_keypress_123(self):
        self.view.window().run_command("keypress", {"string": "123"})
        yield 1000
        self.assertEqual(self.view.substr(sublime.Region(0, self.view.size())), "123")

    def test_loremipsum(self):
        self.view.window().run_command("show_overlay", {"overlay": "command_palette"})
        yield 1000
        self.view.window().run_command("keypress", {"string": "loremipsum"})
        yield 1000
        self.view.window().run_command("keypress", {"key": "enter"})
        yield 1000
        self.assertIn("Lorem ipsum", self.view.substr(sublime.Region(0, self.view.size())))
