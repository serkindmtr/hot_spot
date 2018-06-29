m = []

target = 1
while target != 0:
    target = int(input())
    if target != 0:
        m.append(target)
print(sum(m)/float(len(m)))

