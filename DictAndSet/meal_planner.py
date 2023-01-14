from contents import pantry, recipes


def add_shopping_item(data: dict, item: str, amount: int) -> None:
    """Add an `item` with a `amount` to a dictionary, if the item already
    exists, increase the `amount`."""
    data[item] = data.setdefault(item, 0) + amount


# display_dict = {str(index + 1): meal for index, meal in enumerate(recipes)}
display_dict = {}
my_shopping_list = {}
for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key

while True:
    # Display a menu of the recipes we know how to cook
    print("Please choose a recipe")
    print("----------------------")
    for key, value in display_dict.items():
        print(f"{key} - {value}")

    choice = input(": ")

    if choice == '0':
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"You have selected {selected_item}")
        print("Checking ingredients ...")
        ingredients = recipes[selected_item]
        print(ingredients)
        for food_item, required_quantity in ingredients.items():
            quantity_in_pantry = pantry.get(food_item, 0)
            if required_quantity <= quantity_in_pantry:
                # print(f"\tYou have enough {food_item}")
                pass
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                add_shopping_item(my_shopping_list,
                                  food_item,
                                  quantity_to_buy)
                # print(f"\tYou need to buy {quantity_to_buy} of {food_item}")


print(f'Your shopping list: {my_shopping_list}')
