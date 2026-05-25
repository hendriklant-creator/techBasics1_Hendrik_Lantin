# Assignment 6 - Inventory game with dialogue choices
# Scene inspired by the opening of Metal Gear Solid V: The Phantom Pain (my absolute favourite game ever)
# Venom Snake wakes up in a hospital after 9 years in a coma due to a helicopter crash

# The doctor asks you three questions and your answers shape the ending, i tried to give it an rpg spin with the inventory system and item interactability adding a bit of a storytelling aspect to the examining of stuff around the room

# ===== INVENTORY AND ROOM =====
# the players inventory is a list of dictionaries
inventory = []
INVENTORY_LIMIT = 5

# items currently in the room
items_in_room = [
    {"name": "bandages", "type": "healing", "uses": 1, "desc": "Old bloody bandages wrapped tight around your chest."},
    {"name": "mirror", "type": "tool", "uses": 1, "desc": "A small mirror on the bedside table. You haven't looked yet."},
    {"name": "iv_drip", "type": "tool", "uses": 1, "desc": "An IV drip is feeding something cold into your arm."},
    {"name": "chart", "type": "info", "uses": 1, "desc": "A clipboard hangs at the foot of the bed. The handwriting is rushed."},
    {"name": "arm", "type": "body", "uses": 1, "desc": "Your right arm. Wrapped in gauze. It doesn't feel like yours."},
]

#STORY STATE TRACKER

look_count = 0
doctor_arrived = False
arm_looked_at = False
panic_calmed = False
assassin_arrived = False
scene_over = False

# this list collects the player's three answers
# each one is "soldier", "broken" or "cold"
# at the end we count which came up most to pick the ending which would make sense
choices = []


# BASIC INVENTORY FUNCTIONS

def show_room_items():
    print("\nYou look around the room and see:")
    if len(items_in_room) == 0:
        print(" - nothing of interest")
    for item in items_in_room:
        print(" - " + item["name"])


def show_inventory():
    print("\nYour inventory:")
    if len(inventory) == 0:
        print(" - empty")
    for item in inventory:
        print(" - " + item["name"])


def pick_up(item_name):
    # same pattern as the draw_card() example in class
    if len(inventory) >= INVENTORY_LIMIT:
        print("You can't carry any more.")
        return
    for item in items_in_room:
        if item["name"] == item_name:
            inventory.append(item)
            items_in_room.remove(item)
            print("You took the " + item_name + ".")
            return
    print("There's no " + item_name + " here.")


def drop(item_name):
    for item in inventory:
        if item["name"] == item_name:
            items_in_room.append(item)
            inventory.remove(item)
            print("You dropped the " + item_name + ".")
            return
    print("You don't have a " + item_name + ".")


def examine(item_name):
    # examining the arm ONLY AFTER the doctor arrived triggers the panic attack
    global arm_looked_at
    for item in inventory + items_in_room:
        if item["name"] == item_name:
            print(item["desc"])
            if item_name == "arm":
                arm_looked_at = True
            return
    print("You can't see that.")


def use(item_name):
    for item in inventory:
        if item["name"] == item_name:
            if item_name == "bandages":
                print("\nYou tighten the bandages. The pain dulls a little.")
                inventory.remove(item)
            elif item_name == "mirror":
                print("\nYou hold the mirror up. A stranger stares back.")
                print("Long hair. Bearded. A piece of metal sticking out of your forehead!")
                print("That can't be you.")
            elif item_name == "iv_drip":
                print("\nYou tug at the IV. It hurts. Better leave it in.")
            else:
                print("Nothing happens.")
            return
    print("You don't have a " + item_name + ".")


def show_help():
    print("\nCommands you can use:")
    print(" - look")
    print(" - inventory")
    print(" - pickup [item]")
    print(" - drop [item]")
    print(" - examine [item]")
    print(" - use [item]")
    print(" - help")
    print(" - quit")


#DIALOGUE CHOICE FUNCTION / used AI here because i was lost

