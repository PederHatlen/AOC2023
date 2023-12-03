import regex as re

def Task1(data):
    out = []
    for l in data:
        n = re.findall("[\d]", l)
        out.append(int(''.join([n[0], n[-1]])))
    return sum(out)

def Task2(data):
    digits = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
    out = []
    for l in data:
        digitified = re.findall(f"({'|'.join(digits.keys())}|[\d])", l, overlapped=True)
        for n in range(len(digitified)):
            if digitified[n] in digits: digitified[n] = str(digits[digitified[n]])
        out.append(int(''.join([digitified[0], digitified[-1]])))
    return sum(out)

if __name__ == '__main__':
    input = open('input/Day1.txt', "r").read().split("\n")
    print(Task1(input))
    print(Task2(input))