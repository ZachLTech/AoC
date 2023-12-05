cardpile = open('C:\\Users\\Zach\\AoC\\2023\\Day4\\input.txt', 'r')
solution = 0
for card in cardpile:
    points = 0
    card = card.split(": ", maxsplit=1)
    cardid = int(''.join(filter(str.isdigit, card[0])))
    card = card[1].split(" | ", maxsplit=1)
    winningnumbers = card[0]
    givennumbers = card[1].strip()
    eachwinningnumber = winningnumbers.split(" ")
    eachgivennumber = givennumbers.split(" ")
    for winningnumber in eachwinningnumber:
        if (winningnumber!='') == True:
            for givennumber in eachgivennumber:
                if (givennumber!='') == True:
                    if winningnumber==givennumber:
                        if points==0:
                            points+=1
                        elif points!=0:
                            points = points*2
    solution+=points
print(solution)