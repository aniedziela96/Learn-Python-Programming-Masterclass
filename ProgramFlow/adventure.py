available_exits = ["north", "south", "east", "west"]

chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose an direction: ")
    if chosen_exit.casefold() == "quit":
        print("Game over")
        break

else:
    print("Aren't you glad that you got out of there ")
    