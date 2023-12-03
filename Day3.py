import re

def getAreaAround(input, line, start, end, depthX, depthY):
    return [s[max(0, start-depthX):min(end+depthX, len(s))] for s in input[max(0, line-depthY):min(line+depthY+1, len(input))]]

def Task1(input):
    out = []
    for i in range(len(input)):
        line = input[i]
        for snum in re.finditer("[\d]+", line):
            adjacent = "".join(getAreaAround(input, i, snum.start(0), snum.end(0), 1, 1))
            if re.search("[^\d.]", adjacent): out.append(int(snum.group(0)))
    return sum(out)

def Task2(input):
    out = []
    for i in range(len(input)):
        line = input[i]
        for gear in re.finditer("[*]", line):
            ratio = 1
            snums = 0
            # Adding an extra , to seperate numbers on newlines, max number length was 3, no need for wider
            gearAdjacent = ",".join(getAreaAround(input, i, gear.start(0), gear.end(0), 3, 1))
            for snum in re.finditer("[\d]+", gearAdjacent):
                # Example: ....755,.$.*...,64.598.
                # If number exists somewhere between 2 and 5 (the star) -> counted.
                if 2 < snum.end(0)%8 and snum.start(0)%8 < 5:
                    ratio *= int(snum.group(0))
                    snums += 1
            if snums == 2: out.append(ratio)
    return sum(out)

if __name__ == '__main__':
    input = open('input/Day3.txt', "r").read().split("\n")
    print(Task1(input))
    print(Task2(input))