def is_invalid1(id):
    istr = str(id)
    return (istr[len(istr)//2:] == istr[:len(istr)//2] and len(istr) > 1)

def is_repeating(number, section_len):
    istr = str(number)
    for n_section in range(1, (len(istr) // section_len)):
        first = istr[0:section_len]
        current = istr[n_section * section_len:(n_section + 1) * (section_len)]
        if current != first:
            return False 
        elif (n_section == (len(istr) // section_len) - 1):
            return True

def is_invalid2(id):
    istr = str(id)
    for section_len in range(1, len(istr)):
        if (len(istr) % section_len == 0):
            if is_repeating(id, section_len):
                return True
    return False

def solution(ids):
    n1 = 0
    n2 = 0
    for id in ids:
        id_range = id.split('-')
        for i in range(int(id_range[0]), int(id_range[1])):
            if (is_invalid1(i)):
                n1 += i
            if (is_invalid2(i)):
                n2 += i
    return (n1, n2)


with open("input.txt", "r") as file:
    ids = file.read().split(',')
    n1, n2 = solution(ids)
    print("n1 : ", n1)
    print("n2 : ", n2)
