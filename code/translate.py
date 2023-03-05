import sys
import binascii
from Crypto.Util.number import *

# def encode_hex(s):
#     return '0X'+binascii.hexlify(s.encode()).decode()

def get_pub(path):
    '''获取公钥'''
    with open(path,'r') as f:
        data = f.read()
        n = int(data[0:256],16)
        e = int(data[256:512],16)
        c = int(data[512:768],16)
    return n,e,c        

for i in range(21):
    p = 'Frame'+str(i)
    n,e,c = get_pub(p)
    if e ==5 :
        print('Frame'+str(i))
        print('n =',n)
        print('e =',e)
        print('c =',c)
        print('-----------------------------------')
    with open('./tr/frame'+str(i)+'.txt','w+') as f:
        f.write('n = '+str(n)+'\r')
        f.write('e = '+str(e)+'\r')
        f.write('c = '+str(c)+'\r')

# def get_n(path):
#     '''获取n'''
#     with open(path,'r') as f:
#         data = f.read()
#         n=(int(data[0:256],16))
#     return n
# n = []
# for i in range(21):
#     p = 'Frame'+str(i)
#     n.append(get_n(p))

# from itertools import combinations
# for i,j in combinations(n, 2):
#     if GCD(i, j) != 1:
#         print(i)
#         print(j)
#         print(GCD(i, j))
#         print('-----------------------------------')