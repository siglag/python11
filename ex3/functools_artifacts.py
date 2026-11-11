from functools import lru_cache, partial, reduce, singledispatch
from operator import add, mul
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    operations: dict[str, Callable[[list[int]], int]] = {
        "add": lambda x: reduce(
            add, x) if len(spells) > 0 else 0,
        "multiply": lambda x: reduce(
            mul, x) if len(spells) > 0 else 0,
        "max": lambda numbers: max(numbers) if len(spells) > 0 else 0,
        "min": lambda numbers: min(numbers) if len(spells) > 0 else 0,
    }
    try:
        return operations[operation](spells)
    except KeyError:
        raise ValueError(f"Unknown operation: {operation}")


def partial_enchanter(
        base_enchantment: Callable[..., str]
        ) -> dict[str, Callable[..., str]]:
    return {
        "fire": partial(base_enchantment, 50, "fire"),
        "water": partial(base_enchantment, 50, "water"),
        "earth": partial(base_enchantment, 50, "earth"),
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:

    @singledispatch
    def dispatcher(spell: Any) -> str:
        return "Unknown spell type"

    @dispatcher.register(int)
    def _(spell: int) -> str:
        return f"{spell} damage"

    @dispatcher.register(str)
    def _(spell: str) -> str:
        return f"{spell} enchantment"

    @dispatcher.register(list)
    def _(spell: list[int]) -> str:
        return f"{len(spell)} spells"

    return dispatcher


if __name__ == "__main__":
    print("Testing spell reducer...")
    spells = [10, 20, 30, 40]

    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")
    print(f"Min: {spell_reducer(spells, 'min')}")

    print("\nTesting partial enchanter...")

    def base_enchantment(power: int, element: str, target: str) -> str:
        return f"{target} receives {power} {element} power"

    enchantments = partial_enchanter(base_enchantment)

    print(enchantments["fire"]("dragon"))
    print(enchantments["water"]("wizard"))
    print(enchantments["earth"]("golem"))

    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print(f"Cache info: {memoized_fibonacci.cache_info()}")

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()

    print(f"Damage spell: {dispatcher(42)}")
    print(f"Enchantment: {dispatcher('fireball')}")
    print(f"Multi-cast: {dispatcher([1, 2, 3])}")
    print(dispatcher(3.14))
