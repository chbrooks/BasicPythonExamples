## Python uses the classic while and for models of iteration.

## while uses a logical condition.

x=0
while x < 10 :
    print(x)
    x=x+1

## for iterates over a sequence - like the enhanced for loop in Java

my_list = [1,2,3,4,5]

for item in my_list :
    print(item)

## What if we want to do something a specific number of times, like in C?
## We use the 'range' method to generate a sequence.

for item in range(10) :
    print(item)

## let's start at 11
for item in range(11,20) :
    print(item)

## let's count by 2

for item in range(21,30,2) :
    print(item)