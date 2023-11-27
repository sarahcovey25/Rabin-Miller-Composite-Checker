# The numbers to be witnesses for the Rabin-Miller algorithm.
witnesses = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

# ------------------------------------------------------------ #
# Code for calculating a^q mod n with successive squaring
# ------------------------------------------------------------ #

# returns the highest power of 2 below x
def getHighestPowerOf2(x):
    k = 0
    powK2 = 1
    while(True):
        powK2 = powK2 * 2
        if powK2 > x:
            return k
        k += 1

# returns the powers of 2 that, when summed, get q
def splitIntoPowersOf2(q):
    r = []
    while(q > 0):
        r.append(getHighestPowerOf2(q))
        q -= pow(2, r[-1])
    return r

# calculates a^q mod n with successive squaring
def successiveSquaring(a, q, n):
    q = q % n   # making sure q is positive and in simplest form
    listOfPowsToUse = splitIntoPowersOf2(q)
    listOfAllPows = [a] # list containing a^(2^k) for 0 <= k <= highestPowerOf2
    for i in range(listOfPowsToUse[0]):
        newPow = pow(listOfAllPows[-1], 2) % n
        listOfAllPows.append(newPow) # adding new power of 2 to end of list
    
    # multiply the right powers together
    product = 1
    for powInSum in listOfPowsToUse:
        product *= listOfAllPows[powInSum] # multiplying by the right power of 2 mod n
        product = product % n  # reducing mod n
    
    return product


# ------------------------------------------------------------ #
# Code for prime checking with Rabin-Miller algorithm.
# ------------------------------------------------------------ #

# returns the largest odd divisor of x, and the number of times we had to 
# factor out 2 (added to the k given)
def getQK(x, k):
    if x % 2 == 1:
        return (x, k)
    else:
        return getQK(x//2, k+1)

# returns True if w is a witness to n being a composite number, False if else
def checkOneWitness(n, w):
    q, k = getQK(n-1, 0)
    wq = successiveSquaring(w, q, n) # wq = w^q mod n
    if wq == 1 or wq == n-1: # w is not a witness if w^q == 1 mod n
        return False
    for i in range(k):   # checking all 2^i for 1 <= i <= k-1 (because we already checked 0)
        wq = (wq * wq) % n  # squaring mod n
        if wq == n-1:
            return False
    return True

# returns True if n is composite (definitively).
# returns False if it's probably prime (estimated probabibility > 1-(9.5E-7) ).
# uses the Rabin-Miller test.
def checkComposite(n):
    if n in witnesses: # n is prime if it's in our list of prime witnesses
        return False
    for w in witnesses:
        if checkOneWitness(n, w):
            return True
    return False