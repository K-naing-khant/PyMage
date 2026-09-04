class Character:
  def __init__(self, name, health):
    self.name = name
    self.health = health
hero = Character("Hero", 100)
goblin = Character("Goblin", 30)

print(hero.health)
print(goblin.health)
hero.health = 50
print(hero.health)
print(goblin.health)