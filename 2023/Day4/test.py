######################################################################################################
# Literally just a battleground of random code I tested to make sure what I was doing made sense lol #
######################################################################################################


#cardid = 3
#matches = 1

#copiesofcard = ["card 0: ", "card 1: ","card 2: ","card 3: ","card 4: ","card 5: ","card 6: ",]

#print((f"card {cardid+matches}") in card)
#print(copiesofcard.index(card))
#print(copiesofcard[copiesofcard.index(f"card {cardid+matches}")])#+="8"
#print(copiesofcard[copiesofcard.index(f"card {cardid+matches}")])
"""
num=0
for card in copiesofcard:
    if ((f"card {cardid+matches}") in card)==True:
        copiesofcard[num]+="8"
    num+=1

print(copiesofcard)
"""

copiesofcard = [{"card 0": 3}]

print(copiesofcard[0]["card 0"])