# Assignment: Coin Tosses
# Write a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears.
#
# Sample output should be like the following:
#
# Starting the program...
# Attempt #1: Throwing a coin... It's a head! ... Got 1 head(s) so far and 0 tail(s) so far
# Attempt #2: Throwing a coin... It's a head! ... Got 2 head(s) so far and 0 tail(s) so far
# Attempt #3: Throwing a coin... It's a tail! ... Got 2 head(s) so far and 1 tail(s) so far
# Attempt #4: Throwing a coin... It's a head! ... Got 3 head(s) so far and 1 tail(s) so far
# ...
# Attempt #5000: Throwing a coin... It's a head! ... Got 2412 head(s) so far and 2588 tail(s) so far
# Ending the program, thank you!
# Hint: Use the python built-in round function to convert that floating point number into an integer

import random

def cointoss(a):
    heads = 0
    tails = 0
    for coin in range(1,a):
        heads = 1
        tails = 1
        number = int(random.randint(1,2))
        if number == 1:
            heads += 1
            print "Attempt# " + str(coin) + " Throwing a coin...It's a heads... Got " + str(heads) + " so far an " + str(tails) + " so far"

        if number == 2:
            tails += 1
            print "Attempt# " + str(coin) + " Throwing a coin...It's a tail(s)... Got " + str(tails) + " so far an " + str(heads) + " so far"


cointoss(5001)
