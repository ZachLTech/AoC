# Each line is 140 characters long -- 10 for sample
# Both sample and input are 140 long w/ 140 lines -- 10 long w/ 10 lines)
input = open("../input.txt", "r")
solution = 0
position = 0
index = [char for char in input]
print(len(index))
for char in index:
    if char == "*":
        topleft = 0
        bottomleft = 0
        topmiddle = 0
        bottommiddle = 0
        hat = 0
        snowboard = 0
        partnumamount = 0
        gearratio = 1
        # Check Left
        if index[(position-1)].isnumeric()==True:
            partnumamount+=1
            left = 1
            if index[(position-2)].isnumeric()==True:
                left += 1
            if index[(position-3)].isnumeric()==True and index[(position-2)].isnumeric()==True:
                left += 1
            if left == 3:
                if partnumamount < 2:
                    gearratio*int(index[(position-3)]+index[(position-2)]+index[(position-1)])
            if left == 2:
                if partnumamount < 2:
                    gearratio*int(index[(position-2)]+index[(position-1)])
            if left == 1:
                if partnumamount < 2:
                    gearratio*int(index[(position-1)])
        # Check Right
        if index[(position+1)].isnumeric()==True:
            partnumamount+=1
            right = 1
            if index[(position+2)].isnumeric()==True:
                right += 1
            if index[(position+3)].isnumeric()==True and index[(position+2)].isnumeric()==True:
                right += 1
            if right == 3:
                if partnumamount < 2:
                    gearratio*int(index[(position+1)]+index[(position+2)]+index[(position+3)])
            if right == 2:
                if partnumamount < 2:
                    gearratio*int(index[(position+1)]+index[(position+2)])
            if right == 1:
                if partnumamount < 2:
                    gearratio*int(index[(position+1)])
        # Check Top Left
        if index[(position-141)].isnumeric()==True:
            partnumamount+=1
            topleft = 1
            left = 0
            right = 0
            if index[(position-140)].isnumeric()==True:
                right += 1
            if index[(position-139)].isnumeric()==True and index[(position-140)].isnumeric()==True:
                right += 1
            if index[(position-142)].isnumeric()==True:
                left += 1
            if index[(position-143)].isnumeric()==True and index[(position-142)].isnumeric()==True:
                left += 1
            if left == 0 and right == 0:
                if partnumamount < 2:
                    gearratio*int(index[(position-141)])
            if left == 0 and right == 1:
                if partnumamount < 2:
                    gearratio*int(index[(position-141)]+index[(position-140)])
                hat = 1
            if left == 0 and right == 2:
                if partnumamount < 2:
                    gearratio*int(index[(position-141)]+index[(position-140)]+index[(position-139)])
                hat = 1
            if left == 1 and right == 0:
                if partnumamount < 2:
                    gearratio*int(index[(position-142)]+index[(position-141)])
            if left == 2 and right == 0:
                if partnumamount < 2:
                    gearratio*int(index[(position-143)]+index[(position-142)]+index[(position-141)])
            if left == 1 and right == 1:
                if partnumamount < 2:
                    gearratio*int(index[(position-142)]+index[(position-141)]+index[(position-140)])
                hat = 1
        # Check Top Middle
        if index[(position-140)].isnumeric()==True and topleft!=1:
            partnumamount+=1
            topmiddle = 1
            right = 0
            if index[(position-139)].isnumeric()==True:
                right += 1
            if index[(position-138)].isnumeric()==True and index[(position-139)].isnumeric()==True:
                right += 1
                hat = 1
            if right == 0:
                if partnumamount < 2:
                    gearratio*int(index[(position-140)])
            if right == 1:
                if partnumamount < 2:
                    gearratio*int(index[(position-140)]+index[(position-139)])
            if right == 2:
                if partnumamount < 2:
                    gearratio*int(index[(position-140)]+index[(position-139)]+index[(position-138)])
        #Check Top Right
        if index[(position-139)].isnumeric()==True and topmiddle!=1 and hat!=1:
            partnumamount+=1
            right = 0
            if index[(position-138)].isnumeric()==True:
                right += 1
            if index[(position-137)].isnumeric()==True and index[(position-138)].isnumeric()==True:
                right += 1
            if right == 0:
                if partnumamount < 2:
                    gearratio*int(index[(position-139)])
            if right == 1:
                if partnumamount < 2:
                    gearratio*int(index[(position-139)]+index[(position-138)])
            if right == 2:
                if partnumamount < 2:
                    gearratio*int(index[(position-139)]+index[(position-138)]+index[(position-137)])
            
        # Check Bottom Left
        if index[(position+139)].isnumeric()==True:
            partnumamount+=1
            bottomleftleft = 1
            left = 0
            right = 0
            if index[(position+140)].isnumeric()==True:
                right += 1
            if index[(position+141)].isnumeric()==True and index[(position+140)].isnumeric()==True:
                right += 1
            if index[(position+138)].isnumeric()==True:
                left += 1
            if index[(position+138)].isnumeric()==True and index[(position+137)].isnumeric()==True:
                left += 1
            if left == 0 and right == 0:
                if partnumamount < 2:
                    gearratio*int(index[(position+139)])
            if left == 0 and right == 1:
                if partnumamount < 2:
                    gearratio*int(index[(position+139)]+index[(position+140)])
                snowboard = 1
            if left == 0 and right == 2:
                if partnumamount < 2:
                    gearratio*int(index[(position+139)]+index[(position+140)]+index[(position+141)])
                snowboard = 1
            if left == 1 and right == 0:
                if partnumamount < 2:
                    gearratio*int(index[(position+138)]+index[(position+139)])
            if left == 2 and right == 0:
                if partnumamount < 2:
                    gearratio*int(index[(position+137)]+index[(position+138)]+index[(position+139)])
            if left == 1 and right == 1:
                if partnumamount < 2:
                    gearratio*int(index[(position+138)]+index[(position+139)]+index[(position+140)])
                snowboard = 1
        # Check Bottom Middle
        if index[(position+140)].isnumeric()==True and bottomleftleft!=1:
            partnumamount+=1
            bottommiddle = 1
            right = 0
            if index[(position+141)].isnumeric()==True:
                right += 1
            if index[(position+141)].isnumeric()==True and index[(position+142)].isnumeric()==True:
                right += 1
                snowboard = 1
            if right == 0:
                if partnumamount < 2:
                    gearratio*int(index[(position+140)])
            if right == 1:
                if partnumamount < 2:
                    gearratio*int(index[(position+140)]+index[(position+141)])
            if right == 2:
                if partnumamount < 2:
                    gearratio*int(index[(position+140)]+index[(position+141)]+index[(position+142)])
        #Check Bottom Right
        if index[(position+141)].isnumeric()==True and bottommiddle!=1 and snowboard!=1:
            partnumamount+=1
            right = 0
            if index[(position+142)].isnumeric()==True:
                right += 1
            if index[(position+142)].isnumeric()==True and index[(position+143)].isnumeric()==True:
                right += 1
            if right == 0:
                if partnumamount < 2:
                    gearratio*int(index[(position+141)])
            if right == 1:
                if partnumamount < 2:
                    gearratio*int(index[(position+141)]+index[(position+142)])
            if right == 2:
                if partnumamount < 2:
                    gearratio*int(index[(position+141)]+index[(position+142)]+index[(position+143)])
        solution+=gearratio
        #print(f"pos of {char}: {position}")
    position+=1
print(f"Solution: {solution}")