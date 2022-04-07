from utils import *
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
        for upcoming in self._upcoming:
            lists.append(upcoming.__str__() + "\n" + line)
        return "\n".join(lists)

    def str_past(self) -> str:
        lists = []
        for past in self._past:
            lists.append(past.__str__() + "\n" + line)
        return "\n".join(lists)

    def __str__(self) -> str:
        return "Upcoming: \n" + self.str_upcoming() + "\n" + "Past: \n" + self.str_past()
