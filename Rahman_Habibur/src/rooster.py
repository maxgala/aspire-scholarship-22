from utils import *
import pandas as pd
# class for weekly rooster of coffee chats


class Rooster:
    def __init__(self, upcoming, past):
        self._upcoming = upcoming
        self._past = past

    def get_upcoming(self):
        return self._upcoming

    def get_past(self):
        return self._past

    def add_upcoming(self, upcoming):
        self._upcoming.append(upcoming)

    def add_past(self, past):
        self._past.append(past)

    def str_upcoming(self) -> str:
        lists = []
        prev = None
        for upcoming in self._upcoming:
            _str = upcoming.__str__()
            if prev != None:
                prev_date = pd.to_datetime(
                    str(prev.get_date()) + ' ' + str(prev.get_time()))
                up_date = pd.to_datetime(
                    str(upcoming.get_date()) + ' ' + str(upcoming.get_time()))
                if prev_date.week != up_date.week or prev_date.year != up_date.year:
                    _str = "\n" + line + _str
            lists.append(_str)
            prev = upcoming
        return "\n".join(lists) + "\n" + line

    def str_past(self) -> str:
        lists = []
        prev = None
        for past in self._past:
            _str = past.__str__()
            if prev != None:
                prev_date = pd.to_datetime(
                    str(prev.get_date()) + ' ' + str(prev.get_time()))
                past_date = pd.to_datetime(
                    str(past.get_date()) + ' ' + str(past.get_time()))
                if prev_date.week != past_date.week or prev_date.year != past_date.year:
                    _str = "\n" + line + _str
            lists.append(_str)
            prev = past
        return "\n".join(lists) + "\n" + line

    def __str__(self) -> str:
        return "Upcoming: \n" + self.str_upcoming() + "\n" + "\nPast: \n" + self.str_past()
