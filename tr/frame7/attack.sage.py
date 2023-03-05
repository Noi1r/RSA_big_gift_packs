

# This file was *autogenerated* from the file attack.sage
from sage.all_cmdline import *   # import sage library

_sage_const_155266493936043103849855199987896813716831986416707080645036022909153373110367007140301635144950634879983289720164117794783088845393686109145443728632527874768524615377182297125716276153800765906014206797548230661764274997562670900115383324605843933035314110752560290540848152237316752573471110899212429555149 = Integer(155266493936043103849855199987896813716831986416707080645036022909153373110367007140301635144950634879983289720164117794783088845393686109145443728632527874768524615377182297125716276153800765906014206797548230661764274997562670900115383324605843933035314110752560290540848152237316752573471110899212429555149); _sage_const_3 = Integer(3); _sage_const_124929943232081828105808318993257526364596580021564021377503915670544445679836588765369503919311404328043203272693851622132258819278328852726005776082575583793735570095307898828254568015886630010269615546857335790791577865565021730890364239443651479580968112031521485174068731577348690810906553798608040451024 = Integer(124929943232081828105808318993257526364596580021564021377503915670544445679836588765369503919311404328043203272693851622132258819278328852726005776082575583793735570095307898828254568015886630010269615546857335790791577865565021730890364239443651479580968112031521485174068731577348690810906553798608040451024); _sage_const_0 = Integer(0); _sage_const_8 = Integer(8); _sage_const_21 = Integer(21); _sage_const_448 = Integer(448); _sage_const_416 = Integer(416)
n = _sage_const_155266493936043103849855199987896813716831986416707080645036022909153373110367007140301635144950634879983289720164117794783088845393686109145443728632527874768524615377182297125716276153800765906014206797548230661764274997562670900115383324605843933035314110752560290540848152237316752573471110899212429555149 
e = _sage_const_3 
c = _sage_const_124929943232081828105808318993257526364596580021564021377503915670544445679836588765369503919311404328043203272693851622132258819278328852726005776082575583793735570095307898828254568015886630010269615546857335790791577865565021730890364239443651479580968112031521485174068731577348690810906553798608040451024 
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


