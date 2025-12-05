# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kbarru <kbarru@student.42lyon.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/05 10:44:10 by kbarru            #+#    #+#              #
#    Updated: 2025/12/05 11:04:22 by kbarru           ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #




def reader(filename):
    with open(filename, 'r') as file:
        for line in file:
            if line == "\n":
                continue
            elif line.find("-") == -1:
                ids.append(int(line.strip()))
            else:
                line = line.strip().split('-')
                line = map(int, line)
                valids.append(list(line))
    return (valids, ids)

def solution1(valids, ids):
    n = 0
    for id in ids:
        for valid_range in valids:
            if id > valid_range[0] and id <= valid_range[1]:
                n += 1
                break
    return(n)

def solution2(valids):
    sorted_ranges = sorted(valids, key=lambda range : range[0]) # sort by minimums
    for i in range(len(sorted_ranges) - 2):
        while len(sorted_ranges) - 1 > i and sorted_ranges[i][1] >= sorted_ranges[i + 1][0]:
            if (sorted_ranges[i][1] < sorted_ranges[i + 1][1]):
                sorted_ranges[i][1] = sorted_ranges[i + 1][1]
            sorted_ranges.pop(i + 1)
    n = 0
    for r in sorted_ranges:
        n += r[1] - r[0] + 1
    return(n)

valids = []
ids = []
valids, ids = reader("input.txt")
print(solution1(valids, ids))
print(solution2(valids))
