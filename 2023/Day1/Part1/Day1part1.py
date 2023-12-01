Day1File = open("Day1Input.txt", "r")

# Test Data
test = ["1abc2", "pqr3stu8vwx","a1b2c3d4e5f", "treb7uchet"]

lines = []
finalnum = "0"

# Where the magic happens (dw about my var and arr names... I'm really bad at naming things....)
# Also there're some of unnecessary print statements that were just for finding bugs
for line in Day1File:
    linenochars = ''.join(filter(str.isdigit, line))
    nums = []
    for num in linenochars:
        nums.append(num)
    first = nums[0]
    last = nums[-1]
    numstogether = (first + last)
    finalnum = (int(finalnum) + int(numstogether))
    #print(f"first: {first} last: {last} numstogether: {numstogether} finalnum: {finalnum}")

    # Code to sort each string from smallest number to largest then calculate that I made on accident without realizing and lost me time lol
    """
    orderedfinalnums = []
    maxnum = max(nums)
    minnum = min(nums)
    if nums.index(maxnum) > nums.index(minnum):
        orderedfinalnums.append(minnum)
        orderedfinalnums.append(maxnum)
    else:
        orderedfinalnums.append(maxnum)
        orderedfinalnums.append(minnum)
    print(orderedfinalnums)
    """
# Prints answer :yay:
print(finalnum)
