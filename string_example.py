
### python is very good at working with strings.

message = "Hello world"

message2 = 'this string has single quotes bounding it   '

print(message)

print(message.lower())
print(message.upper())
print(message2.capitalize())

## a string can be indexed just like a list or array

print(message[3])

## We can slice it, just like a list.

print(message[3:7])
print(message[-1])
print(message[3:])
print(message[:6])
print(message[:-3])

## We concatenate with '+'

print(message + " " + message2)