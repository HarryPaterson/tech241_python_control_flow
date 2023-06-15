# Odds and evens program

# # Take user input
# number = int(input("Enter a number: "))
#
# # Check if the number is odd or even
# if number % 2 == 0:
#     print("The number is even!")
# else:
#     print("The number is odd!")


# Fizzbuzz program

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)