class CharacterStats:

    def __init__(self, str, dex, con, int, wis, cha):

        self.str = str # strength
        self.dex = dex # dexterity
        self.con = con # constitution
        self.int = int # intelligence
        self.wis = wis # wisdom
        self.cha = cha # charisma

# this method can be used to displays stats when needed
    def display_stats(self):
        print(
        f"\n======Stats======\n¦Strength: {self.str}\n"
        f"¦Dexterity: {self.dex}\n"
        f"¦Constitution: {self.con}\n"
        f"¦Intelligence: {self.int}\n"
        f"¦Wisdom: {self.wis}\n"
        f"¦Charisma: {self.cha}\n"
        "=================\n"
        )        


barbarian_stats = CharacterStats(16, 14, 14, 8, 8, 10)
bard_stats = CharacterStats(8, 14, 11, 12, 10, 15)
fighter_stats = CharacterStats(15, 13, 13, 10, 10, 9)
rogue_stats = CharacterStats(8, 16, 10, 13, 9, 14)
ranger_stats = CharacterStats(12, 16, 12, 9, 13, 8)
sorcerer_stats = CharacterStats(8, 14, 12, 11, 9, 16)
warlock_stats = CharacterStats(8, 12, 14, 11, 10, 15)
wizard_stats = CharacterStats(8, 13, 12, 15, 15, 7)