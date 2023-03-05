import random


def gcd(m, n):

    if m < n:
        m, n = n, m
    while m % n != 0:
        m, n = n, m % n
    return n


def sieve(n):
    mpfs = [0] * (n + 1)
    pn = []
    for i in range(2, n + 1):
        mpf = mpfs[i]
        if mpf == 0:
            pn.append(i)
            mpf = i
        for p in pn:
            if p > mpf:
                break
            x = p * i
            if x > n:
                break
            mpfs[x] = p
    return pn


def pollard(n):
    b = 10_0000
    while b <= 100_0000:
        a = random.randint(2, n - 1)
        g = gcd(a, n)
        if g > 1:
            return g, n // g
        for p in sieve(b):
            if p >= b:
                continue
            p_power = 1
            while p_power * p <= b:
                p_power *= p
            g = gcd(p_power - 1, n)
            if g > 1 and g < n:
                return g, n // g
        b <<= 1
    return 1, n

def factor(n):
    factors = []
    stack = [n]
    while len(stack) > 0:
        x = stack.pop()
        if x == 2:
            factors.insert(0, x)
            continue
        p, q = pollard(x) if x & 1 == 1 else (2, x >> 1)
        if p == 1:
            factors.insert(0, q)
        else:
            stack.append(p)
            stack.append(q)
    return factors


if __name__ == '__main__':
    print(factor(94154993593274109828418786834159728190797445711539243887409583756844882924221269576486611543668906670821879426307992404721925623741478677756083992902711765865503466687919799394258306574702184666207180530598057989884729154273423032471322027993848437082723045300784582836897839491321003685598931080456249945287))