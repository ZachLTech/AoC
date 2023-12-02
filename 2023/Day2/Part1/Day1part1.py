gamesInput = open('2023/Day2/input.txt', "r")
solution = 0

for game in gamesInput:
    game = game.split(": ", maxsplit=1)
    gameid = int(''.join(filter(str.isdigit, game[0])))
    game = game[1]
    game = game.split("; ")
    gamegood = True
    for round in game:
        round = round.split(", ")
        coloramount = len(round)
        i = 0
        
        while i < coloramount:
            
            amount = int(''.join(filter(str.isdigit, round[i])))
            if ('red' in round[i]) == True and amount>12:
                gamegood = False
            elif ('blue' in round[i]) == True and amount>14:
                gamegood = False
            elif ('green' in round[i]) == True and amount>13:
                gamegood = False
            i+=1
    if gamegood == False:
        continue
    else:
        solution+=gameid

print(f"Solution: {solution}")