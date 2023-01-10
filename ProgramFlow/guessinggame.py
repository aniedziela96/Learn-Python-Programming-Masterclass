import random

highest = 1000
answer = random.randint(1,highest)
print(answer)   # TODO: remove after testing
guess = 0

print("Please guess a number between 1 and {}: ".format(highest))

while guess != answer:
    guess = int(input())
    if guess == 0:
        print("Game over")
        break
    if guess == answer:
        print("Well done, you got it ")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")


