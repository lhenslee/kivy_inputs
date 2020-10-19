import sys
sys.path.append('../..')
from kivy_inputs.date import DateInput
from kivy.app import App


class Test(App):

    def build(self):
        return DateInput()


Test().run()

