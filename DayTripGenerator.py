import random

destination = ['Gotham City', 'Asgard', 'Mars', 'Atlantis', 'Hogwarts' ]
restaurant = ['The Three Broomsticks', 'The Iceberg Lounge', 'The Mos Eisley Cantina', 'Good Burger', 'Guss Galaxy Grill']
transportation = ['The Millennium Falcon', 'TARDIS', 'Dragon', 'Broomstick', 'Hoverboard' ]
entertainment = ['Quidditch', 'Tomb Raiding', 'Time Travel', 'Mars Walk With Elon', 'Squba Diving']
user_choice = []
def destinationb():
    choice1=random.choice(destination)
    print(f'We have selected {choice1} does this sound good?')
    user_choice.append(choice1)
    response= input('Enter y/n: ')
    while response == ('n'):
        print('Sorry you dont like your destination how about',(random.choice(destination)),)
        response= input('Enter y/n: ')
    else :
        print('Awesome! Lets move on')

destinationb()

def transportationb():
    choice3=random.choice(transportation)
    print(f'We have selected {choice3} does this sound good?')
    user_choice.append(choice3)
    response= input('Enter y/n: ')
    while response == ('n'):
        print('Sorry you dont like your transportation how about',(random.choice(transportation)),)
        response= input('Enter y/n: ')
    else :
        print('Awesome! Lets move on')

transportationb()

def entertainmentb():
    choice4=random.choice(entertainment)
    print(f'We have selected {choice4} does this sound good?') 
    user_choice.append(choice4)
    response= input('Enter y/n: ')
    while response == ('n'):
        print('Sorry you dont like your entertainment how about',(random.choice(entertainment)),)
        response= input('Enter y/n: ')
    else :
        print('Awesome! Lets move on')

entertainmentb()

def restaurantb():
    choice2=random.choice(restaurant)
    print(f'We have selected {choice2} does this sound good?')
    user_choice.append(choice2)
    response= input('Enter y/n: ')
    while response == ('n'):
        print('Sorry you dont like your restaurant how about',(random.choice(restaurant)),)
        response= input('Enter y/n: ')
    else :
        print('Awesome! Lets move on')
    
restaurantb()
 

def final():
    print('For your amazing trip, you will be arriving in',(user_choice[0]),'by',(user_choice[1]),'were you wil spend the day with',(user_choice[2]),'and you will end the the evening dining in',(user_choice[3]),)
    print(input('do you confirm this trip enter y/n: '))

final()