# Write a program that takes an integer as input and returns an integer with reversed digit 
# ordering
def reverse_integer(n):
    if n == 0:
        return 0

    reversed_num = 0
    abs_num = abs(n)  # Store the absolute value of n
    while abs_num != 0:
        digit = abs_num % 10
        reversed_num = reversed_num * 10 + digit
        abs_num //= 10

    # Handling single-digit numbers
    if abs(n) < 10:
        reversed_num *= 10

    return reversed_num * (-1 if n < 0 else 1)

num = int(input("Enter an integer: "))
reversed_num = reverse_integer(num)

print(f"The reversed integer is: {reversed_num}")

