

# This file was *autogenerated* from the file attack.sage
from sage.all_cmdline import *   # import sage library

_sage_const_92270627783020341903769877272635163757611737252302329401876135487358785338853904185572496782685853218459404423868889360808646192858060332110830962463986164014331540336037718684606223893506327126112739408023014900003600028654929488487584130630596342720833061628867179840913592694993869009133576053124769728363 = Integer(92270627783020341903769877272635163757611737252302329401876135487358785338853904185572496782685853218459404423868889360808646192858060332110830962463986164014331540336037718684606223893506327126112739408023014900003600028654929488487584130630596342720833061628867179840913592694993869009133576053124769728363); _sage_const_5 = Integer(5); _sage_const_83421434286602546493364204139182949897795123160498680670964040331447569764445309937195566103281638928183742488663157138572020817924561990979723444797045375101801354862472761507421896454904818874439231990567738173059815647539737800523632262742398190575822391771655932895657208471832891505814792263361394479317 = Integer(83421434286602546493364204139182949897795123160498680670964040331447569764445309937195566103281638928183742488663157138572020817924561990979723444797045375101801354862472761507421896454904818874439231990567738173059815647539737800523632262742398190575822391771655932895657208471832891505814792263361394479317); _sage_const_0 = Integer(0); _sage_const_8 = Integer(8); _sage_const_21 = Integer(21); _sage_const_448 = Integer(448); _sage_const_416 = Integer(416)
n = _sage_const_92270627783020341903769877272635163757611737252302329401876135487358785338853904185572496782685853218459404423868889360808646192858060332110830962463986164014331540336037718684606223893506327126112739408023014900003600028654929488487584130630596342720833061628867179840913592694993869009133576053124769728363 
e = _sage_const_5 
c = _sage_const_83421434286602546493364204139182949897795123160498680670964040331447569764445309937195566103281638928183742488663157138572020817924561990979723444797045375101801354862472761507421896454904818874439231990567738173059815647539737800523632262742398190575822391771655932895657208471832891505814792263361394479317 
a = b'\x98vT2\x10\xab\xcd\xef\x00\x00\x00\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00m A to B'

from Crypto.Util.number import long_to_bytes,bytes_to_long
qian_zhui = a[_sage_const_0  :_sage_const_8  ]
# print(qian_zhui)
q = bytes_to_long(qian_zhui)

P = PolynomialRing(Zmod(n), names=('x',)); (x,) = P._first_ngens(1)
for i in range(_sage_const_21 ):
    try:
        m = (q<<_sage_const_448  ) + (i<<_sage_const_416  ) + x
        f = m**e - c
        r = f.small_roots()
        print(i,r)
        print(long_to_bytes(r[_sage_const_0 ]))
    except:
        continue

