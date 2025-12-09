class Solution():
    def __init__(self, filename):
        with open(filename, 'r') as file:
            self.data = [tuple(map(int, line.strip().split(','))) for line in file.readlines()]
            self.area = 0
        self.row_range = dict()
        self.col_range = dict()
            # print(self.data)


    def solve1(self):
        for p1 in self.data:
            for p2 in self.data:
                area = abs((p2[0] - p1[0] + 1) * (p2[1] - p1[1] + 1))
                self.area = max(area, self.area)
        return (self.area)

    # def solve2(self):
    #     for p in self.data:
    #         for p2 in self.data:
    #             if (p2[0], p1[1]) in self.data and (p2[1], p1[0] in self.data)



        # for point in self.data:
        #     if point[0] in self.col_range:
        #         self.col_range[point[0]] =  min(self.col_range[point[0]][0], point[1]), max(self.col_range[point[0]][1], point[1])
        #     else:
        #         self.col_range[point[0]] = [point[1], point[1]]
        #     if point[1] in self.row_range:
        #         self.row_range[point[1]] =  min(self.row_range[point[1]][0], point[0]), max(self.row_range[point[1]][1], point[0])
        #     else:
        #         self.row_range[point[1]] = [point[0], point[0]]


        print(self.row_range)
        print(self.col_range)
        self.area = 0
        for p1 in self.data:
            print("considering ", p1)
            for p2 in self.data:
                print("    considering", p2)

                area = abs((p2[0] - p1[0] + 1) * (p2[1] - p1[1] + 1))
                self.area = max(self.area, area)
        return (self.area)


sol = Solution('example.txt')
print(sol.solve1())
print(sol.solve2())
