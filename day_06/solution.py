def reader():
    lines = []
    with open('input.txt', 'r') as file:
        read_lines = file.readlines()
    for l in read_lines:
        l = list(filter(None, l.strip().split(' ')))
        lines.append(l)
    return (lines)

def solution1(lines):
    big_n = 0
    for i in range(len(lines[0])):
        n = int(lines[0][i])
        if lines[-1][i] == '*':
            for j in range(1, len(lines) - 1):
                n *= int(lines[j][i])
        elif lines[-1][i] == '+':
            for j in range(1, len(lines) - 1):
                n += int(lines[j][i])
        big_n += n
    return (big_n)

def define_sizes(line):
    d = 0
    i = 1
    sizes = []
    while i < len(line):
        if line[i] != ' ':
            sizes.append(i - d + (0 if i == len(line) - 1 else - 1))
            d = i
        i += 1
    return (sizes)

def to_cols(lines):
    sizes = define_sizes(lines[-1])
    cols = [] * (len(lines))
    for col_n in range(len(sizes)):
        col = []
        for row_n in range(len(lines)):
            col.append(lines[row_n][0:sizes[col_n]])
            lines[row_n] = lines[row_n][sizes[col_n] + 1:]
        cols.append(col)
    return (cols)

def define_operations(col):
    r = int(col[0])
    max_len = len(max(col))
    operation = [''] * (max_len + 1)

    for l in range(max_len):
        for number in col[0:-1]:
            if number[l] != ' ':
                operation[l] += number[l]
    operation[-1] = col[-1].strip()

    return operation

def calculate(operation):
    n = int(operation[0])
    for number in operation[1:-1]:
        if operation[-1] == '*':
            n *= int(number)
        else:
            n += int(number)
    return n

def solution2(lines):
    cols = to_cols(lines)
    operations = []
    n = 0
    for col in cols:
        operations.append(define_operations(col))
    for op in operations:
        n += calculate(op)
    return n

with open('input.txt', 'r') as file:
    lines = file.readlines()
print(solution1(reader()))
print(solution2(lines))
