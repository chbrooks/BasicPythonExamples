## A big strength of python is is versatile data structures.
## The three we'll use the most are lists, tuples and dictionaries.

## A list is a mutable sequence.

names = ['luke','leia','obi-wan','vader']

for name in names :
    print(name)

names[1] = 'anakin'
print(names)

names.append("C3P0")
print(names)
print(names.pop())
print(names.pop(0))

## We can use slicing to access parts of lists.

names = ['han','leia','chewbacca','vader','obi-wan','luke','yoda']
print("Names: " + str(names))
## indices start at 0. This prints starting at 1, up through but not including 4
print(names[1:4])

## if we leave off an index, python uses the start or end.
print(names[:4])
print(names[2:])

## We can use negative indices to count from the end of the string. This is helpful
## when you want to get the last element.

print(names[-1])
print(names[3:-2])

## A tuple is an immutable sequence. Once created, they can't be modified. (this will allow them to be returned and used as keys.)

player="Steph Curry"
averages=(30.1, 4.3, 3.1)

## We can access a tuple just like a list.

print(averages[1])
print(averages[-1])
print(averages[0:2])

## We can also make nested lists and tuples.

players = ["steph","klay","draymond"]
averages = [(30.1, 4.3, 3.1), (19.2, 6.1, 4,4), (6.2, 4,4, 7,8)]

## Unlike some other languages, a sequence can contain different types of objects.

steph_summary = ["steph curry", 30, (30.1, 4.3, 3.1)]

## A dictionary is a structure that maps keys to objects. We will make very heavy use of these.

english_to_spanish = {"dog": "perro", "cat": "gato", "blue": "azul", "red": "rojo"}

print(english_to_spanish["dog"])
print(english_to_spanish["cat"])

## We can also store data structures as the value in the dictionary

warriors = {"steph" :  (30.1, 4.3, 3.1), "klay" :(19.2, 6.1, 4,4),
            "draymond" :(6.2, 4,4, 7,8) }

steph_scores = warriors['steph']
print(steph_scores)

warriors['wiggins'] = (18.2, 8.8, 4.1)

english_to_french = {'blue': 'bleu', 'cat':'chat', 'red': 'rouge','dog':'chien'}

translators = {}
translators['spanish'] = english_to_spanish
translators['french'] = english_to_french

print(translators['spanish']['dog'])
print(translators['french']['dog'])


## the key can be any immutable object. (number, string, tuple)

tic_tac_toe = {(0,0) : 'x', (0,1) : ' ', (0,2) : ' ',
                (1,0) : 'o', (1,1) : ' ', (1,2) : 'x',
                (2,0) : 'o', (2,1) : ' ', (2,2) : 'x'}

x=2
y=2
print("Cell %s, %s is %s" % (x, y, tic_tac_toe[(x,y)]))