import sys
sys.path.append('../..')
from kivy_inputs.number import NumberInput
from kivy.app import App


class Test(App):

    def build(self):
        return NumberInput()


Test().run()

