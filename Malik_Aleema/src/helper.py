from senior_executive import SeniorExecutive
from aspiring_professional import AspiringProfessional
from tabulate import tabulate
from datetime import datetime, timedelta
import random
import json

# Method used to load data from JSON files
def load_data(file_name):
    f = open (file_name, "r")
    data = json.loads(f.read())
    return data

# Method used to create objects depending on the mock JSON data
def load_members():
    senior_executives = load_data("../data/senior_executive_data.json")
    senior_executives_list = []
    for member in senior_executives:
        senior_executives_list.append(SeniorExecutive(member["id"], member["first_name"], member["last_name"], member["industry"], member["max_coffee_chats"], member["interests"]))

    aspiring_professionals = load_data("../data/aspiring_professional_data.json")
    aspiring_professionals_list = []
    for member in aspiring_professionals:
        aspiring_professionals_list.append(AspiringProfessional(member["id"], member["first_name"], member["last_name"], member["industry"],  member["interests"]))
    
    return senior_executives_list, aspiring_professionals_list

# Method used to get a random date in the week
def get_random_date():
    start = datetime.now()
    end = start + timedelta(days=7)
    random_date = start + (end - start) * random.random()
    random_date = random_date.strftime('%m/%d/%Y')
    return random_date

#  Method to create a dictionary that stores members with their unique ID's
#  {Senior Executive ID: Senior Executive Object}
def get_member_id(list):
    list_dict = {}
    for i in list:
        list_dict[i.get_id()] = i
    return list_dict

# Method used to print all Coffee Chat information neatly
def print_senior_executive_statistics(senior_executives_list,aspiring_professionals_list):
    senior_executive_dict = get_member_id(senior_executives_list)
    aspiring_professionals_dict = get_member_id(aspiring_professionals_list)

    final_list = []
    for i in senior_executives_list:
        format_data = []
        format_data.append(i.get_first_name())
        format_data.append(i.get_last_name())
        format_data.append(i.get_industry())
        format_data.append(i.get_frequency()) 
        format_data.append(i.get_num_coffee_chats())
        final_list.append(format_data)
    print('\n--------------------------------------------------------------------')
    print('---------- Getting This Weeks Senior Executive Statistics ----------')
    print('--------------------------------------------------------------------\n')
    print(tabulate(final_list, headers=['First Name','Last Name','Industry', 'Frequency', 'Coffee Chats']),)

# Method used to print all Coffee Chat information neatly
def print_coffee_chats(coffee_chats,senior_executives_list, aspiring_professionals_list):
    senior_executive_dict = get_member_id(senior_executives_list)
    aspiring_professionals_dict = get_member_id(aspiring_professionals_list)

    final_list = []
    for i in coffee_chats:
        format_data = []
        format_data.append(i.get_date())
        format_data.append(aspiring_professionals_dict[i.get_aspiring_professional()].get_first_name() + ' ' + aspiring_professionals_dict[i.get_aspiring_professional()].get_last_name())
        format_data.append(senior_executive_dict[i.get_senior_executive()].get_first_name() + ' ' + senior_executive_dict[i.get_senior_executive()].get_last_name())
        format_data.append(i.get_location())
        final_list.append(format_data)


    print('\n-------------------------------------------------------------------')
    print('----------------- Getting This Weeks Coffee Chats -----------------')
    print('-------------------------------------------------------------------\n')
    print(tabulate(final_list, headers=['Date','Aspiring Professional','Senior Executive', 'Location']))
    print_senior_executive_statistics(senior_executives_list,aspiring_professionals_list)

