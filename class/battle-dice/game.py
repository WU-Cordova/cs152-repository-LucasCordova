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
        """Performs an attack where the attacker rolls a die to determine damage dealt.
            The damage is multiplied by the attacker's attack power."""
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
                self.attack_alt(self.__player1, self.__player2)
            else:
                self.attack_alt(self.__player2, self.__player1)
            
            turn += 1
        
        winner: Character = self.__player1 if self.__player1.health > 0 else self.__player2
        print(f"{winner.name} wins the battle!")

    def attack_alt(self, attacker: Character, defender: Character) -> None:
        """Performs an attack where the attacker rolls a die to determine damage dealt.
            Another factor is applied based on the attacker's and defender's character types:
            Attacker   |   Defender   |   Factor to Damage
            +----------+--------------+-------------------+
            Warrior    |   Warrior    |   1.1
            Warrior    |   Mage, Rogue|   1.2
            Mage       |   Warrior    |   1.4
            Mage       |   Mage       |   1.5
            Mage       |   Rogue      |   1.6
            Rogue      |   Mage       |   1.7

            If none of these combinations are met, the damage factor is 2.0.
        """
        damage: int = random.randint(1, 6) * attacker.attack_power
        
        if attacker.character_type == CharacterType.WARRIOR:
            if defender.character_type == CharacterType.WARRIOR:
                damage = int(damage * 1.1)
            elif defender.character_type in [CharacterType.MAGE, CharacterType.ROGUE]:
                damage = int(damage * 1.2)
        elif attacker.character_type == CharacterType.MAGE:
            if defender.character_type == CharacterType.WARRIOR:
                damage = int(damage * 1.4)
            elif defender.character_type == CharacterType.MAGE:
                damage = int(damage * 1.5)
            elif defender.character_type == CharacterType.ROGUE:
                damage = int(damage * 1.6)
        elif attacker.character_type == CharacterType.ROGUE:
            if defender.character_type == CharacterType.MAGE:
                damage = int(damage * 1.7)
        else:
            damage = int(damage * 2.0)
        
        defender.health -= damage
        print(f"{attacker.name} ({attacker.character_type.value}) attacks {defender.name} ({defender.character_type.value}) for {damage} damage!")
        print(f"{defender.name} now has {max(0, defender.health)} health remaining.\n")

    def attack_alt_with_match(self, attacker: Character, defender: Character) -> None:
        """Performs an attack where the attacker rolls a die to determine damage dealt.
            Another factor is applied based on the attacker's and defender's character types:
            Attacker   |   Defender   |   Factor to Damage
            +----------+--------------+-------------------+
            Warrior    |   Warrior    |   1.1
            Warrior    |   Mage, Rogue|   1.2
            Mage       |   Warrior    |   1.4
            Mage       |   Mage       |   1.5
            Mage       |   Rogue      |   1.6
            Rogue      |   Mage       |   1.7

            If none of these combinations are met, the damage factor is 2.0.
        """

        damage: int = random.randint(1, 6) * attacker.attack_power
        
        match attacker.character_type, defender.character_type:
            case CharacterType.WARRIOR, CharacterType.WARRIOR:
                damage = int(damage * 1.1)
            case CharacterType.WARRIOR, (CharacterType.MAGE | CharacterType.ROGUE):
                damage = int(damage * 1.2)
            case CharacterType.MAGE, CharacterType.WARRIOR:
                damage = int(damage * 1.4)
            case (CharacterType.MAGE | CharacterType.ROGUE), CharacterType.MAGE:
                damage = int(damage * 1.5)
            case CharacterType.MAGE, CharacterType.ROGUE:
                damage = int(damage * 1.6)
            case CharacterType.ROGUE, CharacterType.MAGE:
                damage = int(damage * 1.7)
            case _:
                damage = int(damage * 2.0)

        defender.health -= damage
        print(f"{attacker.name} ({attacker.character_type.value}) attacks {defender.name} ({defender.character_type.value}) for {damage} damage!")
        print(f"{defender.name} now has {max(0, defender.health)} health remaining.\n")