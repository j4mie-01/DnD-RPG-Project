class Character:
    def __init__(self, name, species, player_class):
        self.name = name
        self.species = species
        self.player_class = player_class

def character_creator():
    print("Create your character:")
    name = input("Choose your character name >> ")
    print("Classes:\n[1] Barbarian\n[2] Fighter\n[3] Rogue\n[4] Sorcerer\n[5] Warlock\n[6] Wizard")
    player_class = input("Choose a class >> ")
    print("Species:\n[1] Human\n[2] Elf\n[3] Dwarf\n[4] Orc\n")
    species = input("Choose a species >> ")

    return Character(name, species, player_class)


player = character_creator()
print(f"\nCharacter successfully created:\nName: {player.name}\nSpecies: {player.species}\nClass: {player.player_class}")