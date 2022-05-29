ppp = [i for i in range(1000)]
print(id(ppp))

for i in range(10):
    pppp = [x for x in ppp]
    print(id(pppp))