from kivy.graphics import Color, Rectangle
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
from kivy.properties import ObjectProperty


class ImageButton(ButtonBehavior, Image):
    background_normal = ObjectProperty()
    background_down = ObjectProperty()
    rect = None

    def __init__(self, source='', background_normal=(0, 1, 0, 1),
                 background_down=(0, 0, 1, 1), **kwargs):
        super(ImageButton, self).__init__(**kwargs)
        self.source = source
        self.background_normal = background_normal
        self.background_down = background_down
        self.build_background(background_normal)

    def build_background(self, color):
        r, g, b, a = color
        self.canvas.clear()
        with self.canvas:
            Color(r, g, b, a)
            self.rect = Rectangle(pos=self.pos, size=self.size, texture=self.texture)

    def set_color(self, color):
        r, g, b, a = color
        with self.canvas:
            Color(r, g, b, a)

    def on_pos(self, instance, pos):
        if self.rect:
            self.rect.pos = pos

    def on_size(self, instance, size):
        if self.rect:
            self.rect.size = size

    def on_background_normal(self, instance, color):
        self.build_background(color)

    def on_press(self):
        self.build_background(self.background_down)

    def on_release(self):
        self.build_background(self.background_normal)

