from abc import abstractmethod

from topteam.models import Player
from topteam.rules_repository import RulesRepository


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
