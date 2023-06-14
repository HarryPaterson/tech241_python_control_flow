# Control Flow

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



