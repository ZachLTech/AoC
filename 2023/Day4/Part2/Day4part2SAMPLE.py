# NOT 17002... forgot to remove \n's oops lol
# Sample Cards and solution declaration
cardpile = ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53","Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19", "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1", "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83", "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36", "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"]
solution = 0
# Array of dictionaries declaration for each card and how many copies each one has
cardandtotal = [{"card 0": 0}]
# Loops through 198 times to add all card instances to the cards dictionary (198 in my case) and declare them with 1 card as a starting value since there's at least 1 original card each
num=1
while num<=198:
    cardandtotal.append({f"card {num}": 1})
    num+=1
print(cardandtotal)
for card in cardpile:
    # Declaring and parsing cardpile string in prep for comparison
    points = 0
    card = card.split(": ", maxsplit=1)
    cardid = int(''.join(filter(str.isdigit, card[0])))
    card = card[1].split(" | ", maxsplit=1)
    winningnumbers = card[0]
    givennumbers = card[1].strip()
    print(f"Card: {cardid} Winning: {winningnumbers} Given: {givennumbers}")
    eachwinningnumber = winningnumbers.split(" ")
    print(f"each winning number for card {cardid}: {eachwinningnumber}")
    eachgivennumber = givennumbers.split(" ")
    print(f"each given number for card {cardid}: {eachgivennumber}")
    # Matches doesn't change and the current amount of copies is taken to have a mutable variable of the amount of copies per card in the dict array
    matches = 0
    currentamountofcopies=cardandtotal[cardid][(f"card {cardid}")]
    # Basically just goes through every given number for each winning number for this card and compares it
    for winningnumber in eachwinningnumber:
        if (winningnumber!='') == True:
            print(f"Winning number that's not '': {winningnumber}")
            for givennumber in eachgivennumber:
                if (givennumber!='') == True:
                    print(f"given number that's not '': {givennumber}")
                    # Adds match to matches in prep for copy addition
                    if winningnumber==givennumber:
                        print(f"They're the same ({winningnumber} and {givennumber})")
                        print(f"It's now made {matches} matches")
                        matches+=1
 
    # This gets a little confusing
    # Ok so this loops through an amount of times that is equal to the amount of copies present in the corresponding card dict
    # I then declared a temp matches variable to have a mutable version
    # with that I looped through and added copies to each dict following the current card for as far as the amount of matches made
    # this then looped through an amount of times that is equal to the amount of copies present in the current card dict so it would add the proper amount of copies to the right cards the appropriate amount of times
    while currentamountofcopies>0:
        matchestmp = matches
        while matchestmp>0:
            cardandtotal[cardid+matchestmp][(f"card {cardid+matchestmp}")]+=1
            matchestmp-=1
        currentamountofcopies-=1

# Since I made sure each amount of cards per card number in the dicts stayed the same, I could just loop through all the dicts in the array and add their values to the solution
cardnum = 1
# In this case it was until less than 7 since there're only 6 cards in the sample data (although it still made 198 dicts lol but I made it with the final product in mind)
while cardnum<7:
    solution+=cardandtotal[cardnum][f"card {cardnum}"]
    cardnum+=1

# Prints the final solution (:
print(solution)