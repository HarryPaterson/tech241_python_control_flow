# Movie ratings program

# Create dictionary of ages and written form
age_dict = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
}

# Take user input
age_input = str(input("What is your age?(Please enter this as a lowercase word:"))
age_lower = age_input.lower()
age = age_dict.get(age_lower)

# Display ratings
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
