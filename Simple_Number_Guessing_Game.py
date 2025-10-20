import random
list=[*range(1,101)]
number =random.choice(list)
guess=int(input("Guess a number between 1 and 100:"))

while not (number==guess) :
    if guess > number:
        print("Your guess is too big...")
    elif guess < number:
        print("Your guess is too small...")
    guess=int(input("Guess a number between 1 and 100:"))
else :
   print("Congratulations on your correct guess!")
