gamesInput = open('2023/Day2/input.txt', "r")
solution = 0

for game in gamesInput:
    game = game.split(": ", maxsplit=1)
    gameid = int(''.join(filter(str.isdigit, game[0])))
    game = game[1]
    game = game.split("; ")
    gamegood = True
    lowestred = 1
    lowestblue = 1
    lowestgreen = 1
    for round in game:
        round = round.split(", ")
        coloramount = len(round)
        i = 0
        while i < coloramount:
            amount = int(''.join(filter(str.isdigit, round[i])))
            if ('red' in round[i]) == True:
                if lowestred<amount:
                    lowestred = amount
            elif ('blue' in round[i]) == True:
                if lowestblue<amount:
                    lowestblue = amount
            elif ('green' in round[i]) == True:
                if lowestgreen<amount:
                    lowestgreen = amount
            i+=1
    solution+=(lowestred*lowestblue*lowestgreen)
print(f"Solution: {solution}")