# Rabin-Miller-Composite-Checker
Below are the descriptions of three useful functions included in this code.

## checkComposite(n)
Uses the Rabin-Miller test, and 10 pre-selected witnesses, to test whether a number is composite or prime.
Returns True if n is definitively composite.
Returns False if n is prime, with estimated certainty > 1-(9.5E-7).

## checkOneWitness(n, w)
Returns True if w is a witness to n being a composite number, via the Rabin-Miller test.
Returns False if else.

## successiveSquaring(a, q, n)
Returns a^q mod n.
Uses the method of successive squaring to keep data size and run time manageable.
