from . import global_height, label_width
from .arrows import Adjust
from .number import Input
from calendar import monthrange
from datetime import datetime as dt
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


class PositiveInput(Input):

    def __init__(self, **kwargs):
        super(PositiveInput, self).__init__(**kwargs)
        self.bind(text=self.make_positive)

    def make_positive(self, *args):
        self.text = self.text.replace('-', '')


class Month(PositiveInput):

    def __init__(self, **kwargs):
        super(Month, self).__init__(**kwargs)

    def on_text(self, *args):
        if self.get_value() > 12:
            self.text = '12'


class Day(PositiveInput):

    def __init__(self, **kwargs):
        super(Day, self).__init__(**kwargs)


class Year(PositiveInput):

    def __init__(self, **kwargs):
        super(Year, self).__init__(**kwargs)

    def on_text(self, *args):
        if len(self.text) > 4:
            self.text = self.text[:4]


class Info(Label):

    def __init__(self, **kwargs):
        super(Info, self).__init__(**kwargs)
        self.size_hint_x = None
        self.width = label_width
        self.text = 'MM/DD/YYYY'


class DateInput(BoxLayout):

    def __init__(self, **kwargs):
        super(DateInput, self).__init__(**kwargs)
        self.size_hint_y = None
        self.height = global_height
        self.month = Month()
        self.day = Day()
        self.year = Year()
        self.info = Info()
        self.adjust = Adjust()
        self.increment = self.adjust.up_arrow
        self.decrement = self.adjust.down_arrow
        self.increment.bind(on_press=self.increment_day)
        self.month.bind(text=self.check_days)
        self.day.bind(text=self.check_days)
        self.year.bind(text=self.check_days)
        self.add_widget(self.month)
        self.add_widget(self.day)
        self.add_widget(self.year)
        self.add_widget(self.info)
        self.add_widget(self.adjust)

    def check_days(self, *args):
        if self.date_is_invalid():
            self.info.text = 'MM/DD/YYYY'
            return
        month, day, year = self.mdy_tuple()
        max_days = monthrange(year, month)[1]
        if day > max_days:
            self.day.text = str(max_days)
        else:
            date = dt(year, month, day)
            self.info.text = weekdays[date.weekday()]

    def date_is_invalid(self):
        month, year, day = self.mdy_tuple()
        return month == 0 or year == 0 or day == 0

    def mdy_tuple(self):
        return self.month.get_value(), self.day.get_value(), self.year.get_value()

    def increment_day(self, *args):
        if self.date_is_invalid():
            self.info.text = 'MM/DD/YYYY'
            return
        month, day, year = self.mdy_tuple()
        max_days = monthrange(year, month)[1]
        if day == max_days:
            day = 1
            month += 1
        else:
            day += 1
        if month == 13:
            month = 1
            year += 1
        self.month.text = str(month)
        self.day.text = str(day)
        self.year.text = str(year)

