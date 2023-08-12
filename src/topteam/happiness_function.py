import itertools

from topteam.models import Team


class HappinessFactor:
    def __init__(self, weight: float = 1.0) -> None:
        self.weight = weight

    def __call__(self, teams: list[Team]) -> float:
        raise NotImplementedError()


class TeamsAreFull(HappinessFactor):
    def __call__(self, teams: list[Team]) -> float:
        for team in teams:
            if not team.is_full():
                return 0.0
        return 100


class DiffByTeamValuesFactor(HappinessFactor):
    def __call__(self, teams: list[Team]) -> float:
        if sum(self.get_values(teams)) == 0:
            return 0.0
        score = 1.0
        for x, y in list(itertools.combinations(self.get_values(teams), r=2)):
            diff = abs(x - y)
            if diff == 0:
                score += 1.0
                continue
            value = 1 / (diff * self.weight)
            score += round(value, 2)
        return score

    @staticmethod
    def get_values(teams: list[Team]) -> list[int]:
        raise NotImplementedError()


class DiffByDefenseFactor(DiffByTeamValuesFactor):
    @staticmethod
    def get_values(teams: list[Team]) -> list[int]:
        return [team.defense() for team in teams]


class DiffByOffenseFactor(DiffByTeamValuesFactor):
    @staticmethod
    def get_values(teams: list[Team]) -> list[int]:
        return [team.offense() for team in teams]


class DiffByPhysicalFactor(DiffByTeamValuesFactor):
    @staticmethod
    def get_values(teams: list[Team]) -> list[int]:
        return [team.physical() for team in teams]


class DiffByTeamPlayFactor(DiffByTeamValuesFactor):
    @staticmethod
    def get_values(teams: list[Team]) -> list[int]:
        return [team.team_play() for team in teams]


class DiffByVisionFactor(DiffByTeamValuesFactor):
    @staticmethod
    def get_values(teams: list[Team]) -> list[int]:
        return [team.vision() for team in teams]


class DiffByMentalityFactor(DiffByTeamValuesFactor):
    @staticmethod
    def get_values(teams: list[Team]) -> list[int]:
        return [team.mentality() for team in teams]


class DiffByTotalRatingFactor(DiffByTeamValuesFactor):
    @staticmethod
    def get_values(teams: list[Team]) -> list[int]:
        return [team.rating() for team in teams]


class HappinessFunction:
    def __init__(self, happiness_factors: list[HappinessFactor]) -> None:
        if not happiness_factors:
            raise ValueError("At leas one happiness factor must be provided")
        self.happiness_factors = happiness_factors

    def calculate_score(self, teams: list[Team]) -> float:
        result = sum([hf(teams) for hf in self.happiness_factors])
        print(f"happiness: {result}")
        return result
