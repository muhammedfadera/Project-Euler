"""
In the card game poker, a hand consists of five cards and is ranked, from lowest to 
highest, in the following way:

 - High Card: Highest value card.
 - One Pair: Two cards of the same value.
 - Two Pairs: Two different pairs.
 - Three of a Kind: Three cards of the same value.
 - Straight: All cards are consecutive values.
 - Flush: All cards of the same suit.
 - Full House: Three of a kind and a pair.
 - Four of a Kind: Four cards of the same value.
 - Straight Flush: All cards are consecutive values of the same suit.
 - Royal Flush: Ten, Jack, Queen, King, Ace, in the same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; 
for example, a pair of eights beats a pair of fives. But if two ranks tie, for example, 
both players have a pair of queens, then highest cards in each hand are compared; 
if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand 1
Player 1: 5H 5C 6S 7S KD (Pair of Fives)
Player 2: 2C 3S 8S 8D TD (Pair of Eights)
Winner: Player 2

Hand 2
Player 1: 5D 8C 9S JS AC (Highest card Ace)
Player 2: 2C 5C 7D 8S QH (Highest card Queen)
Winner: Player 1

Hand 3
Player 1: 2D 9C AS AH AC (Three Aces)
Player 2: 3D 6D 7D TD QD (Flush with Diamonds)
Winner: Player 2

Hand 4
Player 1: 4D 6S 9H QH QC (Pair of Queens, Highest card Nine)
Player 2: 3D 6D 7H QD QS (Pair of Queens, Highest card Seven)
Winner: Player 1

Hand 5
Player 1: 2H 2D 4C 4D 4S (Full House with Three Fours)
Player 2: 3C 3D 3S 9S 9D (Full House with Three Threes)
Winner: Player 1

The file poker.txt contains one thousand random hands dealt to two players. 
Each line of the file contains ten cards (separated by a single space): 
the first five are Player 1's cards and the last five are Player 2's cards. 
You can assume that all hands are valid (no invalid characters or repeated cards), 
each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?



# checking if the function works
# hand1 = '5H 5C 6S 7S KD'
# hand2 = '2C 3S 8S 8D TD'
# hand1 = '5D 8C 9S JS AC'
# hand2 = '2C 5C 7D 8S QH'
# hand1 = '2D 9C AS AH AC'
# hand2 = '3D 6D 7D TD QD'
# hand1 = '4D 6S 9H QH QC'
# hand2 = '3D 6D 7H QD QS'
# hand1 = '2H 2D 4C 4D 4S'
# hand2 = '3C 3D 3S 9S 9D'
hand1 = '8C TS KC 9H 4S'
hand2 = '7D 2S 5D 3S AC'
# rank(hand1)
winner(hand1, hand2)

"""
#%%
from time import time
t1 = time()
# 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6':6, '7': 7, '8': 8, '9': 9, 
               'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}


def suit_counter(hand):
    output = dict()
    for s in ['H', 'C', 'S', 'D']:
        if s in hand:
            output[s] = hand.count(s)
    return output

def is_hand_consecutive_valued(min_value, values):
# def is_hand_consecutive_valued(hand):
    for v in range(min_value, min_value+5):
        if v not in values:
            return False
    return True
    
# ranking a hand
def rank(hand):
    S = suit_counter(hand)
    l = len(S)
    min_value = 100
    values = []
    value_counts = {}
    card_value_hist = {}
    for c in hand:
        if c in card_values:
            v = card_values[c]
            try:
                value_counts[v] += 1
            except KeyError:
                value_counts[v] = 1
            values.append(v)
            min_value = min(min_value, v)
    for v, c in value_counts.items(): 
        try:
            card_value_hist[c].append(v)
        except KeyError:
            card_value_hist[c] = [v]

    if 'T' in hand and 'J' in hand and 'Q' in hand and 'K' in hand and \
        'A' in hand and l == 1:
        return 10, card_value_hist
    elif l == 1:
        if is_hand_consecutive_valued(min_value, values):
            return 9, card_value_hist
        else:
            return 6, card_value_hist
    elif 4 in card_value_hist:
        return 8, card_value_hist
    elif 3 in card_value_hist:
        if 2 in card_value_hist:
            return 7, card_value_hist
        else:
            return 4, card_value_hist
    elif is_hand_consecutive_valued(min_value, values):
        return 5, card_value_hist
    elif 2 in card_value_hist:
        if len(card_value_hist[2]) >= 2:
            return 3, card_value_hist
        else:
            return 2, card_value_hist
    else:
        return 1, card_value_hist
    
def winner(hand1, hand2):
    r1, value_counts1 = rank(hand1)
    r2, value_counts2 = rank(hand2)
    if r1 > r2:
        return 1
    elif r1 < r2:
        return 0
    else:
        c1 = list(value_counts1.keys())
        c2 = list(value_counts2.keys())
        while len(c1) > 0 and len(c2) > 0:
            m1 = max(c1)
            m2 = max(c2)
            v1 = value_counts1[m1]
            v2 = value_counts2[m2]
            while len(v1) > 0 and len(v2) > 0:
                m11 = max(v1)
                m22 = max(v2)
                if m11 > m22:
                    return 1
                elif m11 < m22:
                    return 0
                else:
                    v1.remove(m11)
                    v2.remove(m22)
            else:
                c1.remove(m1)
                c2.remove(m2)
        # print(f"We should never reach here")
        return -1
with open("0054_poker.txt", 'r') as f:
    # game = f.readlines()
    game = f.read()
player1 = ''
player2 = ''
spaces = 0
player1_winner_counter = 0
for c in game:
    # print(c)
    if c == ' ':
        spaces += 1
        if spaces < 5:
            player1 += c
        elif spaces > 5:
            player2 += c
    elif c == '\n':
        w = winner(player1, player2)
        if w == -1:
            print(player1)
            print(player2)
            break
        else:
            player1_winner_counter += winner(player1, player2)
            player1 = ''
            player2 = ''
            spaces = 0
    elif spaces < 5:
        player1 += c
    elif spaces >= 5:
        player2 += c

print(f"Player 1 won {player1_winner_counter} times")
print(f"Time taken: {time() - t1: .2f} seconds")