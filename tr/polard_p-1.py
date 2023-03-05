from Crypto.Util.number import *
import random
def sieve(maximum=10000):
    # In general Sieve of Sundaram, produces primes smaller
    # than (2*x + 2) for a number given number x. Since
    # we want primes smaller than maximum, we reduce maximum to half
    # This array is used to separate numbers of the form
    # i+j+2ij from others where 1 <= i <= j
    marked = [False]*(int(maximum/2)+1)

    # Main logic of Sundaram. Mark all numbers which
    # do not generate prime number by doing 2*i+1
    for i in range(1, int((math.sqrt(maximum)-1)/2)+1):
        for j in range(((i*(i+1)) << 1), (int(maximum/2)+1), (2*i+1)):
            marked[j] = True

    # Since 2 is a prime number
    primes.append(2)

    # Print other primes. Remaining primes are of the
    # form 2*i + 1 such that marked[i] is false.
    for i in range(1, int(maximum/2)):
        if (marked[i] == False):
            primes.append(2*i + 1)


def get_primorial(n):
    result = 1
    for i in range(n):
        result = result * primes[i]
    return result

primes = []
sieve()

def get_prime_factors(n):
    i = 2
    while True:
        B = get_primorial(i)
        if GCD(n, pow(2, B, n)-1) == 1:
            i = i + 1
            print(i)
        else:
            print(i)
            return GCD(n, pow(2, B, n)-1)

a = get_prime_factors(120008876536855131221255979370745233738591934188224528487535120483456214085493237482915446419599357910343450285858995374277365393767669569942204888383426461862651659865189178784473131914234181752055950431093341514138390898892413182538823693941124637301582389014479754627419560568004831093116617428970538503551)
print(a)