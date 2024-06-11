from echo_mainstats import Mainstats
from echo_substats import Substats
from echo_class import EchoClass
from echo_rarity import EchoRarity

from typing import Optional

import random

# This is temporary :clueless:
MAX_SUBSTAT_MAP = {EchoRarity.RANK_2 : 2, EchoRarity.RANK_3 : 3, EchoRarity.RANK_4 : 4, EchoRarity.RANK_5 : 5}
ALL_ECHO_SUBSTATS = set(Substats)
SUBSTAT_VALUES = {
    Substats.ATK_FLAT : [40, 50, 60, 70],
    Substats.DEF_FLAT : [40, 50, 60, 70],
    Substats.ATK_PERCENT : [0.064, 0.071, 0.079, 0.086, 0.094, 0.101, 0.109, 0.116],
    Substats.DEF_PERCENT : [0.081, 0.09, 0.1, 0.109, 0.118, 0.128, 0.138, 0.147],
    Substats.HP_FLAT : [320, 360, 390, 430, 470, 510, 540, 580],
    Substats.HP_PERCENT : [0.081, 0.09, 0.1, 0.109, 0.118, 0.128, 0.138, 0.147],
    Substats.CRIT_DMG : [.126, .138, .15, .162, .174, .186, .198, .21],
    Substats.CRIT_RATE : [.063, .069, .075, .081, .087, .093, .099, .105],
    Substats.ENERGY_REGEN : [.068, 0.076, 0.084, 0.092, 0.1, 0.108, 0.116, 0.124],
    Substats.BASIC_ATTACK_DMG : [0.064, 0.071, 0.079, 0.086, 0.094, 0.101, 0.109, 0.116],
    Substats.HEAVY_ATTACK_DMG : [0.064, 0.071, 0.079, 0.086, 0.094, 0.101, 0.109, 0.116],
    Substats.RESONANCE_LIBERATION : [0.064, 0.071, 0.079, 0.086, 0.094, 0.101, 0.109, 0.116],
    Substats.RESONANCE_SKILL : [0.064, 0.071, 0.079, 0.086, 0.094, 0.101, 0.109, 0.116],
}

SUBSTAT_ROLL_WEIGHTS = {
    Substats.ATK_FLAT : [0.1852, 0.4445, 0.2638, 0.1036],
    Substats.DEF_FLAT : [0.1852, 0.4445, 0.2638, 0.1036],
    Substats.ATK_PERCENT : [0.0773, 0.1465, 0.1954, 0.2351, 0.1563, 0.1042, 0.0595, 0.0298],
    Substats.DEF_PERCENT : [0.0773, 0.1465, 0.1954, 0.2351, 0.1563, 0.1042, 0.0595, 0.0298],
    Substats.HP_FLAT : [0.0773, 0.1465, 0.1954, 0.2351, 0.1563, 0.1042, 0.0595, 0.0298],
    Substats.HP_PERCENT : [0.0773, 0.1465, 0.1954, 0.2351, 0.1563, 0.1042, 0.0595, 0.0298],
    Substats.CRIT_DMG : [0.0773, 0.1465, 0.1954, 0.2351, 0.1563, 0.1042, 0.0595, 0.0298],
    Substats.CRIT_RATE : [0.0773, 0.1465, 0.1954, 0.2351, 0.1563, 0.1042, 0.0595, 0.0298],
    Substats.ENERGY_REGEN : [0.0773, 0.1465, 0.1954, 0.2351, 0.1563, 0.1042, 0.0595, 0.0298],
    Substats.BASIC_ATTACK_DMG : [0.0773, 0.1465, 0.1954, 0.2351, 0.1563, 0.1042, 0.0595, 0.0298],
    Substats.HEAVY_ATTACK_DMG : [0.0773, 0.1465, 0.1954, 0.2351, 0.1563, 0.1042, 0.0595, 0.0298],
    Substats.RESONANCE_LIBERATION : [0.0773, 0.1465, 0.1954, 0.2351, 0.1563, 0.1042, 0.0595, 0.0298],
    Substats.RESONANCE_SKILL : [0.0773, 0.1465, 0.1954, 0.2351, 0.1563, 0.1042, 0.0595, 0.0298],
}

class Echo:

    def __init__(self, 
                 mainstat : Optional[Mainstats] = None, 
                 rarity : Optional[EchoRarity]=None, 
                 substats : Optional[list[Substats]]=None, 
                 echo_class :Optional[EchoClass]=None, 
                 starting_level=25, 
                 substat_values=None) -> None:
        self.mainstat = mainstat if mainstat else self.random_mainstat()
        self.rarity = rarity if rarity else random.choice(list(EchoRarity))
        self.max_substat_count = MAX_SUBSTAT_MAP[self.rarity]
        self.current_level = starting_level
        self.substats = substats if substats else []
        self.substat_values = substat_values if substat_values else {}
        self.echo_class = echo_class
    
    def generate_substats_default(self):
        for i in range((self.current_level // 5) + 1):
            self.roll_substat()

    # Roll a new substat to be added to this echo, if applicable. 
    def roll_substat(self) -> None:
        if len(self.substats) < self.max_substat_count:
            # Enums don't support indexing by default (but do have iteration)
            possible_substats = ALL_ECHO_SUBSTATS.copy()
            for substat in self.substats:
                possible_substats.remove(substat)
            # Technically inefficient (O(n)), but the set of possible substats is not particularly large, so this should be fine
            new_substat = random.choice(list(possible_substats))
            self.substats.append(new_substat)
            self.substat_values[new_substat] = random.choices(SUBSTAT_VALUES[new_substat], SUBSTAT_ROLL_WEIGHTS[new_substat])[0]

    # Mainstats are randomly chosen
    def random_mainstat(self) -> Mainstats:
        return random.choice(list(Mainstats))


    