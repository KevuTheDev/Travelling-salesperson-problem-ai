from copy import deepcopy

ppp = [i for i in range(1000)]
print(id(ppp))

for i in range(10):
    pppp = deepcopy(ppp)
    print(id(pppp))