from typing import Callable


def spell_combiner(
        spell1: Callable[[str, int], str],
        spell2: Callable[[str, int], str]
        ) -> Callable[[str, int], tuple[str, str]]:
    return lambda target, power: (
        spell1(target, power),
        spell2(target, power)
    )


def power_amplifier(
        base_spell: Callable[[str, int], str],
        multiplier: int
        ) -> Callable[[str, int], str]:
    return lambda target, power: base_spell(target, power * multiplier)


def conditional_caster(
        condition: Callable[[str, int], bool],
        spell: Callable[[str, int], str]
        ) -> Callable[[str, int], str]:
    return lambda target, power: spell(target, power) if condition(
        target, power) else "Spell fizzled"


def spell_sequence(
        spells: list[Callable[[str, int], str]]
        ) -> Callable[[str, int], list[str]]:
    return lambda target, power: [spell(target, power) for spell in spells]
