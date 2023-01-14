available_parts = {'1': "computer",
                   '2': "monitor",
                   '3': "keyboard",
                   '4': "mouse",
                   '5': "hdmi cable",
                   '6': "dvd drive",
                   }

current_choice = None
computer_parts = []

while current_choice != '0':
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        if chosen_part not in computer_parts:
            print(f"Adding {chosen_part}")
            computer_parts.append(chosen_part)
        else:
            print(f"Removing: {chosen_part}")
            computer_parts.remove(chosen_part)
        print(f"Your list now contains: {computer_parts}")
    else:
        print("Please choose something from below:")
        for key, item in available_parts.items():
            print(f"{key}: {item}")
        print("0: to finish")

    current_choice = input("> ")

