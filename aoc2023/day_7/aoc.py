from functools import reduce

values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
values_2 = ['J', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
possible_hands = [(1, 1, 1, 1, 1), (1, 1, 1, 2), (1, 2, 2), (1,1,3), (2, 3), (1,4), (5,)]


def handle_part_1(lines: list[str]) -> int:
    hands = []
    bids = {}

    for line in lines:
        [hand, bid] = line.split(" ")
        bids[hand] = bid

        t = {}
        for card in hand:
            if card not in t:
                t[card] = 1
            else:
                t[card] += 1

        hands.append((tuple(sorted(t.values())), hand))
    sort(hands, values)
    s = 0
    for i, hand in enumerate(hands):
        s += (int(bids[hand[1]]) * (i + 1))

    return s



def handle_part_2(lines: list[str]) -> int:
    hands = []
    bids = {}

    for line in lines:
        [hand, bid] = line.split(" ")
        bids[hand] = bid

        # look at the number of each Card
        t = {}
        for card in hand:
            if card not in t:
                t[card] = 1
            else:
                t[card] += 1

        # if J is in the hand and is not alone, we can use J to replace another card
        if 'J' in t and len(t) > 1:
            # search for the card which is the most represented
            [m, _] = reduce(lambda t, v : [v[0], v[1]] if v[0] != 'J' and v[1] > t[1] else t, t.items(), ['', 0])

            # for the one that has the most, add the number of Js
            t[m] += t['J']
            t.pop('J')

        hands.append((tuple(sorted(t.values())), hand))

    sort(hands, values_2)
    s = 0
    for i, hand in enumerate(hands):
        s += (int(bids[hand[1]]) * (i + 1))

    return s



# hands = (...numbers of each different card (from possible_hands), hand)[]
def sort(hands, card_values): # bubble sort on hands with a specific comparison function
    n = len(hands)
    for i in range(n):
        swapped = False

        for j in range(0, n-i-1):
            if compare_hands(hands[j], hands[j+1], card_values) > 0:
                hands[j], hands[j+1] = hands[j+1], hands[j]
                swapped = True
        if not swapped:
            break


# h1/h2 of form ((...numbers of each different cards (from possible_hands)), hand)
def compare_hands(h1, h2, card_values):
    if possible_hands.index(h1[0]) != possible_hands.index(h2[0]):
        return possible_hands.index(h1[0]) - possible_hands.index(h2[0])

    for i in range(len(h1[1])):
        if card_values.index(h1[1][i]) == card_values.index(h2[1][i]):
            continue
        return card_values.index(h1[1][i]) - card_values.index(h2[1][i])

    return 0
