def gcd(x,y):
    if x < y:
        x,y = y,x
    while y != 0:
        x,y = y,x%y
    return x

def get_n(path):
    '''获取n'''
    with open(path,'r') as f:
        data = f.read()
        n=(int(data[0:256],16))
    return n
n = []
for i in range(21):
    p = 'Frame'+str(i)
    n.append(get_n(p))

from itertools import combinations
for i,j in combinations(n, 2):
    tep = gcd(i, j)
    if tep != 1:
        print(n.index(i),':',i)
        print(n.index(j),':',j)
        print(tep)
        print('-----------------------------------')