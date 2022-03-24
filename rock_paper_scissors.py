import random
import time

instructions = '''There will be three rounds. Rock is r, Paper is p, and Scissors are s.'''

options = ['r','p','s']


def check_against(user):
    comp_attempt = options.index(random.randrange(1,4))
    




print(instructions)

for x in range(3):
    user_attempt = input('Enter either r,p, or s.\n-    ').lower()
