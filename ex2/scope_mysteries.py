from typing import Any
from collections.abc import Callable


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
        return f"{ench} {item}"

    return enchanter


def memory_vault() -> dict[str, Callable[..., Any]]:
    dictionary: dict[str, str] = {}

    def store(key: str, value: str) -> None:
        dictionary[key] = value

    def recall(key: str) -> str:
        try:
            return dictionary[key]
        except KeyError:
            return "Memory not found"

    return {"store": store, "recall": recall}


if __name__ == "__main__":
    print("Testing mags counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print("counter_a call 1:", counter_a())
    print("counter_a call 2:", counter_a())
    print("counter_b call 1:", counter_b())

    print("\nTesting spell accumulator...")
    accumulator_a = spell_accumulator(100)
    print(f"Base 100, add 20: {accumulator_a(20)}")
    print(f"Base 100, add 30: {accumulator_a(30)}")

    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    forzen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(forzen("Shield"))

    print("\nTesting memory vault...")
    vault = memory_vault()
    vault["store"]("secret", "42")
    print("store 'secret' = 42")
    print(f"recall 'secret': {vault['recall']('secret')}")
    print(f"recall 'unknown': {vault['recall']('unknown')}")
