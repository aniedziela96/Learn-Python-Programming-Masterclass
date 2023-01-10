def fizz_buzz(n: int) -> str:
    if n % 3 == 0:
        if n % 5 == 0:
            return "fizz buzz"
        else:
            return "fizz"
    elif n % 5 == 0:
        return "buzz"
    else:
        return str(n)


def play_fizz_buzz() -> str:
    """
    Play Fizz Buzz.

    :return: "congratulation" if player put their guesses correctly.
        "you loose" if player made a mistake.
    """

    for i in range(1, 101):
        if i % 2 == 1:  # computer turn
            print(fizz_buzz(i))
        else:
            player_guess = input("Your turn: ")
            if player_guess == fizz_buzz(i):
                continue
            else:
                return "you loose"

    return "congratulation"

