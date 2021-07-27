
"""
Probability of Straight Flush Calculator
"""

from random import shuffle
deck = [{'value':i,'suit':c}
        for c in ['clubs','spades','hearts','diamonds']
        for i in range(1,14)]

straight_flush_no = 0
n = 1000000
for i in range(n):                                                                                          # does it n times
    shuffle(deck)                                                                                           # shuffles the deck
    if deck[0]['suit'] == deck[1]['suit'] == deck[2]['suit'] == deck[3]['suit'] == deck[4]['suit']:         # checks if all the suits are the same
        straight_flush = deck[0:5]                                                                          # if suits are the same, get first 5 cards and put them in "straight_flush"
        sorted_deck = sorted(straight_flush, key=lambda i:(i['value']))                                     # sort these 5 cards by their value
        if (sorted_deck[4]['value']-1 == sorted_deck[3]['value']) and (sorted_deck[3]['value']-1 == sorted_deck[2]['value']) and (sorted_deck[2]['value']-1 == sorted_deck[1]['value']) and (sorted_deck[1]['value']-1 == sorted_deck[0]['value']):
            straight_flush_no += 1                                                                          # if values are consecutive, add 1 to number of straight flushes



print('Probability of Straight Flush = ', straight_flush_no * 100/ n, "%") # number of straight flushes / n converted to percentage