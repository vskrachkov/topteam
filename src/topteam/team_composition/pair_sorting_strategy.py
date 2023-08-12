from topteam.models import PlayersPair, Player
from topteam.rules_repository import RulesRepository


class PairSortingStrategy:
    def __init__(self, rules_repository: RulesRepository) -> None:
        self.rules_repository = rules_repository

    def __call__(self, pair: PlayersPair) -> int:
        return (
            pair.rating()
            + self.calc_modifier(pair.first, pair.second)
            + self.calc_modifier(pair.second, pair.first)
        )

    def calc_modifier(self, player_for: Player, player_with: Player) -> int:
        result = 0
        if modifiers_for_first := self.rules_repository.find_rules(
            player_for
        ):
            for m in modifiers_for_first:
                if m.player.id == player_with:
                    result += m.value
        return result
