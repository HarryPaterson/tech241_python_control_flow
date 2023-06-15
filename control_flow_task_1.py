# Movie ratings program

# Take user input
age_str = input("What is your age?: ")

# Check if the age input contains only digits
if not age_str.isdigit():
    print("Please enter a valid age (digits only).")
    exit()

# Convert the age to an integer
age = int(age_str)

# Check for invalid age values then display rating
if age < 1 or age > 117:
    print("Please enter a valid age.")
else:
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

