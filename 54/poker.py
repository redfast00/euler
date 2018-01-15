import sys
from collections import Counter

mapping = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
mapping.update({str(v): v for v in range(2, 10)})
suits = {'H', 'C', 'S', 'D'}

# Unneeded, this is just a special case of straight flush

# def royal_flush(hand):
#     suit = hand[0].suit
#     for card in hand[1:]:
#         if card.suit != suit:
#             return False, None
#     won = ({10,11,12,13,14} == set(map(lambda x: x.value, hand)))
#     cards = hand
#     return won, cards

def straight_flush(hand):
    suit = hand[0].suit
    for card in hand[1:]:
        if card.suit != suit:
            return False, None
    values = sorted(map(lambda x: x.value, hand))
    won = (values == [values[0] + i for i in range(5)])
    return won, hand

def four_of_a_kind(hand):
    c = Counter(map(lambda x: x.value, hand))
    value, number_of_cards = c.most_common(1)[0]
    if number_of_cards == 4:
        return True, list(filter(lambda x: x.value == value, hand))
    else:
        return False, None

def full_house(hand):
    c = Counter(map(lambda x: x.value, hand))
    three, two = c.most_common(2)
    if three[1] == 3 and two[1] == 2:
        return True, hand
    else:
        return False, None

def flush(hand):
    c = Counter(map(lambda x: x.suit, hand))
    value, number_of_cards = c.most_common(1)[0]
    if number_of_cards == 5:
        return True, hand
    else:
        return False, None

def straight(hand):
    values = sorted(map(lambda x: x.value, hand))
    won = (values == [values[0] + i for i in range(5)])
    return won, hand

def three_of_a_kind(hand):
    c = Counter(map(lambda x: x.value, hand))
    value, number_of_cards = c.most_common(1)[0]
    if number_of_cards == 3:
        return True, list(filter(lambda x: x.value == value, hand))
    else:
        return False, None

def two_pairs(hand):
    c = Counter(map(lambda x: x.value, hand))
    first_pair, second_pair = c.most_common(2)
    if first_pair[1] == 2 and second_pair[1] == 2:
        return True, list(filter(lambda x: x.value == first_pair[0] or x.value == second_pair[0], hand))
    else:
        return False, None

def one_pair(hand):
    c = Counter(map(lambda x: x.value, hand))
    value, number_of_cards = c.most_common(1)[0]
    if number_of_cards == 2:
        return True, list(filter(lambda x: x.value == value, hand))
    else:
        return False, None

def high_card(hand):
    return True, hand

def best_card(first_cards_needed, second_cards_needed, full_first_hand, full_second_hand):
    # Only selected cards
    # Inverse sort by value (so highest value first)
    for first_hand, second_hand in [(first_cards_needed, second_cards_needed), (full_first_hand, full_second_hand)]:
        first_s = sorted(first_hand, key=lambda x: -x.value)
        second_s = sorted(second_hand, key=lambda x: -x.value)
        for a, b in zip(first_s, second_s):
            if a.value != b.value:
                return 1 if a.value > b.value else 2
    raise NotImplementedError("Draw between same-valued cards")
    return 1

win_order = [straight_flush, four_of_a_kind, full_house, flush, straight, three_of_a_kind, two_pairs, one_pair, high_card]

def winner(first_hand, second_hand):
    '''Returns 1 for first player, 2 for second player'''
    for comparison_function in win_order:
        first_won, first_cards_needed = comparison_function(first_hand)
        second_won, second_cards_needed = comparison_function(second_hand)
        if first_won != second_won:
            return 1 if first_won else 2
        elif first_won and second_won:
            return best_card(first_cards_needed, second_cards_needed, first_hand, second_hand)

class Card(object):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f'{self.value}-{self.suit}'

    @classmethod
    def decode(cls, card_as_string):
        value = mapping[card_as_string[0]]
        suit = card_as_string[1]
        assert suit in suits
        return cls(value, suit)


total = 0
invtotal = 0
with open(sys.argv[1]) as infile:
    for line in infile:
        cards = line.strip().split()
        first_hand = [Card.decode(card) for card in cards[:5]]
        second_hand = [Card.decode(card) for card in cards[5:]]
        player = winner(first_hand, second_hand)
        if 1 == player:
            total += 1

print(total)
