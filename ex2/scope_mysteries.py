from typing import Callable


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable:
    count = initial_power

    def counter(power: int) -> int:
        nonlocal count
        count += power
        return count

    return counter


def enchantment_factory(enchantment: str) -> Callable:
    ench = enchantment

    def enchanter(item: str) -> str:
        return f"{item} {ench}"

    return enchanter


def memory_vault() -> Callable:
    dictionary: dict = {}

    def add(key: str, value: str) -> dict:
        dictionary[key] = value
        return dictionary

    return add
