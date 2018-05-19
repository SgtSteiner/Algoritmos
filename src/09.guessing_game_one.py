import random

num_random = random.randint(0, 9)
attempts = 0
while True:
    attempts += 1
    guess = input("Enter a number (0-9): ")

    if guess == "exit":
        break
    elif int(guess) > num_random:
        print("Too high\n")
    elif int(guess) < num_random:
        print("Too low\n")
    else:
        print("Exactly right! You have succeeded in {} attempts".format(attempts))
        break
