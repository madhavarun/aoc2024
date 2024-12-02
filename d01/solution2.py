from collections import Counter

list1: list = []
list2: list = []

with open("input", "r") as infile:
    for line in infile:
        numbers = list(map(int, line.strip().split()))
        list1.append(numbers[0])
        list2.append(numbers[1])

counter_2 = Counter(list2)

answer = 0
for number in list1:
    repetition = counter_2[number]
    answer += repetition * number

print(answer)