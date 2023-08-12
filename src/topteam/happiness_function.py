from topteam.models import Team


class HappinessFactor:
    def __call__(self, teams: list[Team]) -> float:
        return 1.0


class HappinessFunction:
    def __init__(self, happiness_factors: list[HappinessFactor]) -> None:
        if not happiness_factors:
            raise ValueError("At leas one happiness factor must be provided")
        self.happiness_factors = happiness_factors

    def calculate_score(self, teams: list[Team]) -> float:
        return sum([hf(teams) for hf in self.happiness_factors])
