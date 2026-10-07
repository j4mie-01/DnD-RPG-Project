import time

# stats only depend on the class, not the species as well (just cosmetic, although will have different dialogue in-game)
# 20 is the max stat lvl, 1 is lowest, all stats add to 70 for each class
import stats

class_stat_lookup = {
    "Barbarian": stats.barbarian_stats,
    "Bard": stats.bard_stats,
    "Fighter": stats.fighter_stats,
    "Rogue": stats.rogue_stats,
    "Ranger": stats.ranger_stats,
    "Sorcerer": stats.sorcerer_stats,
    "Warlock": stats.warlock_stats,
    "Wizard": stats.wizard_stats
}

def typing_text(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.04) 
    print()

def character_creator():
    print("Create your character:")
    name = input("Choose your character name >> ")
    
    while True:
        name_confirm = input("Are you sure you want that name? Confirm: Y/N >> ").lower()
        if name_confirm == "y":
            print(f"Okay, greetings {name}! Now choose your class.\n")
            break
        elif name_confirm == "n":
            name = input("Okay, enter your name again >> ")
        else:
            print("Invalid confirmation. Type 'Y' or 'N'.")

    print("Classes:\n[1] Barbarian\n[2] Bard \n[3] Fighter\n[4] Rogue\n[5] Ranger\n[6] Sorcerer\n[7] Warlock\n[8] Wizard\n")

    while True:
        player_class = int(input("Choose a class >> "))
        if player_class == 1:
            player_class = "Barbarian"
            print("You have chosen Barbarian.")
            break
        elif player_class == 2:
            player_class = "Bard"
            print("You have chosen Bard.")
            break
        elif player_class == 3:
            player_class = "Fighter"
            print("You have chosen Fighter.")
            break
        elif player_class == 4:
            player_class = "Rogue"
            print("You have chosen Rogue.")
            break
        elif player_class == 5:
            player_class = "Ranger"
            print("You have chosen Ranger.")
            break
        elif player_class == 6:
            player_class = "Sorcerer"
            print("You have chosen Sorcerer.")
            break
        elif player_class == 7:
            player_class = "Warlock"
            print("You have chosen Warlock.")
            break
        elif player_class == 8:
            player_class = "Wizard"
            print("You have chosen Wizard.")
            break            
        else:
            print("Invalid class chosen. Try again.")

    print("Species:\n[1] Human\n[2] Elf\n[3] Dwarf\n[4] Orc\n")

    while True:
        species = int(input("Choose a species >> "))
        if species == 1:
            species = "Human"
            print("You have chosen human.")
            break
        elif species == 2:
            species = "Elf"
            print("You have chosen Elf.")
            break
        elif species == 3:
            species = "Dwarf"
            print("You have chosen Dwarf.")
            break
        elif species == 4:
            species = "Orc"
            print("You have chosen Orc.")
            break
        else:
            print("Invalid species chosen. Try again.")

    return name, species, player_class

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

name, species, player_class = character_creator()

print("=============================="
    f"\nCharacter successfully created:\n"
    f"¦Name: {name}\n"
    f"¦Species: {species}\n"
    f"¦Class: {player_class}\n"
    "=============================="
)

if player_class in class_stat_lookup:
    class_stat_lookup[player_class].display_stats()
else:
    print("An error occurred.")

typing_text("Greetings fellow adventurer, you have been chosen to embark on a treacherous journey.\nYou must explore this realm, battling any foe or creature that gets in your way.")