def ask_choice(question, options):
    # prints a question and three options, returns the chosen vibe - I used AI for this because i was lost and couldn't figure it out!!!
    # options is a list of three (label, vibe) tuples
    print("\n" + question)
    print(" 1) " + options[0][0])
    print(" 2) " + options[1][0])
    print(" 3) " + options[2][0])
    # keep asking until the input is valid
    while True:
        answer = input("> ").strip()
        if answer == "1":
            return options[0][1]
        elif answer == "2":
            return options[1][1]
        elif answer == "3":
            return options[2][1]
        else:
            print("Type 1, 2 or 3.")


#STORY EVENTS

def doctor_enters():
    # the doctor walks in and starts asking you questions
    # each answer is added to the choices list!!!!!
    global doctor_arrived
    doctor_arrived = True
    print("\n--- The door clicks open. ---")
    print("A man in a white coat steps in. His face is tired.")
    print("Easy. Easy now. You've been out a long time.")
    print("Nine years. You were in a coma for nine years, just try to relax.")
    print("He pulls a chair close to the bed and sits down.")

    # first question is about identity
    vibe1 = ask_choice(
        "'Do you remember your name?'",
        [("\"Yeah... I'm Snake.\"", "soldier"),
         ("\"I don't know.\"", "broken"),
         ("\"Does it matter?\"", "cold")]
    )
    choices.append(vibe1)

    # the doctor reacts a little to your answer
    if vibe1 == "soldier":
        print("\nHe nods slowly. Good. That's good.")
    elif vibe1 == "broken":
        print("\nHe writes something down. It'll come back. Give it time.'")
    else:
        print("\nHe pauses. It might. Soon.")

    # second question - memory of the explosion
    vibe2 = ask_choice(
        "'Do you remember the explosion?'",
        [("\"Every second of it.\"", "soldier"),
         ("\"Flashes. Fire.\"", "broken"),
         ("\"Nothing. Blank.\"", "cold")]
    )
    choices.append(vibe2)

    if vibe2 == "soldier":
        print("\nThen you know what's coming. There are people who want you dead.")
    elif vibe2 == "broken":
        print("\nIt'll come back. Maybe more than you want it to.")
    else:
        print("\nProbably better that way. For now.")

    print("\nTake your time. Look at yourself, look around you, what can you recognise or remember. Remember slowly.")
    print("\n(Maybe you should examine your arm.)")


def panic_attack():
    # if the player examined their arm - memory floods back, the doctor sedates you
    # after the panic, the doctor asks the third question, softer
    global panic_calmed
    print("\n--- Your heart starts pounding. ---")
    print("You stare at the gauze on your arm. Pieces of memory come back.")
    print("Fire. Screaming. Paz, and the bomb. A helicopter going down. Hands pulling you out.")
    print("The heart monitor screams. You can't breathe.")
    print("\nThe doctor rushes over with a syringe.")
    print("Stay with me. Stay with me. Breathe.")
    print("He pushes a serum into the IV. The world goes soft.")
    print("\nThe panic fades. He stays sitting beside the bed.")
    print("'There's one more thing I have to ask you.'")

    # third question - what do you want
    vibe3 = ask_choice(
        "When you get out of here. What do you want?",
        [("\"Revenge.\"", "soldier"),
         ("\"To be left alone.\"", "broken"),
         ("\"To keep fighting.\"", "cold")]
    )
    choices.append(vibe3)

    if vibe3 == "soldier":
        print("\nHe looks at you for a long time. 'I thought you'd say that.'")
    elif vibe3 == "broken":
        print("\nHe looks away. I'm sorry. I don't think they'll let you.")
    else:
        print("\nThen this isn't over for you.")

    panic_calmed = True


def assassin_enters():
    # Quiet sneaks in through the window and kills the doctor!!!!
    global assassin_arrived
    assassin_arrived = True
    print("\n The window slides open. Quietly. ")
    print("A figure climbs through. Tall. Silent. A woman.")
    print("She moves past your bed without looking at you.")
    print("The doctor turns. He doesn't even get to scream, before the tight wire wraps around his neck")
    print("She is standing over you now. Looking down. Waiting, hesitating...")
    print("\nThere is a scalpel on the tray next to your bed.")
    print("There is a pistol on the doctor's belt.")
    print("\nYou could try to grab something. You probably can't move fast enough, but it might be worth a shot.")
    print("(Type: pickup scalpel / pickup pistol / wait)")
    items_in_room.append({"name": "scalpel", "type": "weapon", "uses": 1, "desc": "A small blade."})
    items_in_room.append({"name": "pistol", "type": "weapon", "uses": 1, "desc": "A handgun on the doctor's belt."})


