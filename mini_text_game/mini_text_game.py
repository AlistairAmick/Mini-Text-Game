#!/usr/bin/python

from sys import argv
import random

script, name = argv

flag = 0

def usr_input():
    answer = raw_input("> ")
    return answer

def die():
    global flag

    print "Your life ends."
    print "Restart?"

    choice = usr_input()

    if choice == "yes":
        flag = 0
        start()
    else:
        exit(0)

def invalid():
    print "I'm not sure what you mean."

wall = "There is a brick wall in this direction."


# function for eating
def eat_pastry():
    global pieces_cake
    global num_cupcakes
    global num_cups
    global num_scoops
    global num_donuts

    print "What would you like to eat?"
    choice = usr_input()

    how_many = "How many would you like to eat?"

    cake = choice == 'cake' and pieces_cake > 0
    cupcake = choice == 'cupcake' and num_cupcakes > 0
    pudding = choice == 'pudding' and num_cups > 0
    icecream = choice == 'ice cream' and num_scoops > 0
    donuts = choice == 'donut' and num_donuts > 0

    if cake:
        print "You have %d pieces of cake." % pieces_cake
        print how_many

        pieces_to_eat = int(usr_input())

        pieces_enough = pieces_to_eat > 1 and pieces_cake >= pieces_to_eat
        pieces_not_enough = pieces_to_eat > 1 and pieces_cake < pieces_to_eat

        if pieces_to_eat == 1:
            print "You ate one piece of cake!"
            pieces_cake -= 1
        elif pieces_enough:
            print "You ate %d pieces of cake!" % pieces_to_eat
            pieces_cake -= pieces_to_eat
        elif pieces_not_enough:
            print "You don't have that many pieces of cake!"
        elif pieces_to_eat == 0:
            pass
        else:
            invalid()

    elif cupcake:
        print "You have %d cupcakes." % num_cupcakes
        print how_many

        cupcakes_to_eat = int(usr_input())

        cupcakes_enough = cupcakes_to_eat > 1 and num_cupcakes >= cupcakes_to_eat
        cupcakes_not_enough = cupcakes_to_eat > 1 and num_cupcakes < cupcakes_to_eat

        if cupcakes_to_eat == 1:
            print "You ate one cupcake!"
            num_cupcakes -= 1
        elif cupcakes_enough:
            print "You ate %d cupcakes!" % cupcakes_to_eat
            num_cupcakes -= cupcakes_to_eat
        elif cupcakes_not_enough:
            print "You don't have enough cupcakes!"
        elif cupcakes_to_eat == 0:
            pass
        else:
            invalid()

    elif pudding:
        print "You have %d cups of pudding." % num_cups
        print how_many

        cups_to_eat = int(usr_input())

        cups_enough = cups_to_eat > 1 and num_cups >= cups_to_eat
        cups_not_enough = cups_to_eat > 1 and num_cups < cups_to_eat

        if cups_to_eat == 1:
            print "You ate one cup of pudding!"
            num_cups -= 1
        elif cups_enough:
            print "You ate %d cups of pudding!" % cups_to_eat
            num_cups -= cups_to_eat
        elif cups_not_enough:
            print "You don't have that many cups of pudding!"
        elif cups_to_eat == 0:
            pass
        else:
            invalid()

    elif icecream:
        print "You have %d scoops of ice cream." % num_scoops
        print how_many

        scoops_to_eat = int(usr_input())

        scoops_enough = scoops_to_eat > 1 and num_scoops >= scoops_to_eat
        scoops_not_enough = scoops_to_eat > 1 and num_scoops < scoops_to_eat

        if scoops_to_eat == 1:
            print "You ate one scoop of ice cream!"
            num_scoops -= 1
        elif scoops_enough:
            print "You ate %d scoops of ice cream!" % scoops_to_eat
            num_scoops -= scoops_to_eat
        elif scoops_not_enough:
            print "You don't have that many scoops of ice cream!"
        elif scoops_to_eat == 0:
            pass
        else:
            invalid()

    elif donuts:
        print "You have %d donuts." % num_donuts
        print how_many

        donuts_to_eat = int(usr_input())

        donuts_enough = donuts_to_eat > 1 and num_donuts >= donuts_to_eat
        donuts_not_enough = donuts_to_eat > 1 and num_donuts < donuts_to_eat

        if donuts_to_eat == 1:
            print "You ate one donut!"
            num_donuts -= 1
        elif donuts_enough:
            print "You ate %d donuts!" % donuts_to_eat
            num_donuts -= donuts_to_eat
        elif donuts_not_enough:
            print "You don't have that many donuts!"
        elif donuts_to_eat == 0:
            pass
    else:
        invalid()

