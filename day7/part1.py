cards = '§§§§§§§§§§23456789TJQKA'


def get_hand_strength(shand):
    hand = sorted(shand, key=lambda x: shand.count(x)*100 + cards.index(x), reverse=True)
    # print(hand, shand)
    if hand.count(hand[0]) == 5: # five
        return '7'
    elif hand.count(hand[0]) == 4: # four
        return '6'
    elif hand[0] == hand[1] == hand[2] and hand[3] == hand[4]: # full house
        return '5'
    elif hand[0] == hand[1] == hand[2]: # three
        return '4'
    elif hand[0] == hand[1] and hand[2] == hand[3]: # two pair
        return '3'
    elif hand[0] == hand[1]: # one pair
        return '2'
    else: # all different
        return '1'


def get_hand_rank(shand):
    strength = get_hand_strength(shand)
    for b in shand:
        strength +=str(cards.index(b))
    return strength


with open("input.txt") as file:
    hands = [{"hand": x.split(" ")[0], "bet": int(x.split(" ")[1])} for x in file.read().split("\n") if x != ""]

# print(hands)
# print(cards)

sortedhands = sorted(hands, key=lambda x: get_hand_rank(x["hand"]))
sum = 0
for i, h in enumerate(sortedhands):
    sum += (i+1)*h["bet"]

print(sum)
