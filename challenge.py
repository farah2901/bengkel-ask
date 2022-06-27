import random

def main():
    """Start a periodic table game."""
print ("Guess the element of the noble gas!")

noblegas = [
    "helium",
    "neon",
    "argon",
    "krypton",
    "xenson",
    "radon",
    "oganesson"
     ]
x = random.choice(noblegas)
print(x)
guess = None    

while x!= guess:

    guess = str(input("What gas am I thinking of? : "))
        
    if x == guess:
        print("You guessed {}. Congratulations you got it right!".format(guess))
        break
    else:
        print("You guessed {}. Unfortunately you got the wrong answer. Please try again!".format(guess))

main()
