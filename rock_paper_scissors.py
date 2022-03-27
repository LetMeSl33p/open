# IMPORTS
import random
import time


# SETUP
instructions = '''There will be three rounds. Rock is r, Paper is p, and Scissors are s.'''
options = ['r','p','s']
user_wins = 0
comp_wins = 0

def check_against(user):
    comp_attempt = options[random.randrange(0,3)]

    if user == 'r' and comp_attempt == 's' or user == 's' and comp_attempt == 'p' or user == 'p' and comp_attempt == 'r':
        user_wins += 1
        print('You won this round.')
    elif comp_attempt == 'r' and user == 's' or comp_attempt == 's' and user == 'p' or comp_attempt == 'p' and user == 'r':
        comp_wins += 1
        print('you lost this round.')
    
    print('You have won', user_wins, 'time(s). The computer has won', comp_wins,'time(s)')

    return
    




print(instructions)

for x in range(3):
    user_attempt = input('Enter either r,p, or s.\n-    ').lower()
    check_against(user_attempt)

