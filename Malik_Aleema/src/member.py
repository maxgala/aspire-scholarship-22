from random import randint

class Member:
    def __init__(self, id, first_name, last_name, industry, interests=[]):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.industry = industry
        self.interests = interests

    def get_id(self):
        return self.id

    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name

    def get_industry(self):
        return self.industry
    
    def get_interests(self):
        return self.interests

