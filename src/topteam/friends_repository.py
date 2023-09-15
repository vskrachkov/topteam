from topteam.models import Player


class FriendsRepository:
    def __init__(self):
        self.friends: list[list[Player]] = []

    def add_friends(self, friends: list[Player]) -> None:
        self.friends.append(friends)
