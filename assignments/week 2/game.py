import time

# typing function so the words appear one at a time (found on the internet)
def type_print(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.03)
    print()


# title screen
print("*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")
print("*                                   *")
print("*        THE  LOST  FOREST          *")
print("*         A Text Adventure          *")
print("*                                   *")
print("*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")
print()
time.sleep(1)

# intro
type_print("You wake up in a dark forest...    /\\   /\\   /\\")
time.sleep(0.7)
type_print("The wind howls and the trees creak around you.")
time.sleep(0.7)
type_print("You don't remember how you got here.")
time.sleep(1)
print()

# user input 1 - get the player's name
name = input(">> What is your name, traveler?  ")
type_print("\nNice to meet you, " + name + ". Your journey begins now. Good luck!")
time.sleep(1)
print()

# user input 2 - a number between 1 and 5 (with range check)
type_print("Pick your FATE (between 1 and 5).")
type_print("This number will decide your fate later on...")

lucky_number = 0
while True:
    answer = input("Enter a number from 1 to 5:  ")
    if answer.isdigit():
        lucky_number = int(answer)
        # nested if - only break out of the loop if number is in range
        if lucky_number >= 1 and lucky_number <= 5:
            break
        else:
            print("[!] follow the instructions, or there will be consequences.")
    else:
        print("[!] follow the instructions, or there will be consequences.")

type_print("\n*~* Your lucky number is " + str(lucky_number) + " *~*")
time.sleep(1)
print()

# user input 3 - the big choice
type_print("You walk for hours and come to a fork in the road.   ====<>====")
time.sleep(0.5)
type_print("To the LEFT  there is a dark cave.            ( O )")
time.sleep(0.5)
type_print("To the RIGHT there is a glowing river.        ~~~~~~~~~~")
time.sleep(0.7)

choice = input("\n>> Which way do you go? (left/right):  ")
choice = choice.lower()


# now the choice splits
if choice == "left":
    type_print("\nYou step into the dark cave...")
    time.sleep(1)
    type_print("Bats screech overhead.    ^v^    ^v^    ^v^")
    time.sleep(0.7)
    type_print("Suddenly, a HUGE DRAGON appears!    /\\/\\/\\/\\/\\")
    time.sleep(1)

    # user input 4 - what to do about the dragon
    action = input("\n>> Do you FIGHT or RUN?  ")
    action = action.lower()

    if action == "fight":
        # nested if - lucky number decides if you win or die
        if lucky_number >= 4:
            type_print("\n>==> With great courage, you strike the dragon!")
            time.sleep(0.7)
            type_print("The dragon falls. You are a HERO, " + name + "!")
            print("[ * * *  V I C T O R Y  * * * ]")
        else:
            type_print("\nThe dragon roars and breathes fire on you...")
            time.sleep(0.7)
            type_print("You are too weak. The dragon defeats you, the outcome might have been avoided if you were more lucky.")
            print("[ X_X    G A M E   O V E R    X_X ]")
    elif action == "run":
        type_print("\n==>> You run as fast as you can!")
        time.sleep(1)
        type_print("You escape the cave and live another day.")
        type_print("Not very brave, but at least you are alive, " + name + "...")
    else:
        type_print("\nYou freeze in fear...")
        time.sleep(0.7)
        type_print("The dragon eats you in one bite.")
        print("[ X_X    G A M E   O V E R    X_X ]")

elif choice == "right":
    type_print("\nYou walk to the glowing river.    ~~~~~~~~~~")
    time.sleep(1)
    type_print("A small magical fairy appears in front of you!")
    time.sleep(1)

    # user input 4 - what to do at the river
    action = input("\n>> Do you TALK to the fairy or DRINK from the river?  ")
    action = action.lower()

    if action == "talk":
        # nested if - lucky number decides how good your reward is
        if lucky_number == 5:
            type_print("\n*~* The fairy is impressed by your lucky number! *~*")
            time.sleep(0.7)
            type_print("She grants you THREE wishes and a good grade in TechBasics 1!")
            type_print("You become rich and happy forever, " + name + "!")
            print("[ * * *  V I C T O R Y  * * * ]")
        else:
            type_print("\nThe fairy smiles and gives you a gold coin.   (o)")
            type_print("Not bad, " + name + ". A small reward, but a reward.")
    elif action == "drink":
        type_print("\n~~~  You drink the magical water  ~~~")
        time.sleep(1)
        type_print("Energy fills your body!")
        time.sleep(0.7)
        type_print("You become a powerful WIZARD, " + name + "!   ---*")
        print("[ * * *  V I C T O R Y  * * * ]")
    else:
        type_print("\nYou stand there doing nothing...")
        time.sleep(0.7)
        type_print("The fairy gets bored and flies away.")
        type_print("Your adventure ends quietly.")

else:
    type_print("\nYou can't decide and fall asleep on the road...")
    time.sleep(0.7)
    type_print("A wild boar comes by and steals your shoes!")
    type_print("You wake up barefoot and confused. The end.")


# countdown until the game closes
print()
print("--------------------------------------")
print("The game will close in...")
time.sleep(0.5)
print("5...")
time.sleep(1)
print("4...")
time.sleep(1)
print("3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1...")
time.sleep(1)
print("Goodbye!")
time.sleep(1)
