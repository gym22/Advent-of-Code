import re


with open("day4input1.txt") as file:
    cards = list(map(lambda x: {"split_numbers": x.strip().split(":")[1].split(" |"), "copies": 1}, file))

all_points = []
card_copies = {}

for card_no, card in enumerate(cards):
    copies_of_this_card = card["copies"]
    winning_numbers_string = card["split_numbers"][0]
    my_numbers_strnig = card["split_numbers"][1]

    winning_numbers = {winning_numbers_string[start:start+3] for start in range(0, len(winning_numbers_string), 3)}
    my_numbers = {my_numbers_strnig[start:start+3] for start in range(0, len(my_numbers_strnig), 3)}
    wins = winning_numbers & my_numbers

    number_of_next_cards = len(wins)

    print(copies_of_this_card, number_of_next_cards, wins)
    for next_card in cards[card_no+1:card_no+1+number_of_next_cards]:
        next_card["copies"] += copies_of_this_card

print(sum(c["copies"] for c in cards))

# 6227972