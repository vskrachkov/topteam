import itertools
from abc import abstractmethod
from typing import TypeAlias, Callable

from topteam.models import Player, Team, PlayersPair
from topteam.rules_repository import RulesRepository
from topteam.team_composition.pair_sorting_strategy import PairSortingStrategy

_TopTier: TypeAlias = list[Player]
_SeniorTier: TypeAlias = list[Player]
_MiddleTier: TypeAlias = list[Player]
_TiersTuple: TypeAlias = tuple[_TopTier, _SeniorTier, _MiddleTier]
_PairScorer: TypeAlias = Callable[[PlayersPair], int]


class TeamsCompositionStrategy:
    def __init__(
        self,
        players: list[Player],
        players_per_team: int,
        rules_repository: RulesRepository,
    ) -> None:
        self.teams_count = len(players) // players_per_team
        if self.teams_count < 2:
            raise ValueError("Not enough players to form teams for the match")

        self.players = players
        self.players_per_team = players_per_team
        self.rules_repository = rules_repository

    @abstractmethod
    def create_teams(self):
        raise NotImplementedError()


class TopPairsStrategy(TeamsCompositionStrategy):

    def create_teams(self) -> list[Team]:
        top_players, senior_players, middle_players = self.create_player_tiers()

        senior_pairs = self.combine_pairs(senior_players)
        top_senior_pairs = self.top_unique_pairs(
            senior_pairs, PairSortingStrategy(self.rules_repository)
        )

        middle_pairs = self.combine_pairs(middle_players)
        top_middle_pairs = self.top_unique_pairs(
            middle_pairs, PairSortingStrategy(self.rules_repository)
        )

        # top players
        teams = [Team(self.players_per_team) for _ in range(self.teams_count)]
        for team, top_player in zip(teams, top_players):
            team.add_player(top_player)

        # senior players
        pick_top_senior = False
        for team in teams:
            if pick_top_senior and top_senior_pairs:
                team.add_pair(top_senior_pairs.pop(0))
            elif top_senior_pairs:
                team.add_pair(top_senior_pairs.pop(-1))
            pick_top_senior = not pick_top_senior

        # middle players
        for team in teams:
            if pick_top_senior and top_middle_pairs:
                team.add_pair(top_middle_pairs.pop(-1))
            elif top_middle_pairs:
                team.add_pair(top_middle_pairs.pop(0))

            pick_top_senior = not pick_top_senior

        return teams

    def create_player_tiers(self) -> _TiersTuple:
        teams_count = len(self.players) // self.players_per_team
        sorted_by_rating: list[Player] = sorted(
            self.players, key=lambda player: player.rating(), reverse=True
        )
        top_players = sorted_by_rating[:teams_count]
        senior_players = sorted_by_rating[teams_count : teams_count + teams_count * 2]
        middle_players = sorted_by_rating[len(top_players) + len(senior_players) :]
        return top_players, senior_players, middle_players

    @staticmethod
    def combine_pairs(players: list[Player]) -> list[PlayersPair]:
        pairs: list[PlayersPair] = []
        for p in itertools.combinations(players, 2):
            pairs.append(PlayersPair(p[0], p[1]))
        return pairs

    @staticmethod
    def top_unique_pairs(
        pairs: list[PlayersPair], scorer: _PairScorer
    ) -> list[PlayersPair]:
        used_players: set[Player] = set()
        sorted_pairs: list[PlayersPair] = sorted(pairs, key=scorer, reverse=True)
        unique_pairs: list[PlayersPair] = []
        for pair in sorted_pairs:
            if pair.first in used_players or pair.second in used_players:
                continue
            unique_pairs.append(pair)
            used_players.add(pair.first)
            used_players.add(pair.second)
        return unique_pairs
