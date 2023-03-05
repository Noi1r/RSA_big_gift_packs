n = 90267480939368160749458049207367083180407266027531212674879245323647502822038591438536367206422215464489854541063867946215243190345476874546091188408120551902573113507876754578290674792643018845798263156849027209440979746485414654160320058352559498237296080490768064578067282805498131582552189186085941328701
e = 5
c = 44374979291120575503988741531987454898919254880086464254904878064332010355432423956182135846738023874326776872139229379943321321362822522900479438294291206287205647145759972233097276253408812699557305314344220807356024994977399840843758750494467535572805794732065369887057841293267499209427585419962565568495
a = b'\x98vT2\x10\xab\xcd\xef\x00\x00\x00\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00m A to B'

from Crypto.Util.number import long_to_bytes,bytes_to_long
qian_zhui = a[0 :8 ]
# print(qian_zhui)
q = bytes_to_long(qian_zhui)

P.<x>=PolynomialRing(Zmod(n))
for i in range(21):
    try:
        m = (q<<448 ) + (i<<416 ) + x
        f = m^e - c
        r = f.small_roots()
        print(r)
        print(long_to_bytes(r[0]))
    except:
        continue
