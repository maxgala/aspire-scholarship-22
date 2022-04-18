from member import Member

class SeniorExecutive(Member):
    def __init__(self,id, first_name, last_name, industry, max_coffee_chats, interests=[]):
        super().__init__(id, first_name, last_name, industry, interests)
        self.frequency = 0
        self.max_coffee_chats = max_coffee_chats
        self.num_coffee_chats = 0
    
    def get_frequency(self):
        return self.frequency
    
    def get_num_coffee_chats(self):
        return self.num_coffee_chats
    
    def get_max_coffee_chats(self):
        return self.max_coffee_chats

    def increment_frequency(self):
        self.frequency += 1

    def increment_num_coffee_chats(self):
        self.num_coffee_chats += 1
    