from re import L
from wcwidth import list_versions
from coffee_chat import CoffeeChat
from person import Person, AspiringProfessional, SeniorExecutive
from rooster import Rooster
from utils import *


def new_aspiring_professional(first_name, last_name,  industry, interests):
    return AspiringProfessional(first_name, last_name, industry, interests)


def new_senior_executive(first_name, last_name, industry, frequency):
    return SeniorExecutive(first_name, last_name, industry, frequency)


def new_coffee_chat(name, date, time, location, aspiring_professional, senior_executive):
    return CoffeeChat(name, date, time, location, aspiring_professional, senior_executive)


def new_rooster(upcoming, past):
    return Rooster(upcoming, past)


def str_rooster(rooster):
    # format printing of rooster
    return "Upcommings:\n" + pretty_format + rooster.str_upcoming() + "Past:\n" + pretty_format + rooster.str_past()+"\n"


def load_aspiring_professionals():
    aspirings = load_data("data/aspiring_pro.json")
    list_versions = []
    for aspiring in aspirings:
        list_versions.append(new_aspiring_professional(
            aspiring["_first_name"], aspiring["_last_name"], aspiring["_industry"], aspiring["_interests"]))
    return list_versions


def load_senior_executives():
    executives = load_data("data/senior_ex.json")
    list_versions = []
    for executive in executives:
        list_versions.append(new_senior_executive(
            executive["_first_name"], executive["_last_name"], executive["_industry"], executive["_frequency"]))
    return list_versions


def get_person_details(person_data, last_name, first_name):
    for person in person_data:
        if person.get_first_name() == first_name and person.get_last_name() == last_name:
            return person
    print("Person not found: " + first_name + " " + last_name)
    return None


def load_coffee_chats(aspiring_professionals, senior_executives):
    chats = load_data("data/coffee_chats.json")
    list_versions = []
    for chat in chats:
        list_versions.append(new_coffee_chat(chat["_name"],
                                             chat["_date"],
                                             chat["_time"],
                                             chat["_location"],
                                             get_person_details(
                                                 aspiring_professionals, chat["_aspiring_professional"].split(",")[
                                                     0],
                                                 chat["_aspiring_professional"].split(",")[1]),
                                             get_person_details(senior_executives, chat["_senior_executive"].split(",")[0],
                                                                chat["_senior_executive"].split(",")[1])))
    return list_versions


if __name__ == "__main__":
    # create a rooster
    rooster = new_rooster([], [])

    aspiring_professionals = load_aspiring_professionals()
    senior_executives = load_senior_executives()

    # load chats and add to rooster
    chats = load_coffee_chats(aspiring_professionals, senior_executives)
    for chat in chats:
        if chat.has_past():
            rooster.add_past(chat)
        else:
            rooster.add_upcoming(chat)

    print(str_rooster(rooster))
