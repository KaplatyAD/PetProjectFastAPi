from src.model.creature import Creature

_creatures = [
    Creature(name="Yeti",
             aka="Abominable Snowman",
             description="Hirsute Himalayan",
             country="CN",
             area="Himalayas"),
    Creature(name="Bigfoot",
             aka="Sasquatch",
             description="New world Cousin Eddie of the yeti",
             country="US",
             area="*"),
]


def get_all() -> list[Creature]:
    """returns a list of all creatures"""
    return _creatures


def get_one(name: str) -> Creature | None:
    for creature in _creatures:
        if creature.name == name:
            return creature
    return None


# The following are nonfunctional for now,
# so they just act like they work, without modifying
# the actual fake _explorers list:
# The following are nonfunctional for now,
# so they just act like they work, without modifying
# the actual fake _creatures list:
def create(creature: Creature) -> Creature:
    """Add a creature"""
    return creature


def modify(creature: Creature) -> Creature:
    """Partially modify a creature"""
    return creature


def replace(creature: Creature) -> Creature:
    """Completely replace a creature"""
    return creature


def delete(name: str):
    """Delete a creature; return None if it existed"""
    return None
