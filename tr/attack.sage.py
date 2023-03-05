

# This file was *autogenerated* from the file attack.sage
from sage.all_cmdline import *   # import sage library

_sage_const_147733349387696521015664992396355145811249793103958464053225389476050097503928022819269482555955365534137156079172704297584033078453033637103720972881068435459202133846880715879894340131656691631756162323422868846616160423755883726450486845175227682329583615739797782025647376042249605775433971714513081755709 = Integer(147733349387696521015664992396355145811249793103958464053225389476050097503928022819269482555955365534137156079172704297584033078453033637103720972881068435459202133846880715879894340131656691631756162323422868846616160423755883726450486845175227682329583615739797782025647376042249605775433971714513081755709); _sage_const_3 = Integer(3); _sage_const_52253817590056116368273294519761274350847193477090280916373828903718796358618956145225746496960677477661151583828604021049936963779103440560630451125137344639503705880024677345063113240530798352727432768980751992926293801206779839157443722614687126711272753610923903360818026083573711899014859313677159790039 = Integer(52253817590056116368273294519761274350847193477090280916373828903718796358618956145225746496960677477661151583828604021049936963779103440560630451125137344639503705880024677345063113240530798352727432768980751992926293801206779839157443722614687126711272753610923903360818026083573711899014859313677159790039); _sage_const_0 = Integer(0); _sage_const_8 = Integer(8); _sage_const_1 = Integer(1); _sage_const_0X11111111 = Integer(0X11111111); _sage_const_21 = Integer(21); _sage_const_448 = Integer(448); _sage_const_416 = Integer(416); _sage_const_0p99 = RealNumber('0.99'); _sage_const_2 = Integer(2)
a = b'\x98vT2\x10\xab\xcd\xef\x00\x00\x00\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00m A to B'
n = _sage_const_147733349387696521015664992396355145811249793103958464053225389476050097503928022819269482555955365534137156079172704297584033078453033637103720972881068435459202133846880715879894340131656691631756162323422868846616160423755883726450486845175227682329583615739797782025647376042249605775433971714513081755709 
e = _sage_const_3 
c = _sage_const_52253817590056116368273294519761274350847193477090280916373828903718796358618956145225746496960677477661151583828604021049936963779103440560630451125137344639503705880024677345063113240530798352727432768980751992926293801206779839157443722614687126711272753610923903360818026083573711899014859313677159790039 


from Crypto.Util.number import *

qian_zhui = a[_sage_const_0 :_sage_const_8 ]
print(qian_zhui)
q = bytes_to_long(qian_zhui)
print(hex(q))
# print(a[0:8])

## Coppersmith-howgrave
def coppersmith_howgrave(f, N, beta, m, t, R):
    delta = f.degree()
    n = delta * m + t
    
    fZ = f.change_ring(ZZ) #change the ring from Zmod(N) to ZZ
    x = fZ.parent().gen()  #make x a variable in ZZ
    f_list = [] 
    for ii in range(m):
        for j in range(delta):
            #We want them ordered that's we have N^(m-ii1) and fZ^ii
            f_list.append(((x*R)**j) * N**(m-ii) * fZ(x*R)**(ii)) #the g_{i,j}
    for ii in range(t):
        f_list.append((x*R)**ii * fZ(x*R)**m) #the h_i
        
    B = matrix(ZZ, n) # n = delta * m + t
    for ii in range(n):
        for j in range(ii+_sage_const_1 ):
            B[ii, j] = f_list[ii][j]
            
    B_lll = B.LLL(early_red = True, use_siegel = True)

    g = _sage_const_0 
    for ii in range(n):
        g += x**ii * B_lll[_sage_const_0 , ii] / R**ii
    potential_roots = g.roots()
    return potential_roots
    #return roots

P = PolynomialRing(Zmod(n), names=('x',)); (x,) = P._first_ngens(1)
X = _sage_const_0X11111111 

for i in range(_sage_const_21 ):
    m = (q<<448 ) + (i<<416 ) + x
    f = pow(m,_sage_const_3 ,n)+c
    roots = coppersmith_howgrave(f, n, _sage_const_0p99 , _sage_const_2 , _sage_const_1 , X)
    if len(roots) != _sage_const_0 :
        print(roots)
        break

