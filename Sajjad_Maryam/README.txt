This algorithm is created using the feature of file I/O. This file contains information about the name of the Senior Executive, the industry they are a part of, and how many times per week they are appear in the roster. Using this information, and information entered about the Aspiring Professional by the user (you), a list is created showing which Senior Executives the Aspiring Professional can be matched with for a coffee chat. It also includes how many times per week the Senior Executive is available for a chat.

The algorithm is quite simple. It opens the file with every Senior Executives information and it separates the entries on each line and organizes the information into a dictionary with each entry labelled. 

Then, a prompt shows up on the screen, asking the user to enter the name of an Aspiring Professional and the industry they are entering.

Next, I match the Aspiring Professional's industry with every Senior Executive in the file that is also in the same industry. After getting the matches, I put the information of these Senior Executives in a new list, showing the user who the Aspiring Professional is able to have a coffee chat with. 

I ran three test cases for Aspiring Professionals in different industries. Here is what the output looked like for each case: 

test case # 1 output:

list the aspiring professional's name : Hinata Hyuga
list the aspiring professional's industry : Engineering
Hinata Hyuga can set up coffee chats with the following senior executives. 
 Their name, industry, and how many times per week they are available are shown in the list. 
 [{'Name': 'Naruto Uzumaki', 'Industry': 'Engineering', 'Appearances': ' 3'}, {'Name': 'Rock Lee', 'Industry': 'Engineering', 'Appearances': ' 4'}, {'Name': 'Kole Sanderson', 'Industry': 'Engineering', 'Appearances': ' 3'}, {'Name': 'Elisha Fischer', 'Industry': 'Engineering', 'Appearances': ' 6'}]

test case #2 output: 

list the aspiring professional's name : Maryam Sajjad
list the aspiring professional's industry : Technology
Maryam Sajjad can set up coffee chats with the following senior executives. 
 Their name, industry, and how many times per week they are available are shown in the list. 
 [{'Name': 'Shikamaro Nara', 'Industry': 'Technology', 'Appearances': ' 1'}, {'Name': 'Willem Xiong', 'Industry': 'Technology', 'Appearances': ' 5'}, {'Name': 'Mark Zuckerburg', 'Industry': 'Technology', 'Appearances': ' 2'}]

test case #3 output:

list the aspiring professional's name : Darry Data
list the aspiring professional's industry : Health Care
Darry Data can set up coffee chats with the following senior executives. 
 Their name, industry, and how many times per week they are available are shown in the list. 
 [{'Name': 'Cassia Sheridan', 'Industry': 'Health Care', 'Appearances': ' 5'}, {'Name': 'Louisa Craig', 'Industry': 'Health Care', 'Appearances': ' 4'}]

You can also test this code by running it in your IDE, and giving input to the console as shown above. I will include the coffeeChats.txt file so you can use file I/O to run the code successfully. 