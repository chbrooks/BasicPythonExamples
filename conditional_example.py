
## let's see how conditionals work.

value = 1

if value % 2 == 0 :
    print("value is even")

## Note that the body of the if is denoted with indentation. No braces!
## Also note the ':' - this is how we indicate the beginning of a block

if value % 2 == 0 :
    print("value is even")
else :
    print("value is odd")

## here's an else - note that the if and else are at the same depth of indentation.

name="Bob"

if (name.startswith("B")) :
    print("It's a B")
elif (name.startswith("C")) :
    print("It's a C")
elif (name.startswith("D")) :
    print("it's a D")
else :
    print("it's something else")

### in Python 3.10 and above, there's a very powerful switch statement called match

match(name) :
    case "Bob":
        print("It's Bob")
    case "Mary":
        print("It's Mary")
    case "Frank" :
        print("it's Frank")
    case _:
        print("Here's the default")

## Python uses 'and' and 'or' for conjunction and disjunction.

input = "yes"
name = "Fluff"
times = 2

if input == 'yes' and name == "Fluff" :
    print("Hello fluff")
## we can use parentheses to help organize our logic, but it's not required.
elif ((name == "no" or input="what") and (times > 2)) :
    print("got it")
