<h1 style="text-align: center;">Control Flow</h1>

### Contents
* if, elif and else
* Loops and while loops


### if, elif and else

if: The if statement is used to check a specific condition. If the condition is True, the code block following the if statement will be executed. If the condition is False, the code block will be skipped, and the program will continue to the next section of code.

elif: The elif statement is short for "else if". It is used to check an additional condition after the if statement. If the previous if or elif conditions are False, the condition following the elif statement will be evaluated. If the elif condition is True, the code block following the elif statement will be executed. If the elif condition is False, the code block will be skipped, and the program will move on to the next section of code.

else: The else statement is used as a catch-all or fallback option. It is used when you want to execute a code block only if none of the previous if or elif conditions are True. The else statement does not have a condition associated with it. If all the preceding conditions are False, the code block following the else statement will be executed.

#### Example
```
# if and elif

# Like giving Python a recipe or an order to do things

# Conditional statements

age = int(input("What is your age?:"))

if age >= 18:
    print("You can watch all movies!")
elif age >= 15:
    print("Sorry you cannot watch 18 rated movies, but you can watch all other movies")
elif age >= 12:
    print("Sorry you cannot watch 18 or 15 rated movies, but you can watch all other movies")
elif age >= 8:
    print("Sorry you cannot watch 18,15 or 12 rated movies, but you can watch all other movies")
else:
    print("You can only watch U rated movies")

# There are no case or switch statements in Python
```

### Loops and while loops

Loops are used to repeat a block of code multiple times, allowing you to automate repetitive tasks in your program.
A while loop is a type of loop that continues executing a block of code as long as a specified condition remains True.
The loop condition is evaluated before each iteration. If the condition is True, the code block is executed. If the condition is False, the loop is terminated, and the program moves on to the next section of code.

#### Example 
```
# for loops and while loops

# for and foreach in other languages
# In Python we just use for

# list_data = [1, 2, 3, 4, 5]
# embedded_lists = [[1, 2, 3], [4,5,6]]
# dict_data = {
#     1: {"name": "Bronson", "money": "$0.05"},
#     2: {"name": "Masha", "money": "$3.66"},
#     3: {"name": "Roscoe", "money": "$1.14"}
# }

# for num in list_data:
#    print(num * 2)

# nested loops
#for data in embedded_lists:
#   print(data)
#    for num in data:
#        print(num)

# # looping through dictionaries
# for item in dict_data.values():
#     for embed_value in item.values():
#         print(embed_value)
#
# # a loop that only returns the money
# for items in dict_data.values():
#     print(items["money"])
#
# # loops and if statements
#
# for num in list_data:
#     if num == 3:
#         print("You have found three!")
#     elif num > 3:
#         print("Gone too far!")
#     else:
#         print("Too soon!")

# While loops

# x = 0
#
# while x < 10:
#     print(f"It's working -> {x}")
#     if x == 4:
#         break
#     x += 1

# Verifying user input

user_prompt =  True

while user_prompt:
    age = input("What is your age?:")
    if age.isdigit() and int(age) < 117:
        user_prompt = False
    else:
        print("Please enter your age as a digit")

print(f"Your age is {age}")
```