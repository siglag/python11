from typing import Any


def artifact_sorter(
        artifacts: list[dict[str, Any]]
        ) -> list[dict[str, Any]]:
    return sorted(
        artifacts,
        key=lambda x: x['power'],
        reverse=True
    )


def power_filter(mages: list[dict[str, Any]],
                 min_power: Any) -> list[dict[str, Any]]:
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: f"* {x} *", spells))


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, Any]:
    return dict({
        "max_power": max(
                        mages, key=lambda x: x["power"]
                    )["power"] if mages else 0,
        "min_power": min(
                        mages, key=lambda x: x["power"]
                    )["power"] if mages else 0,
        "avg_power": round(sum(map(lambda x: x["power"], mages)) / len(
            mages) if mages else 0, 2)
    })


if __name__ == "__main__":
    print("Testing artifact sorter...")
    artifacts = [
        {'name': 'Lightning Rod', 'power': 69, 'type': 'weapon'},
        {'name': 'Water Chalice', 'power': 95, 'type': 'armor'},
        {'name': 'Storm Crown', 'power': 84, 'type': 'weapon'},
        {'name': 'Storm Crown', 'power': 100, 'type': 'relic'},
    ]
    print(f"testing: {artifacts}")
    print(f"result: {artifact_sorter(artifacts)}")

    print("\nTesting power filter...")
    mages = [
        {'name': 'Casey', 'power': 92, 'element': 'lightning'},
        {'name': 'Riley', 'power': 86, 'element': 'earth'},
        {'name': 'Phoenix', 'power': 81, 'element': 'water'},
        {'name': 'Luna', 'power': 67, 'element': 'water'},
        {'name': 'Alex', 'power': 86, 'element': 'wind'}
    ]
    print(f"original: {mages}")
    print(f"results: {power_filter(mages, 90)}")

    print("\nTesting spell transformer...")
    spells = ['flash', 'meteor', 'lightning', 'earthquake']
    print(f"original: {spells}")
    print(f"result: {spell_transformer(spells)}")

    print("\nTesting mage stats...")
    print(f"original: {mages}")
    print(f"result: {mage_stats(mages)}")
