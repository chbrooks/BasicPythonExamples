### Functions are defined using the def keyword
### unlike other languages, we do not need to provide a signature.

def computeDifference(x, y) :
    return x - y

## Again, the body of the function is indented.

## Note that the function assumes that x and y can be subtracted. If not,
## we will get a runtime error.
## This flexibility can get you into trouble, and makes it very important to
## be disciplined with testing, naming and documenting.

print(computeDifference(3,1))
#print(computeDifference(3, "blah")) ## this will generate a runtime error

## Functions can also have default arguments. This is how we provide polymorphism.

def increase(x, y=1) :
    return x + y

print(increase(3))
print(increase(3,4))

## Functions are not required to return anything.

def printStatements() :
    print("here's a line")
    print("and another")
    print("and now we're done")

## They can also return multiple values, which is pretty cool.

def modular(number, modulus) :
    quotient = number / modulus
    remainder = number % modulus
    return quotient, remainder

q, m = modular(32,5)
print("Results: %d %d" % (q,m))

## What if I only get the first value?

q = modular(32,5)
print(q) # it captures everything as a tuple.



