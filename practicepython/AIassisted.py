#Write a function that takes a string as input and returns a string where every character is doubled. For example, “hello” becomes “hheelllloo”

def double_char(s):
    return ''.join([c*2 for c in s])

print(double_char('hello')) # hheelllloo



#Write a function that given a date will tell you what day (MTWTFSS) it is on.
# For example, if the date is 1st Jan 2020, the day is Wednesday.

import datetime
def get_day(date):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return days[datetime.datetime.strptime(date, '%d %b %Y').weekday()]

print(get_day('17 Dec 2005')) 


# Write a function that takes in a matrix m and a power p and returns m raised to the p.

def matrix_power(m, p):
    return [[x**p for x in row] for row in m]

print(matrix_power([[1, 2], [3, 4]], 5)) # [[1, 4], [9, 16]]

# Write a function that generates random names.

import random
def random_name():
    names = ['John', 'Jane', 'Jack', 'Jill', 'James', 'Jenny']
    return random.choice(names)

print(random_name())

#Write a monte carlo function that calculates the odds of drawing a royal flush.

def monte_carlo(n):
    deck = ['A', 'K', 'Q', 'J', '10']
    count = 0
    for _ in range(n):
        hand = random.choices(deck, k=5)
        if all(card in hand for card in deck):
            count += 1
    return count/n

print(monte_carlo(1000000)) 

