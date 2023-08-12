from collections import defaultdict

from topteam.models import Player, Rule


class RulesRepository:
    def __init__(self) -> None:
        self._modifiers_map: defaultdict[Player, list[Rule]] = defaultdict(
            list
        )

    def save(self, player: Player, modifier: Rule) -> None:
        self._modifiers_map[player].append(modifier)

    def find_rules(self, player: Player) -> list[Rule]:
        return self._modifiers_map.get(player, [])
