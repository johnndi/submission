# Write a program to generate the Fibonacci sequence up to 100
a, b = 0, 1

while a < 100:
    print(a)
    a, b = b, a + b

print(b)