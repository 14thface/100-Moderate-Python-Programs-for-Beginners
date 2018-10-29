#Play a game with your program. Think of a card, then run the program.
#Is your card in the hand it chose?

suits = [ 'Spades', 'Diamonds', 'Clubs' ,'Hearts']
faces =['Ace','2','3','4','5','6','7','8',\
        '9','10','Jack','Queen','King']

import random
random.seed()

face = random.choice(faces)
suit = random.choice(suits)

str1 = 'The card dealt is {} of {}!' .format(face,suit)
print(str1)

def card(face_value,suit_value):
    str2 = 'The card in my hand is {} of {}!' .format(face_value,suit_value)

    if str1 == str2: #comparing strings
        print('You got lucky')
    else:
        print('Sorry.Deal Again.')

card('5','clubs')

#deal until same cards??


