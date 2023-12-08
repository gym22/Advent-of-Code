cards = '§§§§§§§§§§J23456789TQKA'
five = '7'
four = '6'
fullhouse = '5'
three = '4'
two_pair = '3'
one_pair = '2'
all_different = '1'


def get_hand_strength(shand):
    hand = sorted(shand, key=lambda x: shand.count(x) * 100 + cards.index(x), reverse=True)
    # print(hand, shand)
    jokers = hand.count('J')
    if hand.count(hand[0]) == 5:  # five
        return five
    elif hand.count(hand[0]) == 4:  # four
        if jokers > 0:
            return five
        return four
    elif hand[0] == hand[1] == hand[2] and hand[3] == hand[4]:  # full house
        if jokers > 0:
            return five
        return fullhouse
    elif hand[0] == hand[1] == hand[2]:  # three
        if jokers > 0:
            return four
        return three
    elif hand[0] == hand[1] and hand[2] == hand[3]:  # two pair
        if jokers == 1:
            return fullhouse
        if jokers == 2:
            return four
        return two_pair
    elif hand[0] == hand[1]:  # one pair
        if jokers > 0:
            return three
        return one_pair
    else:  # all different
        if jokers > 0:
            return one_pair
        return all_different

def get_hand_rank(shand):
    strength = get_hand_strength(shand)

    for b in shand:
        strength += str(cards.index(b))
    return strength


with open("input.txt") as file:
    hands = [{"hand": x.split(" ")[0], "bet": int(x.split(" ")[1])} for x in file.read().split("\n") if x != ""]

# print(hands)
# print(cards)

sortedhands = sorted(hands, key=lambda x: get_hand_rank(x["hand"]))
sums = 0
for i, h in enumerate(sortedhands):
    sums += (i + 1) * h["bet"]

print(sums)
