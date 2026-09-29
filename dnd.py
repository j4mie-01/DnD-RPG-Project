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

def character_creator(name, species, player_class):
    print("Create your character:")
    name = int(input("Choose your character name >> "))
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
        
player = character_creator()
name, species, player_class = character_creator()

typing_text("Greetings fellow adventurer, you are have been chosen to embark on a treacherous journey.\nYou must explore this realm, battling any foe or creature who gets in your way. ")
valid_input = False
while valid_input == False:
    if species == 1:
        species == "Human"
        print("You have chosen human.")
        valid_input == True
    elif species == 2:
        species == "Elf"
        print("You have chosen Elf.")
        valid_input == True
    elif species == 3:
        species == "Dwarf"
        print("You have chosen Dwarf.")
        valid_input == True
    elif species == 4:
        species == "Orc"
        print("You have chosen Orc.")
        valid_input == True
    else:
        print("Invalid species chosen. Try again.")

print(f"\nCharacter successfully created:\nName: {player.name}\nSpecies: {player.species}\nClass: {player.player_class}\nBackground: {player.background}")

