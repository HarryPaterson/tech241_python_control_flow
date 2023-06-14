# Temperature program

temperature = int(input("Please tell me what the temperature (C\N{DEGREE SIGN}) is:"))

if temperature >= 30:
    print("It's well hot. Might be too hot. Stay cool!")
elif temperature >= 20:
    print("I recommend you get outside and enjoy the weather! Don't forget your suncream")
elif temperature >= 10:
    print("I recommend a light jacket today")
elif temperature >= 0:
    print("It's a little chilly today, wrap up warm!")
else:
    print("Brrrr! Better turn the heating on")