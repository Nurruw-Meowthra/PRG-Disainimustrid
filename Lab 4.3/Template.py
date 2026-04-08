from abc import ABC, abstractmethod

class Creature:
    def __init__(self, attack, health):
        self.attack = attack
        self.health = health
        self.max_HEALTH = health

    def is_alive(self):
        return self.health > 0


class CardGame(ABC):
    def __init__(self, creatures):
        self.creatures = creatures

    def combat(self, c1_index, c2_index):
        c1 = self.creatures[c1_index]
        c2 = self.creatures[c2_index]

        self.hit(c1, c2)
        self.hit(c2, c1)

        if c1.is_alive() == c2.is_alive():
            return -1
        elif c2.is_alive():
            return c2_index
        else:
            return c1_index
    
    @abstractmethod
    def hit(self, attacker, defender):
        pass

class TemporaryDamageCardGame(CardGame):
    def hit(self, attacker, defender):
        defender.health -= attacker.attack
        if defender.health > 0:
            defender.health = defender.max_HEALTH
            return True
        else:
            return False

class PermanentDamageCardGame(CardGame):
    def hit(self, attacker, defender):
        defender.health -= attacker.attack
        if defender.health > 0:
            return True
        else:
            return False
