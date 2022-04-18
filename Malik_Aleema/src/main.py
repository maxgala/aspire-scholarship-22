from helper import *
from coffee_chat import CoffeeChat

'''
The algorithm goes through the following 3 steps in order to intellgiently output a list of coffee chats for every Aspiring Professional on the Platform
Step 1: Industry Match
Match Senior Executives (SE) with Aspiring Profssionals (AP) based on common Industry. This is because, from my experience with MAX, one of the goals is to connect aspiring individuals with senior executives
EX: Every SE in Engineering will get matched to every AP in Engineering
Step 2: Interests Match
Once all AP's have a list of all their SE industry matches, sort their SE matches from most common interets to least common interests. Research shows that mentor-mentee pair are most effective when the two are partnered up according to their interests. This was especiallly highlighted in the article published by the National Library of Medicine entitles Characteristics of Successful and Failed Mentoring Relationships: A Qualitative Study Across Two Academic Health Centers [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3665769/]
EX: After Step 1: SE1 and SE2 are matched to AP1 because of their common insudstry
    SE1: Interets are Career Development and Writing Skills
    SE2: Interets are Career Development and Communication Skills
    AP1: Interets are Career Development and Communication Skills
    AP1's matches will be ordererd as the following: SE2, SE1. This is becaues AP1 has more common interets with SE2 than SE1
Step 3: Set up Coffee Chats
This step requires you to iterate through the AP's sorted matches and set up coffee chats. However, there are a number of cases to consider. It was assumed that due to the nature of SE's roles, All SE's have a max number of coffee chats they can commit to. Every match goes through the following:
1) If the AP had a coffee chat the week before with this SE, DO NOT set up another coffee chat. This is to ensure that SE's are circulating between all AP's
2) If the SE is near their max number of coffee chats and the current AP already has atleast one coffee chat DO NOT set up a coffee chat. This is so that you can distrubute SE to other AP
3) Otherwise, If the SE can commit to another coffee chat, DO set up a coffee chat

Additional Notes:
- It was assumed that the frequency an SE appears on the roster indicates each time they are matched with an AP. This means, even if an SE did not get a coffee chat with an AP for the week, their freqeuency increments. This could be helpful in determining the distribution of your AP's and can help in figuring out what other SE's should be scouted. 
EX: SE1 frequency is 3 (Matched with AP1, AP2 and AP3) but this week only got a coffee chat with AP1. This is possible if SE1 has max number of coffee chat of 1. Knowing SE1's frequency is 3, it might better the matching platform to get more SE's that have similar qualifications so that AP2 and AP3 could get a coffee chat as well.
'''
def MAX_algorithm(senior_executives_list,aspiring_professionals_list):

    # Data structure to hold this weeks Coffee Chats 
    coffee_chats = []

    # Get all id's of the senior executives and aspiring professionals 
    senior_executive_dict = get_member_id(senior_executives_list)

    # Iterate through all Aspiring Professionals and match them with Senior Executives based on Industry and Interets
    for aspriring in aspiring_professionals_list:
        for senior in senior_executives_list:
            # A match is made first based off common industry
            if(aspriring.get_industry() == senior.get_industry()):
                aspriring.set_matches(senior)
                # Increment the frequency
                senior.increment_frequency()

        # After storing all the Senior Executives with Aspriring Professionals, sort them based off most number of common interests to least
        sorted_matches = sorted(aspriring.get_matches().items(), key=lambda x: x[1], reverse=True)  

        # Set coffee chats
        for id, num_common_interets in sorted_matches:
            senior_executive = senior_executive_dict[id]
            # If the Aspiring Professional had a coffee chat the week before with this Senior Executive, DO NOT set up another coffee chat
            if id in aspriring.get_past_matches():
                del (aspriring.get_matches())[id]

            # Otherwise check if a match can be made
            else:
                # If the Senior Executive is near their max number of coffee chats and the current Aspiring Professional already has atleast one coffee chat DO NOT set up a coffee chat so that you can distrubute senior executives to all aspiring professionals
                if senior_executive.get_num_coffee_chats() == (senior_executive.get_max_coffee_chats() - 1) and aspriring.get_num_coffee_chats() >= 1:
                    del (aspriring.get_matches())[id]

                # If the Senior Executive has not reached their max number of coffee chats, DO set up a coffee chat
                elif senior_executive.get_num_coffee_chats() < senior_executive.get_max_coffee_chats():
                    senior_executive.increment_num_coffee_chats()
                    aspriring.increment_num_coffee_chats()
                    aspriring.set_past_matches(senior_executive.get_id())
                    coffee_chats.append(CoffeeChat(aspriring.get_id(), senior_executive.get_id(),get_random_date() ,'Online'))

                # Otherwise, the coffee chat cannot be set up
                else:
                    del (aspriring.get_matches())[id]

    return coffee_chats

if __name__ == "__main__":

    # Get all the mock data used for the algorithm
    senior_executives_list, aspiring_professionals_list = load_members()

    # Execute the algorithm
    coffee_chats = MAX_algorithm(senior_executives_list, aspiring_professionals_list)

    # Display the list of coffee chats for every Aspiring Professional on the Platform and Senior Executive Statistics for this week
    print_coffee_chats(coffee_chats,senior_executives_list, aspiring_professionals_list)
