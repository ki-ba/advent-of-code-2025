def get_new_pos(initial_pos, instruction):
    if (instruction[0] == 'L'):
        return (initial_pos - int(instruction[1:]))
    else:
        return (initial_pos + int(instruction[1:]))

def get_new_pos_detail(pos, instruction, n):
    n2 = n
    if (instruction[0] == 'L'):
        for i in range(int(instruction[1:])):
            pos = (pos - 1) % 100
            if pos == 0:
                n2 += 1
    elif (instruction[0] == 'R'):
        for i in range(int(instruction[1:])):
            pos = (pos + 1) % 100
            if pos == 0:
                n2 += 1
    return (pos, n2)

n = 0;
pos = 50;
file = open("input.txt", "r")
for line in file:
    pos, n = get_new_pos_detail(pos, line, n)
file.close()
print(n)
