file = open('coffeeChats.txt', 'r')

dict = {}
coffee_chats = []
for line in file:
    info = line.strip().split(',')
    name = info[0]
    industry = info[1]
    appearances = info[2]
    dict[name] = {'Name': name, 'Industry': industry, 'Appearances': appearances}

aspiring_prof = input("list the aspiring professional's name : ")
aspiring_prof_industry = input("list the aspiring professional's industry : ")
for senior in dict:
    if dict[senior]["Industry"] == aspiring_prof_industry:
        coffee_chats.append(dict[senior])

print(aspiring_prof, 'can set up coffee chats with the following senior executives.', '\n' ' Their name, industry, '
                     'and how many times per week they are available are shown in the list.', '\n', coffee_chats)
