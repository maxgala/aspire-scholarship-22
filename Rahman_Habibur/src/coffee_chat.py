from datetime import datetime
import pandas as pd
# class for coffee chat


class CoffeeChat:
    def __init__(self, name, date, time, location, aspiring_professional, senior_executive):
        self._name = name
        self._date = date
        self._time = time
        self._location = location
        self._aspiring_professional = aspiring_professional
        self._senior_executive = senior_executive

    def get_name(self):
        return self._name

    def get_date(self):
        return self._date

    def get_time(self):
        return self._time

    def get_location(self):
        return self._location

    def get_participants(self):
        return self._aspiring_professional, self._senior_executive

    def get_aspiring_professional(self):
        return self._aspiring_professional

    def get_senior_executive(self):
        return self._senior_executive

    def add_participant(self, aspiring_professional, senior_executive):
        self._aspiring_professional = aspiring_professional
        self._senior_executive = senior_executive

    def has_past(self):
        # string to datetime
        _date = pd.to_datetime(self._date + ' ' + self._time)
        return _date < datetime.now()

    def __str__(self):
        return "%10s" % self._name + "%15s" % self._date + "%10s" % self._time + "%10s" % self._location + "%40s" % self._aspiring_professional.__str__() + "%60s" % self._senior_executive.__str__()
