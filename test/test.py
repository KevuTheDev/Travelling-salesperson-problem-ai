from copy import deepcopy

def lll(alist, i):
    aalist = deepcopy(alist)
    aalist.remove(i)
    print(aalist)
    for j in aalist:
        lll(aalist, j)


size = 4

aaa = [i for i in range(size)]

print(aaa)


# for i in aaa:
#     aaaa = deepcopy(aaa)
#     aaaa.remove(i)
#     print(i)
#     for j in aaaa:
#         print(j)
#     print("---")

lll(aaa, 0)



