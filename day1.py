with open('day1.txt') as f:
    cals = f.read().splitlines()
elves=[0]
i=0
while i<len(cals):
    if cals[i]=='':
        elves.append(0)
    else:
        elves[-1]+=int(cals[i])
    i+=1
print(max(elves))
a=max(elves)
elves.pop(elves.index(max(elves)))
b=max(elves)
elves.pop(elves.index(max(elves)))
c=max(elves)
print(a+b+c)
