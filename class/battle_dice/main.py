import random
from game import Game
from character import Character
from charactertype import CharacterType

alice = Character(name="Alice", character_type=CharacterType.WARRIOR, health=100, attack_power=25)
bob = Character(name="Bob", character_type=CharacterType.MAGE, health=70, attack_power=15)

game = Game(alice, bob)
game.start_battle()


random_roll = random.randint(1, 6)
print(f"Random roll: {random_roll}")
print()

character_types = list(CharacterType)
print(f"Character types: {character_types}")
random_character_type = random.choice(character_types)
print()

