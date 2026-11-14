import random

secret = random.randint(1, 10)
print("I'm thinking of a number. Can you guess what is it?")

guess = 0

while guess != secret:
  guess = int(input("Your guess: "))
  if guess == secret:
    print("Yes! You got it! My number was", secret)
  else:
    print("Nope, please try again")
