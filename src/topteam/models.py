from dataclasses import dataclass, field


@dataclass(frozen=True)
class Player:
    id: str
    name: str
    defense: int
    offense: int
    physical: int
    team_play: int
    vision: int
    mentality: int

    def __hash__(self) -> int:
        return hash(self.id)

    def __str__(self) -> str:
        return f"*{self.rating()} ({self.name})"

    def __repr__(self) -> str:
        return self.__str__()

    def rating(self) -> int:
        return (
            self.defense + self.offense + self.team_play + self.physical + self.vision
        )


@dataclass
class PlayersPair:
    first: Player
    second: Player

    def __str__(self) -> str:
        return f"*{self.rating()} ({self.first}, {self.second})"

    def __repr__(self) -> str:
        return self.__str__()

    def rating(self) -> int:
        return self.first.rating() + self.second.rating()


@dataclass
class Team:
    players_count: int
    starting_lineup: list[Player] = field(default_factory=list)
    substitutes: list[Player] = field(default_factory=list)

    def is_full(self) -> bool:
        return len(self.starting_lineup) >= self.players_count

    def add_player(self, p: Player) -> None:
        if self.is_full():
            self.substitutes.append(p)
        else:
            self.starting_lineup.append(p)

    def add_pair(self, p: PlayersPair) -> None:
        self.add_player(p.first)
        self.add_player(p.second)

    def rating(self) -> int:
        return sum([p.rating() for p in (self.starting_lineup + self.substitutes)])

    def offense(self) -> int:
        return sum([p.offense for p in (self.starting_lineup + self.substitutes)])

    def defense(self) -> int:
        return sum([p.defense for p in (self.starting_lineup + self.substitutes)])

    def physical(self) -> int:
        return sum([p.physical for p in (self.starting_lineup + self.substitutes)])

    def team_play(self) -> int:
        return sum([p.team_play for p in (self.starting_lineup + self.substitutes)])

    def vision(self) -> int:
        return sum([p.vision for p in (self.starting_lineup + self.substitutes)])

    def mentality(self) -> int:
        return sum([p.mentality for p in (self.starting_lineup + self.substitutes)])

    def __repr__(self) -> str:
        main_lineup = "\n".join([str(p) for p in self.starting_lineup])
        substitutes = "\n".join([str(p) for p in self.substitutes])
        return (
            f"rating:{self.rating()} "
            f"offense: {self.offense()} "
            f"defense: {self.defense()} "
            f"physical: {self.physical()} "
            f"team play: {self.team_play()} "
            f"vision: {self.vision()} "
            f"mentality: {self.mentality()}\n"
            f"{main_lineup}\n"
            f"---"
            f"\n{substitutes}"
        )


@dataclass
class Rule:
    player: Player
    value: int
