# game.py
import random
from character import Character
from charactertype import CharacterType

class Game:
    """Manages the Dice Battle game logic."""
    
    def __init__(self, player1: Character, player2: Character) -> None:
        """Initializes the game with two players."""
        self.__player1: Character = player1
        self.__player2: Character = player2
    
    def attack(self, attacker: Character, defender: Character) -> None:
        """Performs an attack where the attacker rolls a die to determine damage dealt."""
        damage_factor: int = random.randint(1, 6)
        defender.health -= damage_factor * attacker.attack_power
        print(f"{attacker.name} attacks {defender.name} for {damage_factor} damage!")
        print(f"{defender.name} now has {max(0, defender.health)} health remaining.\n")
    
    def start_battle(self) -> None:
        """Starts a turn-based battle between two players."""
        print(f"Battle Start: {self.__player1.name} vs {self.__player2.name}\n")
        turn: int = 0
        
        while self.__player1.health > 0 and self.__player2.health > 0:
            if turn % 2 == 0:
                self.attack(self.__player1, self.__player2)
            else:
                self.attack(self.__player2, self.__player1)
            
            turn += 1
        
        winner: Character = self.__player1 if self.__player1.health > 0 else self.__player2
        print(f"{winner.name} wins the battle!")

    def attack_alt(self, attacker: Character, defender: Character) -> None:
        """Performs an attack where the attacker rolls a die to determine damage dealt.
        A factor is applied based on the defender's character type:
        If the defender is a mage, the damage is halved due to magic.
        If the defender is a warrior, the damage is increased by 25%.
        If the defender is a rogue, the damage is increased by 10%."""
        damage: int = random.randint(1, 6) * attacker.attack_power
        
        if defender.character_type == CharacterType.MAGE:
            damage = damage // 2  # Halve the damage. Also could write: damage //= 2
        elif defender.character_type == CharacterType.WARRIOR:
            damage = int(damage * 1.25)  # Increase by 25%
        elif defender.character_type == CharacterType.ROGUE:
            damage = int(damage * 1.10)  # Increase by 10%
        else:
            damage = damage
        
        defender.health -= damage
        print(f"{attacker.name} ({attacker.character_type.value}) attacks {defender.name} ({defender.character_type.value}) for {damage} damage!")
        print(f"{defender.name} now has {max(0, defender.health)} health remaining.\n")

    def attack_alt_with_match(self, attacker: Character, defender: Character) -> None:
        """Performs an attack where the attacker rolls a die to determine damage dealt.
        A factor is applied based on the defener's character type:
        If the defender is a mage, the damage is halved due to magic.
        If the defender is a warrior, the damage is increased by 25%.
        If the defender is a rogue, the damage is increased by 10%."""
        damage: int = random.randint(1, 6) * attacker.attack_power
        
        match defender.character_type:
            case CharacterType.MAGE:
                damage = damage // 2
            case CharacterType.WARRIOR:
                damage = int(damage * 1.25)
            case CharacterType.ROGUE:
                damage = int(damage * 1.10)
            case _:
                damage = damage

        defender.health -= damage
        print(f"{attacker.name} ({attacker.character_type.value}) attacks {defender.name} ({defender.character_type.value}) for {damage} damage!")
        print(f"{defender.name} now has {max(0, defender.health)} health remaining.\n")