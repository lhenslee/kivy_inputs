from . import global_height
from .arrows import Adjust
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput


class Input(TextInput):

    def __init__(self, **kwargs):
        super(Input, self).__init__(**kwargs)
        self.multiline = False
        self.write_tab = False

    def on_text(self, *args):
        new_text = ''
        for i, char in enumerate(self.text):
            if char.isnumeric() or (char == '-' and i == 0):
                new_text += char
        if new_text == '-':
            new_text = '-1'
        self.text = new_text

    def increment(self, *args):
        if self.text == '':
            self.text = '1'
        else:
            self.text = str(int(self.text)+1)

    def decrement(self, *args):
        if self.text == '':
            self.text = '-1'
        else:
            self.text = str(int(self.text)-1)

    def get_value(self):
        if self.text == '':
            return 0
        else:
            return int(self.text)


class NumberInput(BoxLayout):

    def __init__(self, **kwargs):
        super(NumberInput, self).__init__(**kwargs)
        self.size_hint_y = None
        self.height = global_height
        self.orientation = 'horizontal'
        self.input = Input()
        self.adjust = Adjust()
        self.up_arrow = self.adjust.up_arrow
        self.down_arrow = self.adjust.down_arrow
        self.up_arrow.bind(on_press=self.input.increment)
        self.down_arrow.bind(on_press=self.input.decrement)
        self.add_widget(self.input)
        self.add_widget(self.adjust)

