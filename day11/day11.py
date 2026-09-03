class Character:
  def __init__(self, name, health, attack_power):
    self.name = name
    self.health = health
    self.attack_power = attack_power

  def attack(self, target):
    target.health -= self.attack_power
    print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")

hero = Character("Hero", 100, 15)
goblin = Character("Goblin", 30, 5)

hero.attack(goblin)
print(f"{goblin.name}'s health: {goblin.health}")

goblin.attack(hero)
print(f"{hero.name}'s health: {hero.health}")