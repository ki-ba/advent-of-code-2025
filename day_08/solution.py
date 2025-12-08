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
            # print("line is now ", line)
            self.circuits.append(line)
        # print(self.circuits)

    def distance(self, pointA, pointB):
        return math.sqrt((pointB[0] - pointA[0])**2 + (pointB[1] - pointA[1])**2 + (pointB[2] - pointA[2]) ** 2)

    def calculate_distances(self):
        for circuit in self.circuits: # each circuit is still supposed to be of size 1 at this point
            point = circuit[0]
            for circuit2 in self.circuits:
                if circuit2 == circuit:
                    continue
                point2 = circuit2[0]
                # print("add ",point[0],point[1],point[2],point2[0],point2[1],point2[2], "to distances with value", self.distance(point, point2))
                self.distances[point[0],point[1],point[2],point2[0],point2[1],point2[2]] = self.distance(point, point2)

    def find_closest(self):
        couple = min(self.distances, key=self.distances.get)
        # print("couple is", couple)
        revcouple = couple[3:6] + couple[0:3]
        # print("revcouple is", revcouple)
        self.distances.pop(couple)
        self.distances.pop(revcouple)
        # print(couple)
        # print("found")
        # couple = couple.split()
        pointA = (couple[0], couple[1], couple[2])
        pointB = (couple[3], couple[4], couple[5])
        # print("closest points are", pointA, "and", pointB)
        for circuit in self.circuits:
            if pointA in circuit and pointB in circuit:
                print("error :",pointA, "and", pointB, "already in same circuit")
                # print(circuit)
            elif pointA in circuit:
                # print("append", pointB, "to", circuit)
                circuit.append(pointB)
                # print(circuit)
            elif pointB in circuit:
                # print("pop")
                # print("removing", circuit[circuit.index(pointB)])
                circuit.pop(circuit.index(pointB))
                # print("trying to remove ", pointB, "from", circuit)

    def solve1(self):
        self.calculate_distances()
        for i in range(10):
            sol.find_closest()
        sizes = sorted([len(c) for c in self.circuits])[::-1]
        print(sizes)
        print("FINAL CIRCUITS")
        for circuit in sol.circuits:
            print(circuit)
        return (sizes[0] * sizes[1] * sizes[2])


sol = Solution('example.txt')


print(sol.solve1())
