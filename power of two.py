# Write a program that takes an integer as input and returns true if the input is a power of two
def is_power_of_two(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0

number = int(input("Enter an integer: "))
print(is_power_of_two(number))
