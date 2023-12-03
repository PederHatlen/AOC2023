import re, math

def Task1(input):
    maxvalues = {"red":12, "green":13, "blue":14}
    out = []
    for l in input:
        cubes = re.split(", |: |; ", l[5:])
        passed = True
        for cube in cubes[1:]:
            cube = cube.split(" ")
            if maxvalues[cube[1]] < int(cube[0]):
                passed = False
                break
        if passed: out.append(int(cubes[0]))
    return sum(out)
    
def Task2(input): 
    out = []
    for l in input:
        maxvalues = {"red":0, "green":0, "blue":0}
        cubes = [cube.split(" ") for cube in re.split(", |: |; ", l[5:])[1:]]
        for cube in cubes:
            if maxvalues[cube[1]] < int(cube[0]): maxvalues[cube[1]] = int(cube[0])
        out.append(math.prod(maxvalues.values()))
    return sum(out)

if __name__ == '__main__':
    input = open('input/Day2.txt', "r").read().split("\n")
    print(Task1(input))
    print(Task2(input))