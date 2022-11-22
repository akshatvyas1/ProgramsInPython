a, b = map(int, input().split())

# using temp operator

temp = a
a = b
b = temp

print(a,b)

#using comma operator

a, b = b, a

print(a,b)

#using arithmatic add and substraction operator

a = a + b
b = a - b
a = a - b

print(a, b)

# using XOR operator

a = a ^ b
b = a ^ b
a = a ^ b

print(a, b)

# using arithmatic multiplication and division operator

a = a * b
b = a / b
a = a / b

print(a, b)
