# Days 1-5 review project: The Lost Lantern

print("=== THE LOST LANTERN ===")
print("Find the old lantern before the mountain storm arrives.")

player_name = input("What is your adventurer's name? ").strip()
if not player_name:
    player_name = "Traveler"

health = 10
gold = 5
torch_lit = False
distance = float(input("How many miles have you traveled today? "))

print()
print(f"Welcome, {player_name.upper()}!")
print(f"You have {health} health, {gold} gold, and traveled {distance:.1f} miles.")

# The first character and a slice are both used to inspect a string.
name_initial = player_name[0].upper()
name_preview = player_name[:3].lower()
print(f"Your name begins with {name_initial}. A short name preview is {name_preview}.")

print()
print("You reach a forest path.")
steps = int(input("How many steps will you take into the forest (1-5)? "))

if steps < 1 or steps > 5:
    print("You choose 3 steps instead.")
    steps = 3

found_clue = False
for step in range(1, steps + 1):
    print(f"Step {step}: You look around the trees.")

    if step == 2:
        print("You find a note under a stone.")
        clue = "lantern waits beyond the old bridge"
        words = clue.split()
        # print(words)
        neat_clue = " ".join(words).replace("old", "ancient")
        print(f"The note says: {neat_clue}.")
        found_clue = True
        continue

    if step == 4 and not found_clue:
        print("The path is quiet, but you find no clue.")

if found_clue:
    print("The clue points toward a guarded bridge.")
else:
    print("You decide to follow the path toward a guarded bridge anyway.")

print()
print("A bridge guard blocks your way.")
password = input("The guard asks for the password. Type your guess: ").strip().lower()

if password == "ancient bridge" or password == "lantern":
    print("The guard nods and lets you cross.")
    gold = gold + 2
else:
    print("The guard asks you to answer a riddle instead.")
    riddle_answer = input("What shines in darkness? ").strip().lower()

    if riddle_answer == "lantern" and (found_clue or torch_lit == False):
        print("Correct! The guard gives you a small torch.")
        torch_lit = True
    else:
        print("Wrong answer. You pay one gold coin to cross.")
        gold = gold - 1

print()
print("Beyond the bridge, a cave entrance opens.")
print("A sign reads: 'The first letter of your name opens the door.'")
door_code = input("Enter one letter: ").strip()

if door_code:
    if door_code[0].lower() == name_initial.lower():
        print("The stone door opens.")
        door_open = True
    else:
        print("The door stays closed, but you notice a side tunnel.")
        door_open = False
else:
    print("You enter the side tunnel.")
    door_open = False

print()
if door_open:
    print("Inside, you see the lost lantern beside a sleeping dragon.")
else:
    print("The side tunnel leads to the lantern, but the dragon wakes up.")

print("You have three choices in the cave.")
escaped = False
round_number = 1
while round_number <= 3 and escaped == False and health > 0:
    print(f"Choice round {round_number}:")
    for prompt_line in range(1, 2):
        print("The dragon watches your next move.")
    action = input("Choose sneak, run, or fight: ").strip().lower()
    round_number = round_number + 1

    if action == "sneak":
        if torch_lit or door_open:
            print("You sneak past the dragon and grab the lantern.")
            escaped = True
            break
        else:
            print("It is too dark to sneak safely.")
            continue
    elif action == "run":
        print("You run through the side tunnel and escape with the lantern.")
        escaped = True
        break
    elif action == "fight":
        print("You swing your sword.")
        health = health - 3
        if health <= 0:
            print("The dragon wins.")
            break
        print(f"You survive the attack with {health} health left.")
    else:
        print("That is not a choice. Try again.")
        continue

if escaped and health > 0:
    gold_text = str(gold)
    health_text = str(health)
    summary = [player_name, health_text, gold_text]
    print()
    print(" ".join(summary).replace(player_name, player_name.title()))
    print(f"Victory, {player_name.title()}! You found the lantern.")
    print(f"Final health: {health}, final gold: {gold}.")
else:
    print()
    print(f"Game over, {player_name.title()}. The lantern remains in the cave.")
