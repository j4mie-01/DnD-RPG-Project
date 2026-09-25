import sys
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

def character_creator(name, species, player_class, background):
    print("Create your character:")
    name = input("Choose your character name >> ")
    print("Classes:\n[1] Barbarian\n[2] Fighter\n[3] Rogue\n[4] Sorcerer\n[5] Warlock\n[6] Wizard")
    player_class = input("Choose a class >> ")
    print("Species:\n[1] Human\n[2] Elf\n[3] Dwarf\n[4] Orc\n")
    species = input("Choose a species >> ")
    print("Backgrounds:\n[1] Soldier\n[2] Criminal\n[3] Noble\n[Folk Hero]")
    background = input("Choose a background for your character: ")
    return name, species, player_class, background

# continue this function at home
#def typing_text(char):
#    for char in str:
#        time.sleep(.1)
#        print
        

print("Greetings fellow adventurer, you are have been chosen to embark on a treacherous journey. You must ")
player = character_creator()
if name == "1"
    print("Are you sure you want to ")
print(f"\nCharacter successfully created:\nName: {player.name}\nSpecies: {player.species}\nClass: {player.player_class}\nBackground: {player.background}")