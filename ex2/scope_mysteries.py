from typing import Callable


def mage_counter() -> Callable[[], int]:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    count = initial_power

    def counter(power: int) -> int:
        nonlocal count
        count += power
        return count

    return counter


def enchantment_factory(enchantment: str) -> Callable[[str], str]:
    ench = enchantment

    def enchanter(item: str) -> str:
        return f"{item} {ench}"

    return enchanter


def memory_vault() -> Callable[[str, str], dict[str, str]]:
    dictionary: dict[str, str] = {}

    def add(key: str, value: str) -> dict[str, str]:
        dictionary[key] = value
        return dictionary

    return add
