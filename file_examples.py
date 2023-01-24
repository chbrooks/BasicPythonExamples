### Python is great with files. Here's how to open a file and read each line one at atime.

f = open("number_examples.py")
for line in f.readlines() :
    if len(line) > 0 :
        print(line)
f.close()

## That's fine, but having to close the file by hand is irritating, so usually we do:

with open("number_examples.py") as f :
    for line in f.readlines():
        if len(line) > 0:
            print(line)

## Now f is automatically closed and cleaned up when we're done with the file

## readlines consumes the entire file and gives it to us as a list, with each line as an element.

## If we want the file as one big string, we do: f.read()

## We can also read lines individually with readline() but that's much slower.

## To write, open the file with 'w', as in C or Java

with open("outputfile", 'w') as f2 :
    f2.write("output!!")



