class Shoe():
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

class Converse(Shoe):
    def __init__(self, lowOrHighTop, tongueColor, brand = "Converse"):
        self.lowOrHighTop = lowOrHighTop
        self.tongueColor = tongueColor
        self.brand = brand
    
    def __str__(self):
        return "{} | {} | {}".format(self.lowOrHighTop, self.tongueColor, self.brand)

class CombatBoot(Shoe):
    def __init__(self, militaryBranch, DesertOrJungle):
        self.militaryBranch = militaryBranch
        self.DesertOrJungle = DesertOrJungle
    def __str__(self):
        return "{} | {}".format(self.militaryBranch, self.DesertOrJungle)

class Sandal(Shoe):
    def __init__(self, openOrClosedToe, waterproof):
        self.openOrClosedToe = openOrClosedToe
        self.waterproof = waterproof
    def __str__(self):
        return "{} | {}".format(self.openOrClosedToe, self.waterproof)



sandal = Sandal("Open", "Not-waterproof")
combatboot = CombatBoot("Somewhere", "Desert")
converse = Converse("Low", "Black", "Converse")

print("Sandal: {}".format(sandal))
print("Converse: {}".format(converse))
print("Combatboot: {}".format(combatboot))