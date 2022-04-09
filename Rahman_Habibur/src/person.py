# class for person objects
class Person:
    def __init__(self, firstname, lastname, industry):
        self._first_name = firstname
        self._last_name = lastname
        self._industry = industry

    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def get_interests(self):
        return self._interests

    def get_industry(self):
        return self._industry

    def set_industry(self, industry):
        self._industry = industry

    def __str__(self):
        return self._first_name + " | " + self._last_name + " | " + self._industry


# class for aspirining professionals objects
class AspiringProfessional(Person):
    def __init__(self, firstname, lastname, industry, interests=[]):
        super().__init__(firstname, lastname, industry)
        self._interests = interests

    def __str__(self):
        return super().__str__() + " | " + self.str_interests()

    def add_interests(self, interest):
        self._interests.append(interest)

    def str_interests(self):
        if len(self._interests) == 0:
            return "None"
        return "\n".join(self._interests)

# class for senior executives objects


class SeniorExecutive(Person):
    def __init__(self, firstname, lastname, industry, frequency):
        super().__init__(firstname, lastname, industry)
        self._frequency = frequency

    def get_frequency(self):
        return self._frequency

    def __str__(self):
        return super().__str__() + "  | " + self._frequency
