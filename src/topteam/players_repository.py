from typing import TypeAlias

from topteam.models import Player

_PlayerId: TypeAlias = str


class PlayersRepository:
    def __init__(self) -> None:
        self._players_map: dict[_PlayerId, Player] = {}

    def save(self, p: Player) -> None:
        self._players_map[p.id] = p

    def find_by_id(self, _id: _PlayerId) -> Player:
        return self._players_map[_id]

    def find_all(self) -> list[Player]:
        return list(self._players_map.values())

    def find_by_ids(self, ids: list[_PlayerId]) -> list[Player]:
        result: list[Player] = []
        for id_ in ids:
            if player := self._players_map.get(id_):
                result.append(player)
        return result
