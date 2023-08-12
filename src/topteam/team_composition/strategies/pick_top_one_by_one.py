from topteam.models import Team, Player
from topteam.team_composition.strategies import TeamsCompositionStrategy


class PickTopOneByOneStrategy(TeamsCompositionStrategy):
    def create_teams(self) -> list[Team]:
        sorted_players: list[Player] = sorted(
            self.players, key=lambda player: player.rating(), reverse=True
        )
        teams_count = len(self.players) // self.players_per_team
        teams = [Team(self.players_per_team) for _ in range(teams_count)]
        while sorted_players:
            for team in teams:
                if not sorted_players:
                    break
                team.add_player(sorted_players.pop(0))
        return teams
