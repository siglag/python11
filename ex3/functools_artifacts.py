from functools import lru_cache, partial, reduce, singledispatch
from operator import add, mul
from typing import Callable, Any


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
        return 0


def partial_enchanter(base_spell: Callable, power: int) -> Callable:
    return partial(base_spell, power=power)


def memoized_fibonacci() -> Callable[[int], int]:
    @lru_cache(maxsize=None)
    def fib(n: int) -> int:
        if n < 2:
            return n
        return fib(n-1) + fib(n-2)
    return fib


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
