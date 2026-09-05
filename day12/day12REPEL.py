# class Character:
#     def __init__(self, name, health):
#         self.name = name
#         self.health = health
#     def describe(self):
#         return f"{self.name} has {self.health} HP"
# class Mage(Character):
#     pass   # no new code at all — just inherits everything
# merlin = Mage("Merlin", 80)
# print(merlin.describe())


class Character:
  def attack(self):
    print("Basic attack!")
class Mage(Character):
  def attack(self):
    print("Fireball!")
class Rogue(Character):
  pass
mage = Mage()
rogue = Rogue()

print(mage.attack())
print(rogue.attack())