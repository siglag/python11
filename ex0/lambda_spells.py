def artifact_sorter(artifacts: list[dict[str, int]]) -> list[dict[str, int]]:
    return sorted(
        artifacts,
        key=lambda x: x['power'],
        reverse=True
    )


def power_filter(mages: list[dict[str, int]],
                 min_power: int) -> list[dict[str, int]]:
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: f"* {x} *", spells))


def mage_stats(mages: list[dict[str, int]]) -> dict[str, int | float]:
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
