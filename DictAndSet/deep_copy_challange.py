from contents import recipes


def my_deepcopy(d: dict) -> dict:
    """
    Copy a dictionary, creating copies of the `list` or `dict` values.

    This function will crash with an AttributeError if the values aren't
    lists or dictionaries.

    :param d: The dictionary to copy.
    :return: A copy of `d`, with the values being copies of the original values.
    """

    deep_d = {}
    for key, value in d.items():
        deep_d[key] = value.copy()

    return deep_d


recipes_copy = my_deepcopy(recipes)
recipes_copy["Butter chicken"]["ginger"] = 300
print(recipes_copy["Butter chicken"]["ginger"])
print(recipes["Butter chicken"]["ginger"])
