from enum import Enum

class Mainstats(Enum):
    # Normal stats
    ATK_PERCENT = "ATK_PERCENT"
    DEF_PERCENT = "DEF_PERCENT"
    HP_PERCENT = "HP_PERCENT"
    CRIT_RATE = "CRIT_RATE"
    CRIT_DMG = "CRIT_DMG"
    ENERGY_REGEN = "ENERGY_REGENERATION"

    # Elemental Damage Bonuses
    SPECTRO_DAMAGE = "SPECTRO_DAMAGE"
    HAVOC_DAMAGE = "HAVOC_DAMAGE"
    GLACIO_DAMAGE = "GLACIO_DAMAGE"
    FUSION_DAMAGE = "FUSION_DAMAGE"
    ELECTRO_DAMAGE = "SPECTRO_DAMAGE"
    AERO_DAMAGE = "AERO_DAMAGE"

    def __str__(self) -> str:
        return self.value

