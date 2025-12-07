class Solution:
    def __init__(self, f):
        self.split_count = 0
        self.values = dict()
        with open(f, 'r') as file:
            self.lines = file.readlines()
        self.lines = list(map(list, self.lines))
        self.fill_tachyon()
        # for l in self.lines:
        #     print(l)

    def fill_tachyon(self):
        for i in range(len(self.lines)):
            for j in range(len(self.lines[i])):
                if self.lines[i][j] == '^' and self.lines [i - 1][j] == "|":
                    self.lines[i][j - 1] = '|'
                    self.lines[i][j + 1] = '|'
                    self.split_count += 1
                elif self.lines[i - 1][j] == '|' or self.lines[i - 1][j] == 'S':
                    self.lines[i][j] = '|'

    def to_key(self, i0, j0):
        return (str(i0) + "," + str(j0))

    def count_timelines(self, padding, count, i0,j0):
        # print(padding, "on line", i0, "col", j0)

        if self.to_key(i0, j0) in self.values:
            return self.values[self.to_key(i0, j0)]

        if i0 == len(self.lines) - 1:
            # print(padding, "end of list : putting 1 at", self.to_key(i0, j0))
            self.values[self.to_key(i0,j0)] = 1
            return 1

        if self.lines[i0][j0] == '^' and self.lines[i0 - 1][j0] == '|':
            # print(padding, "split detected at ", i0, j0, ": counting from ", i0+1, j0-1)
            count2 = self.count_timelines(padding + '|', count,  i0 + 1, j0 - 1)
            # print(padding, "split detected at ", i0, j0, ": counting from ", i0+1, j0+1)
            count2 += self.count_timelines(padding + '|', count,  i0 + 1, j0 + 1)
            # print(padding, "putting value ", count2, "at", self.to_key(i0, j0))
            self.values[self.to_key(i0,j0)] = count2
            return count2
        else:
            return self.count_timelines(padding, count, i0 + 1,j0)
        return (count)

    def solve2(self):
        i0 = 1
        j0 = self.lines[i0].index('|')
        return self.count_timelines("", 0, i0, j0)

    def solve1(self):
        return (self.split_count)

sol = Solution('input.txt')
print(sol.solve1())
print(sol.solve2())
