from collections.abc import Callable
from functools import wraps
from typing import Any
import time


def spell_timer(func: Callable[..., str]) -> Callable[..., str]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> str:
        print(f"Casting {func.__name__}...")
        start_time = time.perf_counter()

        result = func(*args, **kwargs)

        elapsed_time = time.perf_counter() - start_time
        print(f"Spell completed in {elapsed_time:.3f} seconds")

        return result

    return wrapper


def power_validator(
    min_power: int,
) -> Callable[[Callable[..., str]], Callable[..., str]]:

    def decorator(func: Callable[..., str]) -> Callable[..., str]:
        @wraps(func)
        def wrapper(
            self: Any,
            spell_name: str,
            power: int
        ) -> str:
            if power < min_power:
                return "Insufficient power for this spell"

            return func(self, spell_name, power)

        return wrapper

    return decorator


def retry_spell(
    max_attempts: int,
) -> Callable[[Callable[..., str]], Callable[..., str]]:

    def decorator(func: Callable[..., str]) -> Callable[..., str]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> str:
            attempt = 0

            while attempt < max_attempts:
                attempt += 1

                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt != max_attempts:
                        print(
                            "Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                        )

            return (
                f"Spell casting failed after {max_attempts} attempts"
            )

        return wrapper

    return decorator


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False

        return all(char.isalpha() or char.isspace() for char in name)

    @power_validator(10)
    def cast_spell(
        self,
        spell_name: str,
        power: int
    ) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def fireball() -> str:
    time.sleep(0.1)
    return "Fireball cast!"


class SpellTester:

    def __init__(self) -> None:
        self.attempts = 0

    @retry_spell(3)
    def unstable_spell(self) -> str:
        self.attempts += 1

        if self.attempts < 3:
            raise ValueError("The spell failed!")

        return "Waaaaaaagh spelled !"


if __name__ == "__main__":

    print("Testing spell timer...")
    result = fireball()
    print(f"Result: {result}")

    print("\nTesting retry spell...")
    spell_tester = SpellTester()
    print(f"Result: {spell_tester.unstable_spell()}")

    print("\nTesting MageGuild...")
    guild = MageGuild()

    mage_names = ["Gandalf", "ab", "Dark Mage", "Fire123"]

    for name in mage_names:
        print(f"{name}: {MageGuild.validate_mage_name(name)}")

    print("\nTesting spell casting...")
    spells = [
        ("Lightning", 15),
        ("Fireball", 10),
        ("Ice Storm", 5),
    ]

    for spell_name, power in spells:
        print(guild.cast_spell(spell_name, power))
