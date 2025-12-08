import math
class Solution():
    def __init__(self, filename):
        self.circuits = []
        self.distances = dict()
        with open(filename, 'r') as file:
            lines = file.readlines()
        for line in lines:
            line = line.strip()
            line = line.split(',')
            line = tuple(map(int, line))
            line = [line]
            self.circuits.append(line)
        self.calculate_distances()

    def distance(self, pointA, pointB):
        return math.sqrt((pointB[0] - pointA[0])**2 + (pointB[1] - pointA[1])**2 + (pointB[2] - pointA[2]) ** 2)

    def calculate_distances(self):
        for circuit in self.circuits: # each circuit is still supposed to be of size 1 at this point
            point = circuit[0]
            for circuit2 in self.circuits:
                if circuit2 == circuit:
                    continue
                point2 = circuit2[0]
                self.distances[point[0],point[1],point[2],point2[0],point2[1],point2[2]] = self.distance(point, point2)

    def find_closest(self):
        couple = min(self.distances, key=self.distances.get)
        revcouple = couple[3:6] + couple[0:3]

        self.distances.pop(couple)
        self.distances.pop(revcouple)

        pointA = (couple[0], couple[1], couple[2])
        pointB = (couple[3], couple[4], couple[5])

        return (pointA, pointB)

    def get_circuit_index(self, point):
        for i in range(len(self.circuits)):
            if point in self.circuits[i]:
                return i

    def connect(self, pointA, pointB):
        index_a, index_b = self.get_circuit_index(pointA), self.get_circuit_index(pointB)
        if (index_a == index_b):
            pass
        else:
            self.circuits[index_a] += self.circuits[index_b]
            self.circuits.pop(index_b)

    def solve1(self):
        for i in range(10):
            a, b = self.find_closest()
            self.connect(a, b)
        sizes = sorted([len(c) for c in self.circuits])[::-1]
        return (sizes[0] * sizes[1] * sizes[2])

    def solve2(self):
        while len(self.circuits) > 1:
            a, b = self.find_closest()
            self.connect(a,b)
        return a[0] * b[0]

print("warning : this solution may take a while to compute for large inputs")
sol = Solution('input.txt')

print(sol.solve1())
print(sol.solve2())
