from . import global_height
from kivy.uix.textinput import TextInput


class StringInput(TextInput):

    def __init__(self, **kwargs):
        super(StringInput, self).__init__(**kwargs)
        self.size_hint_y = None
        self.height = global_height
        self.write_tab = False
        self.multiline = False

