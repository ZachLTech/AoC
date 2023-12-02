games = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red", "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red", "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]
solution = 0
for game in games:
    game = game.split(": ", maxsplit=1)
    gameid = int(''.join(filter(str.isdigit, game[0])))
    print(f"GameID = {gameid}")
    game = game[1]
    game = game.split("; ")
    gamegood = True
    lowestred = 0
    lowestblue = 0
    lowestgreen = 0
    for round in game:
        round = round.split(", ")
        print(f"Game: {gameid} Round Contains: {round}")
        coloramount = len(round)
        i = 0
        while i < coloramount:
            amount = int(''.join(filter(str.isdigit, round[i])))
            if ('red' in round[i]) == True:
                if lowestred == 0:
                    lowestred = amount
                    print(f"NEW Lowest Red: {amount}")
                if lowestred<amount:
                    lowestred = amount
                    print(f"NEW Lowest Red: {amount}")
            elif ('blue' in round[i]) == True:
                if lowestblue == 0:
                    lowestblue = amount
                    print(f"NEW Lowest Blue: {amount}")
                if lowestblue<amount:
                    lowestblue = amount
                    print(f"NEW Lowest Blue: {amount}")
            elif ('green' in round[i]) == True:
                if lowestgreen == 0:
                    lowestgreen = amount
                    print(f"NEW Lowest Green: {amount}")
                if lowestgreen<amount:
                    lowestgreen = amount
                    print(f"NEW Lowest Green: {amount}")
            i+=1
        if lowestred == 0:
            lowestred = 1
        if lowestblue == 0:
            lowestblue = 1
        if lowestgreen == 0:
            lowestgreen = 1
    gamepower = (lowestred*lowestblue*lowestgreen)
    print(f"Game {gameid}'s Power: {gamepower} : LowestRed - {lowestred} : Lowestblue - {lowestblue} : Lowestgreen - {lowestgreen}")
    solution+=(gamepower)

print(f"Solution: {solution}")
            
