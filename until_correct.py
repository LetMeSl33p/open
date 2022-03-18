import random
import time

number = random.randrange(0,1000001)
guess = 0
guesses = 0


print('guesses, number to get, comp guess')
input('')
time_start = time.time()


while True:
    guesses += 1
    guess = 0
    guess = random.randrange(0,1000001)
    print(guesses,number,guess)
    if guess == number:
        time_end = time.time()
        print('The number',number, 'was found in',guesses,'guesses.')
        print('The time it took was:', time_end - time_start)
        break
    else:
        pass
