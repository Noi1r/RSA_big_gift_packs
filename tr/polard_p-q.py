def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def pollard_rho(n):
    if n%2 == 0: return 2
    if is_prime(n): return n # define it somehow, e.g. return False, then it infinite loops on primes
    while True:
        c = random.randint(2, n-1)
        f = lambda x: x**2 + c 
        x = y = 2 
        d = 1 
        while d == 1:
            x = f(x) % n 
            y = f(f(y)) % n 
            d = gcd((x - y) % n, n)
        if d != n: return d
        

from random import randint
def main(n):
    pollard_rho(randint(2,n-1),1)
    return 

n= 146839643970016464813197409569004275595828791825722617066607993001682901023784267554815946189374651530288894322286859792246413142980277245909181062525398546369553995023529451396820549308690493928593324007689135648753323161394735120908960458860801743476353228970081369439513197105039143930008573928693059198131      
main(n)