import random

destination = ['Gotham City', 'Asgard', 'Mars', 'Atlantis', 'Hogwarts' ]
restaurant = ['The Three Broomsticks', 'The Iceberg Lounge', 'The Mos Eisley Cantina', 'Good Burger', 'Guss Galaxy Grill']
transportation = ['The Millennium Falcon', 'TARDIS', 'Dragon', 'Broomstick', 'Hoverboard' ]
entertainment = ['Quidditch', 'Tomb Raiding', 'Time Travel', 'Mars Walk With Elon', 'Squba Diving']
user_choice = []
def destinationb():
    choice1=random.choice(destination)
    print(f'We have selected {choice1} does this sound good?')
    response= input('Enter y/n: ')
    while response == ('n'):
        choice1=random.choice(destination)
        print(f'Sorry you dont like your destination how about {choice1}?')
        response= input('Enter y/n: ')
    if response == ('y'):
        user_choice.append(choice1)
        print('Awesome! Lets move on.')


def transportationb():
    choice3=random.choice(transportation)
    print(f'We have selected {choice3} does this sound good?')
    response= input('Enter y/n: ')
    while response == ('n'):
        choice3=random.choice(transportation)
        print(f'Sorry you dont like your transportation how about {choice3}?')
        response= input('Enter y/n: ')
    if response == ('y'):
        user_choice.append(choice3)
        print('Awesome! Lets move on.')



def entertainmentb():
    choice4=random.choice(entertainment)
    print(f'We have selected {choice4} does this sound good?')
    response= input('Enter y/n: ')
    while response == ('n'):
        choice4=random.choice(entertainment)
        print(f'Sorry you dont like your entertainment how about {choice4}?')
        response= input('Enter y/n: ')
    if response == ('y'):
        user_choice.append(choice4)
        print('Awesome! Lets move on.')


def restaurantb():
    choice2=random.choice(restaurant)
    print(f'We have selected {choice2} does this sound good?')
    response= input('Enter y/n: ')
    while response == ('n'):
        choice2=random.choice(restaurant)
        print(f'Sorry you dont like your restaurant how about {choice2}?')
        response= input('Enter y/n: ')
    if response == ('y'):
        user_choice.append(choice2)
        print('Awesome! Lets move on.')
    

def final():

    print('For your amazing trip, you will be arriving in',(user_choice[0]),'by',(user_choice[1]),'were you wil spend the day with',(user_choice[2]),'and you will end the the evening dining in',(user_choice[3]),)
    confirm = input('Do you confirm this trip? Enter y/n: ')
    while confirm == ('n'):
        all()
    else :
        print('Enjoy your trip!')    

def all():
    user_choice.clear()
    destinationb()
    transportationb()
    entertainmentb()
    restaurantb()
    final()

all()
