# NOT 17002... forgot to remove \n's oops lol
# Sample Cards and solution declaration
cardpile = ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53","Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19", "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1", "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83", "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36", "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"]
solution = 0

# Loops through all the cards in le cardpile
for card in cardpile:
    # Parsing and declaring pieces of the cardpile dataset
    points = 0
    card = card.split(": ", maxsplit=1)
    cardid = int(''.join(filter(str.isdigit, card[0])))
    card = card[1].split(" | ", maxsplit=1)
    winningnumbers = card[0]
    givennumbers = card[1]
    print(f"Card: {cardid} Winning: {winningnumbers} Given: {givennumbers}")
    eachwinningnumber = winningnumbers.split(" ")
    print(f"each winning number for card {cardid}: {eachwinningnumber}")
    eachgivennumber = givennumbers.split(" ")
    print(f"each given number for card {cardid}: {eachgivennumber}")
    # Basically just goes through every given number for each winning number for this card and compares it
    for winningnumber in eachwinningnumber:
        if (winningnumber!='') == True:
            print(f"Winning number that's not '': {winningnumber}")
            for givennumber in eachgivennumber:
                if (givennumber!='') == True:
                    print(f"given number that's not '': {givennumber}")
                    if winningnumber==givennumber:
                        # Does point addition/multiplication if not the first point
                        print(f"They're the same ({winningnumber} and {givennumber})")
                        if points==0:
                            points+=1
                            print(f"added points! It's now at {points}")
                        else:
                            points = points*2
                            print(f"added points! It's now at {points}")
    print(f"card {cardid} checked! total points were {points}")
    # Adds all the points from this card to the Solution (:
    solution+=points
print(solution)