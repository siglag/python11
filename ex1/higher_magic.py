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


if __name__ == "__main__":
    def heal(target: str, power: int) -> str:
        return f"Heal restores {target} for {power} HP"
    print("Testing spell combiner...")
    print(f"Combined spell result: {spell_combiner(heal, heal)('Alice', 10)}")
    print("\nTesting power amplifier...")
    print(f"Original: {heal('Alice', 10)}, Amplified: {
        power_amplifier(heal, 2)('Alice', 10)}")
    print("\nTesting conditional caster...")
    print(f"Conditional spell results: {
        conditional_caster(lambda t, p: p > 5, heal)('Alice', 10)}")
    print("\nTesting spell sequence...")
    print(f"Spell sequence results: {
        spell_sequence([heal, heal])('Alice', 10)}")
