import re

with open("day4input1.txt") as file:
    cards = [{"numbers": x.strip().split(":")[1], "copies": 1} for x in file]

all_points = []
card_copies = {}

for card_no, card in enumerate(cards):
    copies_of_this_card = card["copies"]
    winning_numbers_string, my_numbers_string = card["numbers"].split(" |")

    winning_numbers = set(re.findall(r"(\d+)", winning_numbers_string))
    my_numbers = set(re.findall(r"(\d+)", my_numbers_string))

    wins = winning_numbers & my_numbers

    number_of_next_cards = len(wins)

    print(copies_of_this_card, number_of_next_cards, wins)
    for next_card in cards[card_no + 1:card_no + 1 + number_of_next_cards]:
        next_card["copies"] += copies_of_this_card

print(sum(c["copies"] for c in cards))

# 6227972
