name = input("What's your name? ")
age = int(input("How old are you? "))

if 18 <= age < 31:
    print("Welcome to our holiday, {}! ". format(name))
elif age < 18:
    print("I'm sorry, {} you're too young.".format(name))
else:
    print("I'm sorry, {} you're too old.".format(name))