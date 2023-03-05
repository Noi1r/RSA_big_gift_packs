n = 93836514358344173762895084384953633159699750987954044414830106276642828025218933012478990865656107605541657809389659063108620208004740646099662700112782252200834393363574089818787717951026690934986964275526538236750596344542450864284576226592039259070002692883820960186403938410354082341916474419847211138467

import math


#PerfectSquare = {00, e1, e4, 25, o6, e9}
def CheckPerfectSquare(num):
    #tens = 3, mean it is a odd number, tens = 4, mean it is a even number, otherwise, tens equal the value
    digitList = [   {'unit' : 0, 'tens' : 0}, 
                    {'unit' : 1, 'tens' : 4},  
                    {'unit' : 4, 'tens' : 4},  
                    {'unit' : 5, 'tens' : 2},  
                    {'unit' : 6, 'tens' : 3},  
                    {'unit' : 9, 'tens' : 4}];
    unit = num % 10
    tens = int((num % 100) / 10)
    
    for item in digitList:
        if item['unit'] == unit:
            if item['tens'] < 3:
                return item['tens'] == tens;
            else:
                #Check is odd or even number, check the first bit
                return item['tens'] & 1 == tens & 1;
    return  False;

def Fermat(num):
    x = int(math.isqrt(num));
    if x*x < num:
        x += 1;
    
    times = 0;
    x0 = x;
    while(True):
        y2 = x*x - num;
        if CheckPerfectSquare(y2):
            times += 1;
            y = int(math.sqrt(y2));
            if y*y == y2:
                break;
        x += 1;

    print( "Loop : ", x - x0 +1, ", check perfect square :", times)
    print( "x :", x, ", y :", y)
    return [x+y, x-y]

if __name__ == '__main__':
    # import libnum
    N=93836514358344173762895084384953633159699750987954044414830106276642828025218933012478990865656107605541657809389659063108620208004740646099662700112782252200834393363574089818787717951026690934986964275526538236750596344542450864284576226592039259070002692883820960186403938410354082341916474419847211138467
    p,q=Fermat(N)
    print("p:",p)
    print("q:",q)