def ending(player_choice):
    # the final scene - Ishmael saves you no matter what you did
    # the ending lines change based on which vibe came up most in your choises.
    global scene_over
    print("")
    if player_choice == "scalpel":
        print("You reach for the scalpel. Your fingers won't close around it.")
        print("It clatters to the floor.")
    elif player_choice == "pistol":
        print("You try to reach for the pistol. Your arm doesn't move.")
        print("You can only watch.")
    else:
        print("You don't move. You can't. You just look back at her.")

    print("\nShe raises her hand with the pistol.")
    print("\n--- A gunshot. ---")
    print("She flinches. Her shoulder bursts red. She is gone and out of the window before you blink, she escapes harmed, but not dead")
    print("\nA man rolls out from behind the curtain. Bearded. Bandaged. Familiar, you cant make out his face though, but the voice sounds similar to yours.")
    print("He pulls you off the bed and onto the floor.")
    print("'On your feet, soldier. We are getting you out of here.'")

    # count which vibe came up most in the three answers

    soldier_score = choices.count("soldier")
    broken_score = choices.count("broken")
    cold_score = choices.count("cold")

    # whichever has the highest count picks the ending tone
    print("\nYou look at him. Your voice is rough from nine years of silence.")
    print("\"...Who are you?\"")
    print("\nHe almost smiles.")

    if soldier_score >= broken_score and soldier_score >= cold_score:
        # soldier ending - hungry, vengeful
        print("'I'm you. Or at least... I used to be.'")
        print("\nYou meet his eyes. Then we have work to do.")
        print("He nods. 'Yeah. We do.'")
    elif broken_score >= cold_score:
        # broken ending - grief, can't speak
        print("I'm you. Or at least... I used to be.")
        print("\nYou open your mouth. Nothing comes out.")
        print("He squeezes your shoulder. It's okay. Don't talk. Just move.")
    else:
        # cold ending - identity loss
        print("'I'm you. Or at least... I used to be.'")
        print("\n'Then who am I?'")
        print("He looks at you for a long second.")
        print("Whoever you need to be.")

    print("\n END OF PROLOGUE")
    scene_over = True


#MAIN GAME LOOP

def main():
    global look_count


    print("  THE PHANTOM PAIN - Prologue (text version)")

    print("\nA hospital room. Cyprus. 1984.")
    print("You open your eyes for the first time in nine years, a passing nurse gasps, and runs to get the doctor, you lie motionless trying to make sense of what is happening. As you slowly come to life you look around.")
    print("The ceiling is white. The air smells of disinfectant.")
    print("You don't know where you are. You don't know who you are.")
    print("\n(Type 'help' for commands. Try 'look' first.)")

    while not scene_over:
        command = input("\n> ").strip().lower()

        parts = command.split(" ", 1)
        action = parts[0]
        target = parts[1] if len(parts) > 1 else ""

        # if Quiet has arrived, only the final choice matters
        if assassin_arrived:
            if action == "pickup" and target == "scalpel":
                ending("scalpel")
            elif action == "pickup" and target == "pistol":
                ending("pistol")
            elif action == "wait":
                ending("wait")
            else:
                print("(You can only pickup scalpel, pickup pistol, or wait.)")
            continue

        # normal commands for rpg elements
        if action == "help":
            show_help()
        elif action == "look":
            show_room_items()
            look_count += 1
        elif action == "inventory":
            show_inventory()
        elif action == "pickup":
            pick_up(target)
        elif action == "drop":
            drop(target)
        elif action == "examine":
            examine(target)
            look_count += 1
        elif action == "use":
            use(target)
        elif action == "quit":
            print("You close your eyes again.")
            break
        else:
            print("You don't understand.")

        # automatic story triggers for the dialogue to kick in, i hope this is enough time for a player to actually understand whats going on through the looking commands.
        if look_count >= 3 and not doctor_arrived:
            doctor_enters()
        if doctor_arrived and arm_looked_at and not panic_calmed:
            panic_attack()
        if panic_calmed and not assassin_arrived:
            assassin_enters()


main()
