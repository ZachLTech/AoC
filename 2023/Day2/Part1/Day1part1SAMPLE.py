games = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red", "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red", "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]
solution = 0
for game in games:
    game = game.split(": ", maxsplit=1)
    gameid = int(''.join(filter(str.isdigit, game[0])))
    print(f"GameID = {gameid}")
    game = game[1]
    game = game.split("; ")
    gamegood = True
    for round in game:
        round = round.split(", ")
        print(f"Game: {gameid} Round Contains: {round}")
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
            else:
                print(f"Round {i} is good!")
            i+=1
    if gamegood == False:
        continue
    else:
        print(f"Adding GameID: {gameid} to Solution: {solution}")
        solution+=gameid
print(f"Solution: {solution}")
            
