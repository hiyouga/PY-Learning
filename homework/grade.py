x = input().split()
grade = list(map(int, x))
maximum = max(grade)
maxs = []
for i in range(len(grade)):
    if grade[i] == maximum:
        maxs.append(str(i+1))

print(' '.join(maxs))
