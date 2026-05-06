"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""
card_key = {
        'A':1,
        'K':10,
        'Q':10,
        'J':10,
        '10':10,
        '9':9,
        '8':8,
        '7':7,
        '6':6,
        '5':5,
        '4':4,
        '3':3,
        '2':2,
    }

def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    
    return card_key[card]


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    v1 = card_key[card_one]
    v2 = card_key[card_two]
    
    if v1 == v2:
        return card_one, card_two
    elif v1 > v2:
        return card_one
    else:
        return card_two 


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for an upcoming ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    card_key = {
        'A':11,
        'K':10,
        'Q':10,
        'J':10,
        '10':10,
        '9':9,
        '8':8,
        '7':7,
        '6':6,
        '5':5,
        '4':4,
        '3':3,
        '2':2,
    }
    v1 = card_key[card_one]
    v2 = card_key[card_two]
    v3 = v1 + v2

    if v3 <=10:
        return 11
    else:
        return 1
    


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    if (card_one == 'A' and card_two in ['10','J','Q','K']) or (card_two == 'A' and card_one in ['10','J','Q','K']):
        return True
    
    else:
        v1 = card_key[card_one]
        v2 = card_key[card_two]
        v3 = v1 + v2

        if v3 == 21:
            return True
    
    return False

    




def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    v1 = card_key[card_one]
    v2 = card_key[card_two]
    
    if v1 == v2:
        return True
    else:
        return False



def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    if (card_one == 'A' and card_two in ['8','9','10']) or (card_two == 'A' and card_one in ['8','9','10']):
        return True
    
    else:
        v1 = card_key[card_one]
        v2 = card_key[card_two]
        v3 = v1 + v2

        if v3 in [9,10,11]:
            return True
    
    return False
