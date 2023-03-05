n = 90058705186558569935261948496132914380077312570281980020033760044382510933070450931241348678652103772768114420567119848142360867111065753301402088676701668212035175754850951897103338079978959810673297215370534716084813732883918187890434411552463739669878295417744080700424913250020348487161014643951785502867
e = 46786465362686334917265996843779843233606992585424976481745055335468678697948774988450305612127967926533923268260412557000125153569622340353246096040604284883505587337829322949633637609180797447754513992039018904786537115087888005528547900640339270052628915440787357271345416818313808448127098885767015748889
c = 48641173720475702278690317652676924796340996697567087705119344461991930773386153198223372579328462635803653561516674380209276666328375805315553713680858906705068657158073776194628700821011001144559278784795978097710145192236347629751116534400207288736776545247409895672030976932673010818369814246455196991083

e1 = 152206992575706893484835984472544529509325440944131662631741403414037956695665533186650071476146389737020554215956181827422540843366433981607643940546405002217220286072880967331118344806315756304650248634546597784597963886656422706197757265316981889118026978865295597135470735576032282694348773714479076093197
c1 = 19560634556305755550927540610989537766715902244072312818350844104485773927537226443429404190213856361759564153804627450805880512600339869169513348929194643809859468549718922965997647689203029517135396008631050292544022651948009392475583045438153697076529266662217519588521116539517972522591294232192817502376

from Crypto.Util.number import *
assert GCD(e, e1)==1

def exgec(a, b):
    if b==0:
        return 1, 0
    x, y = exgec(b, a%b)
    return y, x-a//b*y

x, y = exgec(e, e1)
m = pow(c, x, n)
m1 = pow(c1, y, n)
m = m*m1  %n
print(long_to_bytes(m))
a = b'\x98vT2\x10\xab\xcd\xef\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00My secre'