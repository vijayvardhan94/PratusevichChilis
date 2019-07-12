import random
a = random.randint(1, 10)
guess = int(input("Guess your number:"))
if guess == a:
    print("you guessed exactly right!")
elif guess < a:
    print("you guessed low")
else:
    print("You guessed high")