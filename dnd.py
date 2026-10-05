import time

class CharacterStats:
    def __init__(self, str, dex, con, int, wis, cha):
        self.str = str
        self.dex = dex
        self.con = con
        self.int = int
        self.wis = wis
        self.cha = cha

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

def character_creator():
    print("Create your character:")
    name = input("Choose your character name >> ")
    print("Classes:\n[1] Barbarian\n[2] Fighter\n[3] Rogue\n[4] Sorcerer\n[5] Warlock\n[6] Wizard")
    player_class = int(input("Choose a class >> "))
    print("Species:\n[1] Human\n[2] Elf\n[3] Dwarf\n[4] Orc\n")
    species = int(input("Choose a species >> "))
    return name, species, player_class

def typing_text(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.04) 
    print()

name, species, player_class = character_creator()

typing_text("Greetings fellow adventurer, you are have been chosen to embark on a treacherous journey.\nYou must explore this realm, battling any foe or creature who gets in your way. ")

valid_input = False
while valid_input == False:
    if player_class == 1:
        player_class == "Barbarian"
        print("You have chosen Barbarian")
        valid_input == True
        break
    elif player_class == 2:
        player_class == "Fighter"
        print("You have chosen Fighter")
        valid_input == True
        break
    elif player_class == 3:
        player_class == "Rogue"
        print("You have chosen Rogue")
        valid_input == True
        break
    elif player_class == 4:
        player_class == "Sorcerer"
        print("You have chosen Sorcerer")
        valid_input == True
        break
    elif player_class == 5:
        player_class == "Warlock"
        print("You have chosen Warlock")
        valid_input == True
        break
    elif player_class == 6:
        player_class == "Wizard"
        print("You have chosen Wizard")
        valid_input == True
        break
    else:
        print("Invalid class chosen. Try again.")
        
while valid_input == False:
    if species == 1:
        species == "Human"
        print("You have chosen human.")
        valid_input == True
        break
    elif species == 2:
        species == "Elf"
        print("You have chosen Elf.")
        valid_input == True
        break
    elif species == 3:
        species == "Dwarf"
        print("You have chosen Dwarf.")
        valid_input == True
        break
    elif species == 4:
        species == "Orc"
        print("You have chosen Orc.")
        valid_input == True
        break
    else:
        print("Invalid species chosen. Try again.")

print(f"\nCharacter successfully created:\nName: {name}\nSpecies: {species}\nClass: {player_class}")