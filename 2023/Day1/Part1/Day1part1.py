Day1File = open("2023/Day1/Day1Input.txt", "r")
lines = []
finalnum = "0"
for line in Day1File:
    linenochars = ''.join(filter(str.isdigit, line))
    nums = []
    for num in linenochars:
        nums.append(num)
    first = nums[0]
    last = nums[-1]
    numstogether = (first + last)
    finalnum = (int(finalnum) + int(numstogether))
print(finalnum)
Day1File.close()