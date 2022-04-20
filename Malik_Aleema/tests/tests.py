import sys
import unittest
sys.path.insert(0, '../src')
from main import MAX_algorithm
from helper import *

class TestMAXAlgorithm(unittest.TestCase):

    # Verify that an empty platform has no Coffee Chats
    def test_empty_platform(self):
        senior_executives_list = []
        aspiring_professionals_list = []

        coffee_chats = MAX_algorithm(senior_executives_list, aspiring_professionals_list)
        self.assertEqual(coffee_chats, [], 'Error: The Coffee Chats for the week were not as expected' )

    # Verify that an SE and AP with the same Industry get matched
    def test_industry_match(self):
        aspiring_professionals_list,senior_executives_list = [], []
        aspiring_professionals_list.append(AspiringProfessional(1, 'Aleema', 'Malik', 'Engineering', []))
        senior_executives_list.append(SeniorExecutive(2, 'Faheema', 'Abid', 'Engineering', 2, []))
        senior_executives_list.append(SeniorExecutive(3, 'Aqsa', 'Khan', 'Journalism', 2, []))

        # Execute the algorithm
        coffee_chats = MAX_algorithm(senior_executives_list, aspiring_professionals_list)
        
        # Verify there is only 1 Coffee Chat
        self.assertEqual(len(coffee_chats), 1, 'Error: There number of Coffee Chats were not as expected')

        # Verify AP1(id = 1) has a coffee chat
        self.assertEqual(coffee_chats[0].get_aspiring_professional(), 1, 'Error: AP1 does not have a Coffee Chat')

        # Verify the Coffee Chat is with SE1
        self.assertEqual(coffee_chats[0].get_senior_executive(), 2, 'Error: AP1 does not have a Coffee Chat with SE1')
        self.assertNotEqual(coffee_chats[0].get_senior_executive(), 3, 'Error: AP1 was incorrectly matched')

    # Verify that an SE and AP with the same interets but different industries don't get matched
    def test_interest_match(self):
        aspiring_professionals_list,senior_executives_list = [], []
        aspiring_professionals_list.append(AspiringProfessional(1, 'Aleema', 'Malik', 'Consulting', ['Career Development']))
        senior_executives_list.append(SeniorExecutive(2, 'Faheema', 'Abid', 'Journalism', 2, ['Career Development']))

        # Execute the algorithm
        coffee_chats = MAX_algorithm(senior_executives_list, aspiring_professionals_list)
        
        # Verify there is no Coffee Chat
        self.assertEqual(len(coffee_chats), 0, 'Error: There number of Coffee Chats were not as expected')

    # Verify that an AP will be matched with an SE they have the most common interets with
    def test_most_common_interest_match(self):
        aspiring_professionals_list,senior_executives_list = [], []
        aspiring_professionals_list.append(AspiringProfessional(1, 'Aleema', 'Malik', 'Consulting', ['Career Development'])) #AP1
        aspiring_professionals_list.append(AspiringProfessional(2, 'Aleema', 'Malik', 'Consulting', ['Writing Skills'])) #AP2
        senior_executives_list.append(SeniorExecutive(3, 'Faheema', 'Abid', 'Consulting', 1, ['Career Development'])) #SE1
        senior_executives_list.append(SeniorExecutive(4, 'Omer', 'Sulaiman', 'Consulting', 1, ['Interview Skills'])) #SE2

        # Execute the algorithm
        coffee_chats = MAX_algorithm(senior_executives_list, aspiring_professionals_list)
        
        # Verify there are 2 Coffee Chats since both SE have a max of and there are only 2 AP's
        self.assertEqual(len(coffee_chats), 2, 'Error: There number of Coffee Chats were not as expected')

        # Verify AP1 was matched with SE1 instead of SE2
        self.assertEqual(coffee_chats[0].get_aspiring_professional(), 1, 'Error: AP1 was not matched')
        self.assertEqual(coffee_chats[0].get_senior_executive(), 3, 'Error: Matching based off most common interets does not work as expected')

    # Verify that an AP won't get matched again with an SE they were matched with the week before
    def test_past_matches(self):
        aspiring_professionals_list,senior_executives_list = [], []
        senior_executives_list.append(SeniorExecutive(2, 'Faheema', 'Abid', 'Engineering', 2, []))
        senior_executives_list.append(SeniorExecutive(3, 'Aqsa', 'Khan', 'Engineering', 2, []))

        AP1 = AspiringProfessional(1, 'Aleema', 'Malik', 'Engineering', [])
        AP1.set_past_matches(2)
        aspiring_professionals_list.append(AP1)
        # Verify AP1 has one past match
        self.assertEqual(AP1.get_past_matches(), [2], 'Error: The wrong past match was set ')
        
        # Execute the algorithm
        coffee_chats = MAX_algorithm(senior_executives_list, aspiring_professionals_list)
        
        # Verify there is only 1 Coffee Chat
        self.assertEqual(len(coffee_chats), 1, 'Error: There number of Coffee Chats were not as expected')

        # Verify the Coffee Chat is with id = 3 since the past match was with id = 2
        self.assertEqual(coffee_chats[0].get_senior_executive(), 3, 'Error: AP1 match was not as expected')
        self.assertNotEqual(coffee_chats[0].get_senior_executive(), 2, 'Error: AP1 match was not as expected')
    
    # Verify that an SE who's reached their max coffee chat's won't get matched again
    def test_SE_max(self):
        aspiring_professionals_list,senior_executives_list = [], []
        aspiring_professionals_list.append(AspiringProfessional(1, 'Aleema', 'Malik', 'Finance', []))

        # SE1 has a max of 1 Coffee Chats. Set the number of coffee chats they've been scheduled already to 1.
        SE1 = SeniorExecutive(2, 'Faheema', 'Abid', 'Finance', 1, [])
        SE1.increment_num_coffee_chats()
        senior_executives_list.append(SE1)

        # Execute the algorithm
        coffee_chats = MAX_algorithm(senior_executives_list, aspiring_professionals_list)

        # Verify there are no coffee chats scheduled since the only SE in the platform is already busy
        self.assertEqual(len(coffee_chats), 0, 'Error: There number of Coffee Chats were not as expected')
    
    # Verify that the frequency an SE appears on the roster is as expected
    # Recall: It was assumend that Frequency a Senior Executive (SE) appears on the roster indicates each time they are matched with an Aspiring Professional (AP). This means, even if an SE did not get a coffee chat with an AP for the week, their freqeuency increments
    def test_frequency(self):
        aspiring_professionals_list,senior_executives_list = [], []
        aspiring_professionals_list.append(AspiringProfessional(1, 'Aleema', 'Malik', 'Business', []))
        aspiring_professionals_list.append(AspiringProfessional(2, 'Eshaan', 'Khan', 'Business', []))

        SE1 = SeniorExecutive(3, 'Aqsa', 'Khan', 'Business', 1, [])
        senior_executives_list.append(SE1)

        # Execute the algorithm
        coffee_chats = MAX_algorithm(senior_executives_list, aspiring_professionals_list)

        # Verify there are 1 coffee chats scheduled since the SE1 can be matched with AP1 and AP2 but SE1 can only comit to 1
        self.assertEqual(len(coffee_chats), 1, 'Error: There number of Coffee Chats were not as expected')

        # Verify that SE1 still had a frequency of 2 since it had a match with both AP1 and AP2
        self.assertEqual(SE1.get_frequency(), 2, 'Error: The frequency was not as expected')
    

if __name__ == '__main__':
    unittest.main()
