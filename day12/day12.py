class Character:
  def __init__(self, name, health):
    self.name = name
    self.health = health

  def attack(self):
    print(f"{self.name} does a basic attack!")

class Mage(Character):
  def attack(self):
    print(f"{self.name} casts a fireball!")

class Warrior(Character):
  def attack(self):
    print(f"{self.name} swings a sword!")

class Archer(Character):
  def attack(self):
    print(f"{self.name} fires an arrow! ")

# cha1 = Character("Nathan", 24)
# print(cha1.name)

party = [Mage("Merlin", 80), Warrior("Conan", 120), Archer("Legolas", 90)]

for character in party:
  character.attack()