list1: list = []
list2: list = []

with open("input", "r") as infile:
    for line in infile:
        numbers = list(map(int, line.strip().split()))
        list1.append(numbers[0])
        list1.sort()
        list2.append(numbers[1])
        list2.sort()

distance = 0
for i in range(len(list1)):
    distance += abs(list1[i] - list2[i])

print(distance)