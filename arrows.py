from . import global_height
from .image_button import ImageButton
from .resources import resource_dir
from kivy.uix.boxlayout import BoxLayout
import os


class Arrow(ImageButton):

    def __init__(self, **kwargs):
        kwargs['size_hint'] = (None, None)
        kwargs['size'] = (global_height/2, global_height/2)
        super(Arrow, self).__init__(**kwargs)


class LeftArrow(Arrow):

    def __init__(self, **kwargs):
        kwargs['source'] = os.path.join(resource_dir, 'left-arrow.png')
        super(LeftArrow, self).__init__(**kwargs)


class RightArrow(Arrow):

    def __init__(self, **kwargs):
        kwargs['source'] = os.path.join(resource_dir, 'right-arrow.png')
        super(RightArrow, self).__init__(**kwargs)


class DownArrow(Arrow):

    def __init__(self, **kwargs):
        kwargs['source'] = os.path.join(resource_dir, 'down-arrow.png')
        super(DownArrow, self).__init__(**kwargs)


class UpArrow(Arrow):

    def __init__(self, **kwargs):
        kwargs['source'] = os.path.join(resource_dir, 'up-arrow.png')
        super(UpArrow, self).__init__(**kwargs)


class Adjust(BoxLayout):

    def __init__(self, **kwargs):
        super(Adjust, self).__init__(**kwargs)
        self.size_hint_x = None
        self.width = global_height/2
        self.up_arrow = UpArrow()
        self.down_arrow = DownArrow()
        self.orientation = 'vertical'
        self.add_widget(self.up_arrow)
        self.add_widget(self.down_arrow)

