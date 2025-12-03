def solution1(lines):
    n = 0
    for line in lines:
        tens = max(line[0:-2])
        units = max(line[line.index(tens) + 1:])
        n += int(tens + units)
    return (n)

def solution2(lines):
    n = 0
    for line in lines:
        maxjoltage = '0'
        maximum_index = -1
        for i in range(0, 12)[::-1]:
            maximum = max(line[maximum_index + 1:len(line) - i - 1])
            maximum_index += 1 + line[maximum_index + 1:len(line) - i - 1].find(maximum)
            maxjoltage += maximum
        n += int(maxjoltage)
    return (n)

with open("input.txt", "r") as f:
    lines = f.readlines()
print(solution1(lines))
print(solution2(lines))
