from member import Member

class AspiringProfessional(Member):
    def __init__(self, id, first_name, last_name, industry, interests=[]):
        super().__init__(id, first_name, last_name, industry, interests)
        self.matches = {}
        self.num_coffee_chats = 0
        self.past_matches = []

    def get_matches(self):
        return self.matches

    def get_num_coffee_chats(self):
        return self.num_coffee_chats
    
    def get_past_matches(self):
        return self.past_matches

    def set_matches(self, senior_executive):
        # Get all the interests that are in common to the Aspiring Profsesional and Senior Executive
        matching_interests =  set(self.get_interests()).intersection(senior_executive.get_interests())
        # Store the matches in a dictionary {Senior Executive ID: Number of Common Interests}
        self.matches[senior_executive.get_id()] = len(matching_interests)

    def increment_num_coffee_chats(self):
        self.num_coffee_chats += 1

    def set_past_matches(self, senior_executive_id):
        self.past_matches.append(senior_executive_id)