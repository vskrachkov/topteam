from topteam.happiness_function import HappinessFunction
from topteam.models import Team
from topteam.team_composition.teams_composition_strategy import TeamsCompositionStrategy


class TeamsComposer:
    def __init__(self, strategies: list[TeamsCompositionStrategy], happiness_function: HappinessFunction) -> None:
        if not strategies:
            raise ValueError("At least one strategy must be provided")
        self.strategies = strategies
        self.happiness_function = happiness_function

    def create_teams(self) -> list[Team]:
        candidates = [strategy.create_teams() for strategy in self.strategies]
        top_candidate = max(candidates, key=self.happiness_function.calculate_score)
        return top_candidate
