# Openning Input File
Day1File = open("2023/Day1/Day1Input.txt", "r")
#Declaring
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
# Prints answer :yay:
print(finalnum)
# Almost forgot to close
Day1File.close()