line = "two1nine"

if ("nine" in line) == True:
        print("nine" in line)
        nineindex = line.index("nine")
        print(nineindex)
        line = line.replace("nine", "9")
        print(line)