# HOTEL
# Hotel Upper Room / Bakery
def Hotel_Bakery():

    info = '''
    This is a bakery.
    On the counter are several different kinds of pastries.
    Behind the counter is the clerk.
    '''

    print info

    global pieces_cake
    pieces_cake = 0
    global num_cupcakes
    num_cupcakes = 0
    global num_cups
    num_cups = 0
    global num_scoops
    num_scoops = 0
    global num_donuts
    num_donuts = 0

    while True:

        choice = usr_input()

        information = choice is 'info' or choice is 'i'
        call = choice == "call clerk" or choice == "clerk"
        take = choice == "take pastry" or choice == "take pastries"
        steal = choice == "steal pastry" or choice == "steal pastries"
        buy = choice == "buy cake" or choice == "buy cakes" or choice == "buy pudding" or choice == "buy cupcake" or choice == "buy cupcake" or choice == "buy ice cream"
        eat = choice == 'eat' or choice == 'eat cake' or choice == 'eat pudding' or choice == 'eat ice cream' or choice == 'eat cupcakes'
        lobby = choice == 'leave' or choice == 'lobby' or choice == "go to basement" or choice == 'go downstairs' or choice == 'down' or choice == 'downstairs' or choice == "go down"


        if take:
            print "You have to buy them first!"
        elif call:
            call_clerk()
        elif steal:
            print "Sorry; you've been caught."
            print "You have been shot by the clerk."
            die()
        elif buy:
            print "You have to call the clerk first!"
            print "Call clerk?"
            choice = usr_input()

            if choice == 'yes':
                call_clerk()
            else:
                invalid()

        elif eat:
            eat_pastry()
        elif choice == "pastries":
            print "You have %d pastries." % bought
        elif information:
            print info

            if pieces_cake > 0:
                print "Pieces of cake: %d" % pieces_cake
            if num_cupcakes > 0:
                print "Cupcakes: %d" % num_cupcakes
            if num_cups > 0:
                print "Cups of pudding: %d" % num_cups
            if num_scoops > 0:
                print "Scoops of icecream: %d" % num_scoops
            if num_donuts > 0:
                print "Donuts: %d" % num_donuts

        elif lobby:
            Hotel_Lobby()
        else:
            invalid()

# Function for calling clerk
def call_clerk():

    global pieces_cake
    global num_cupcakes
    global num_cups
    global num_scoops
    global num_donuts

    print
    print "Clerk: Hi %s!  What can I get ya?" % name
    print """
    MENU:
    Cake
    Cupcake
    Pudding
    Ice Cream
    Donut
    """


    choice = usr_input()

    if choice == 'cake':
        print "How many pieces of %s do you want?" % choice

        choice = int(usr_input())

        if choice == 1:
            print "You bought %d piece of cake!" % choice
            pieces_cake += choice
        elif choice > 1:
            print "You bought %d pieces of cake!" % choice
            pieces_cake += choice
        else:
            invalid()

    elif choice == 'cupcake':
        print "How many %ss do you want?" % choice

        choice = int(usr_input())

        if choice == 1:
            print "You bought %d cupcake!" % choice
            num_cupcakes += choice
        elif choice > 1:
            print "You bought %d cupcakes!" % choice
            num_cupcakes += choice
        else:
            invalid()

    elif choice == 'pudding':
        print "How many cups of %s do you want?" % choice

        choice = int(usr_input())

        if choice == 1:
            print "You bought %d cup of pudding!" % choice
            num_cups += choice
        elif choice > 1:
            print "You bought %d cups of pudding!" % choice
            num_cups += choice
        else:
            invalid()

    elif choice == 'ice cream':
        print "How many scoops of %s do you want?" % choice

        choice = int(usr_input())

        if choice == 1:
            print "You bought %d scoop of icecream!" % choice
            num_scoops += choice
        elif choice > 1:
            print "You bought %d scoops of icecream!" % choice
            num_scoops += choice
        else:
            invalid()

    elif choice == 'donut':
        print "How many %ss do you want?" % choice

        choice = int(usr_input())

        if choice == 1:
            print "You bought %d donut!" % choice
            num_donuts += choice
        elif choice > 1:
            print "You bought %d donuts!" % choice
            num_donuts += choice
        else:
            invalid()

# Hotel Left Room / Sauna
def Hotel_Sauna():

    info = '''
    This is the Sauna.
    Would you like to stay?
    '''

    print info

    while True:

        choice = usr_input()

        information = choice is 'info' or choice is 'i'

        if information:
            print info
        elif choice == 'yes':
            print "How long would you like to stay?"
            time = int(raw_input("> "))
            moderate = time >= 0 and time < 60
            extended = time >= 60

            if time == 0:
                Hotel_Sauna()
            elif moderate:
                print "That was refreshing!"
                print info
            elif extended:
                print "You've stayed for quite a while!"
                print info
            else:
                invalid()

        elif choice == 'no' or choice == 'leave':
            Hotel_Lobby()
        else:
            invalid()

