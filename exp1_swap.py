def swap_numbers(a, b):
    return b, a

def check_number_sign(num):
    if num > 0:
        return "positive"
    elif num < 0:
        return "negative"
    else:
        return "zero"

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

num1, num2 = swap_numbers(num1, num2)

print(f"After swapping: First number = {num1}, Second number = {num2}")

result1 = check_number_sign(num1)
print(f"The first number is {result1} where first number is {num1}.")

result2 = check_number_sign(num2)
print(f"The first number is {result2} where first number is {num2}.")
