from itertools import permutations

friends = ['A', 'C', 'F', 'J', 'M', 'N', 'R', 'T']
count = 0

conditions = []
for _ in range(int(input())):
    conditions.append(input())

for case in permutations(friends):
    for cond in conditions:
        others = abs(case.index(cond[0]) - case.index(cond[2])) - 1
        if cond[3] == '=' and others != int(cond[4]):
            break
        elif cond[3] == '>' and others <= int(cond[4]):
            break
        elif cond[3] == '<' and others >= int(cond[4]):
            break
    else:
        count += 1

print(count)