# Hotel Hotel Room
def Hotel_Room():

    info = '''
    You are in your hotel room.
    Would you like to take a nap?
        '''
    print info


    while True:
        choice = usr_input()

        information = choice == "info" or choice == 'i'
        hallway = choice == 'leave' or choice == "go to hallway" or choice == "leave room" or choice == "enter hallway"

        if choice == 'yes':
            print "How long would you like to sleep for?"
            time = int(raw_input("> "))
            moderate = time >= 0 and time < 60
            extended = time >= 60



            if time == 0:
                Hotel_Room()
            elif moderate:
                print "That was a nice nap!"
                print info
            elif extended:
                print "You are now well-rested!"
                print info
            else:
                invalid()

        elif choice == 'no':
            print "Alright, but there's not much else to do in this room!"
            print info
        elif hallway:
            Hotel_Hallway()
        elif information:
            print info
        else:
            invalid()

# Hotel Right Room / Hallway
def Hotel_Hallway():

    info = '''
    You are in the hotel's hallway.
    Your room is to your right.
    '''

    print info

    while True:
        choice = usr_input()

        information = choice is 'info' or choice is 'i'
        room = choice == 'right' or choice == "enter room" or choice == "go to room" or choice == "go right"
        lobby = choice == "lobby" or choice == "go to lobby" or choice == "enter lobby"

        if room:
            Hotel_Room()
        elif lobby:
            Hotel_Lobby()
        elif information:
            print info
        else:
            invalid()

# Hotel Main Room / Lobby
def Hotel_Lobby():

    info = '''
    You are in the hotel lobby.
    There are doorways to your left and right, and
    there is a staircase leading upstairs.
    '''

    print info

    while True:

        choice = usr_input()

        information = choice is 'info' or choice is 'i'
        left = choice == 'left' or choice == "go left" or choice == "enter left" or choice == "open left door" or choice == "enter sauna"
        right = choice == 'right' or choice == "go right" or choice == "enter right" or choice == "open right door" or choice == "enter hallway"
        up = choice == 'up' or choice == "go up" or choice == 'upstairs' or choice == "go upstairs" or choice == "enter upstairs" or choice == "climb staircase" or choice == "enter bakery"
        leave = choice == 'leave' or choice == "leave hotel" or choice == "leave lobby" or choice == "go outside"

        if information:
            print info
        elif left:
            Hotel_Sauna()
        elif right:
            Hotel_Hallway()
        elif up:
            Hotel_Bakery()
        elif leave:
            start()
        else:
            invalid()

# Left of Start
def Left_of_Start():

    info = '''
    The fog is very thick.  You can hardly see a few feet towards
    any direction.
    '''

    print info

    while True:

        choice = usr_input()

        information = choice is 'info' or choice is 'i'
        left = choice == 'left' or choice == 'go left'
        right = choice == 'right' or choice == 'go right'
        forward = choice == 'forward' or choice == 'go forward'
        backward = choice == 'backward' or choice == 'backwards' or choice == 'go backward' or choice == 'dive' or choice == 'enter lake'

        if information:
            print info
        elif left:
            print "You've fallen off a cliff.  The drop was quite steep, "
            print "so luckily, you fell asleep before hitting the ground, "
            print "making your death painless."

            die()
        elif right:
            start()
        elif forward:
            print wall
        elif backward:
            print "You've fallen into a lake!"
            print "You drown, but luckily, your drunkeness "
            print "dulls the pain, so your death is not too unpleasant."

            die()
        else:
            invalid()

# start
def start():
    global flag
    if flag == 0:
        info = '''
        Character: %s
        You are outside.  Before you is an entrance to a hotel.
        To your left is a path.  It's quite foggy outside.
        ''' % name
    else:
        info = '''
        You are outside.  Before you is an entrance to a hotel.
        To your left is a path.  It's quite foggy outside.
        '''

    flag = 1
    print info

    while True:

        choice = usr_input()

        information = choice is 'info' or choice is 'i'

        left = choice == 'left' or choice == "go left"
        forward = choice == 'forward' or choice == "go forward" or choice == "enter hotel" or choice == "enter lobby" or choice == 'hotel' or choice == 'enter'

        if information:
            print info
        elif left:
            Left_of_Start()
        elif forward:
            Hotel_Lobby()
        else:
            invalid()


start()
