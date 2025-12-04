





def isRemovable(lines, i, j):
    cur_amount = 0
    if i > 0 :
        cur_amount += (1 if lines[i - 1][j] == '@' else 0)
        if j > 0:
            cur_amount += (1 if lines[i - 1][j - 1] == '@' else 0)
        if j < len(lines[0]) - 1:
            cur_amount += (1 if lines[i - 1][j + 1] == '@' else 0)
    if i < len(lines) - 1:
        cur_amount += (1 if lines[i + 1][j] == '@' else 0)
        if j > 0:
            cur_amount += (1 if lines[i + 1][j - 1] == '@' else 0)
        if j < len(lines[i]) - 1:
            cur_amount += (1 if lines[i + 1][j + 1] == '@' else 0)
    if j > 0:
        cur_amount += (1 if lines[i][j - 1] == '@' else 0)
    if j < len(lines[i]) - 1:
        cur_amount += (1 if lines[i][j + 1] == '@' else 0)
    if (cur_amount) < 4:
        return (True)
    return (False)

def remove_rolls(lines, removable_rolls):
    for i in range(0, len(lines)):
        for j in range(0, len(lines[i])):
            if (i, j) in removable_rolls:
                lines[i][j] = '.'
    return remove_rolls

def solution2(lines):
    removable_rolls = []
    rows = []
    removed = 0
    for line in lines:
        rows.append(list(line))
    while (True):
        new_removed = 0
        for i in range(0, len(lines)):
            for j in range(0, len(lines[i]) - 1):
                if rows[i][j] == '.':
                    continue
                if(isRemovable(rows, i, j)):
                    rows[i][j] = '.'
                    new_removed += 1
        if new_removed == 0:
            break
        removed += new_removed
    return removed

def solution1(lines):
    removable_rolls = 0
    for i in range(0, len(lines)):
        for j in range(0, len(lines[i]) - 1):
            if lines[i][j] == '.':
                continue
            if(isRemovable(lines, i, j)):
               removable_rolls += 1
    return removable_rolls

lines = open("input.txt", "r").readlines()
print(solution1(lines))
print(solution2(lines))
