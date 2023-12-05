cardpile = open("C:\\Users\\Zach\\AoC\\2023\\Day4\\input.txt", "r")
solution = 0
copiesofcard = [{"card 0": 0}]
num=1
while num<=198:
    copiesofcard.append({f"card {num}": 1})
    num+=1
for card in cardpile:
    points = 0
    card = card.split(": ", maxsplit=1)
    cardid = int(''.join(filter(str.isdigit, card[0])))
    card = card[1].split(" | ", maxsplit=1)
    winningnumbers = card[0]
    givennumbers = card[1].strip()
    eachwinningnumber = winningnumbers.split(" ")
    eachgivennumber = givennumbers.split(" ")
    matches = 0
    currentamountofcopies=copiesofcard[cardid][(f"card {cardid}")]
    for winningnumber in eachwinningnumber:
        if (winningnumber!='') == True:
            for givennumber in eachgivennumber:
                if (givennumber!='') == True:
                    if winningnumber==givennumber:
                        matches+=1
    while currentamountofcopies>0:
        matchestmp = matches
        while matchestmp>0:
            copiesofcard[cardid+matchestmp][(f"card {cardid+matchestmp}")]+=1
            matchestmp-=1
        currentamountofcopies-=1
cardnum = 1
while cardnum<199:
    solution+=copiesofcard[cardnum][f"card {cardnum}"]
    cardnum+=1
print(solution)