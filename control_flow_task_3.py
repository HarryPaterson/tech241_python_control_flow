# Loops and lists task
# (Note: It was asked for the file to be named this but I have stuck with a numbered naming convention)

# Loop with a range to say hello 10 times
for _ in range(10):
    print("Hello!")

# Loop with a range to ask for names and append them to a list
list_names = []
for _ in range(5):
    name = input("Please enter a name: ")
    list_names.append(name)

# Loop to format names into lowercase in a new list
list_names_lower = []
for name in list_names:
    list_names_lower.append(name.lower())

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Loop to print even numbers
for num in numbers:
    if num % 2 == 0:
        print(num)

# Loop to sum all numbers from 0 to 100
total_sum = 0
for num in range(101):
    total_sum += num

print("Sum of numbers from 0 to 100:", total_sum)

# Loop to sum all odd and even numbers from 0 to 100 separately
odd_sum = 0
even_sum = 0
for num in range(101):
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

print("Sum of odd numbers from 0 to 100: " + str(odd_sum))
print("Sum of even numbers from 0 to 100:"  + str(even_sum))