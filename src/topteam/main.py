from topteam.happiness_function import (
    HappinessFunction,
    DiffByDefenseFactor,
    DiffByOffenseFactor,
    DiffByPhysicalFactor,
    DiffByTeamPlayFactor,
    DiffByVisionFactor,
    DiffByMentalityFactor,
    DiffByTotalRatingFactor, TeamsAreFull,
)
from topteam.models import Player, Rule
from topteam.players_repository import PlayersRepository
from topteam.rules_repository import RulesRepository
from topteam.team_composition.composer import TeamsComposer
from topteam.team_composition.strategies import TopPairsStrategy
from topteam.team_composition.strategies.pick_top_one_by_one import PickTopOneByOneStrategy

players_repository = PlayersRepository()
players_repository.save(Player('4d654ffe-b901-4cad-afc7-ebeb8cfa06a3', 'Bohdan Sheketa', defense=2, offense=2, team_play=2, physical=2, vision=2, mentality=1))
players_repository.save(Player('dabba36d-0e84-4146-80a9-f3e37bc7c25d', 'Bohdan Shelest', defense=2, offense=4, team_play=3, physical=2, vision=3, mentality=3))
players_repository.save(Player('a3b711af-01ae-4fea-8dbf-4abd8e5b5eef', 'Dima Akimov', defense=2, offense=2, team_play=2, physical=2, vision=2, mentality=1))
players_repository.save(Player('a1014b25-ddd9-43ec-9d35-0614416661cb', 'Sasha', defense=3, offense=3, team_play=2, physical=2, vision=2, mentality=3))
players_repository.save(Player('34542d1c-fb56-40d9-b13f-9cd97dd15ba0', 'Yarik', defense=4, offense=5, team_play=5, physical=5, vision=3, mentality=4))
players_repository.save(Player('33a4b21b-785a-4943-9b1a-3ab4f72f7dce', 'Denver (Oleh)', defense=2, offense=3, team_play=3, physical=1, vision=4, mentality=2))
players_repository.save(Player('0d206713-915f-4d9f-92e1-8ad9d176a1de', 'Rudiy (Ihor)', defense=3, offense=3, team_play=2, physical=3, vision=3, mentality=2))
players_repository.save(Player('d021718e-33c0-4712-b4b4-2211d75edf77', 'Artur', defense=3, offense=3, team_play=4, physical=2, vision=3, mentality=2))
players_repository.save(Player('03c39eae-bad7-4c89-aa6f-2a29f06e1e79', 'Stas', defense=4, offense=3, team_play=4, physical=3, vision=3, mentality=2))
players_repository.save(Player('bd427f45-ef20-4325-b24a-5d5a581d7379', 'Tolik', defense=3, offense=3, team_play=4, physical=3, vision=3, mentality=3))
players_repository.save(Player('17ee46e2-5dd2-481a-97c7-e539393ebfc7', 'Rusik', defense=3, offense=3, team_play=3, physical=3, vision=3, mentality=3))
players_repository.save(Player('8caa92a3-fd22-47e0-b798-799b8cb4bea9', 'Slavko', defense=4, offense=4, team_play=4, physical=4, vision=4, mentality=4))
players_repository.save(Player('4b249bc6-a0c0-4c43-b501-222fc3f09547', 'Dmytro (Artur)', defense=3, offense=3, team_play=3, physical=2, vision=3, mentality=2))
players_repository.save(Player('6be22f3f-30a7-4afc-995c-f80a23c40b5a', 'Max (Dmytro)', defense=4, offense=5, team_play=5, physical=4, vision=5, mentality=3))
players_repository.save(Player('a2b04543-31b8-4d43-bf75-45f8b21f4eb5', 'Serhii (Artur)', defense=2, offense=2, team_play=2, physical=2, vision=2, mentality=3))
players_repository.save(Player('7305e144-4385-4607-8c85-f9d108876357', 'Valik Gisunov', defense=3, offense=3, team_play=3, physical=2, vision=3, mentality=3))
players_repository.save(Player('7d536174-1763-4517-9960-7062d880145b', 'Andrew (ChiTrip)', defense=3, offense=4, team_play=4, physical=5, vision=3, mentality=3))
players_repository.save(Player('603cb7f4-6163-467c-98d4-3d10915d00d5', 'Yarik (Andrew)', defense=3, offense=3, team_play=4, physical=4, vision=3, mentality=3))
players_repository.save(Player('6aab89bf-f479-4be6-b3a2-0401815ae678', 'Vlad Syrota', defense=5, offense=4, team_play=5, physical=3, vision=4, mentality=4))
players_repository.save(Player('00ab89bf-f479-4be6-b3a2-0401815ae678', 'Oleg (Tolik +1)', defense=4, offense=4, team_play=4, physical=5, vision=4, mentality=3))
players_repository.save(Player('113b89bf-f479-4be6-b3a2-0401815ae678', 'Vladimir (Serhii +1)', defense=3, offense=3, team_play=4, physical=3, vision=4, mentality=3))
players_repository.save(Player('333b89bf-f479-4be6-b3a2-0401815ae678', 'Serhii (Serhii +1)', defense=3, offense=3, team_play=2, physical=2, vision=3, mentality=2))
players_repository.save(Player('444489bf-2479-4be6-b3a2-0401815ae678', 'Vladislav (real estate)', defense=3, offense=3, team_play=2, physical=2, vision=2, mentality=2))
players_repository.save(Player('544489bf-2479-4be6-b3a2-0401815ae678', 'Chi One (Jeniok)', defense=3, offense=2, team_play=2, physical=2, vision=2, mentality=4))
players_repository.save(Player('424489bf-2479-4be6-b3a2-0401815ae678', 'Andriy (Dmytro)', defense=3, offense=4, team_play=3, physical=2, vision=3, mentality=3))
players_repository.save(Player('314489bf-2479-4be6-b3a2-0401815ae678', 'Oleksandr (Artur)', defense=5, offense=4, team_play=5, physical=3, vision=5, mentality=2))
players_repository.save(Player('111189b0-2479-4be6-b3a2-0401815ae678', 'Dmytro Lukin', defense=3, offense=3, team_play=3, physical=3, vision=3, mentality=3))


rules_repository = RulesRepository()
rules_repository.save(players_repository.find_by_id('4d654ffe-b901-4cad-afc7-ebeb8cfa06a3'), Rule(players_repository.find_by_id('0d206713-915f-4d9f-92e1-8ad9d176a1de'), -10))
rules_repository.save(players_repository.find_by_id('17ee46e2-5dd2-481a-97c7-e539393ebfc7'), Rule(players_repository.find_by_id('8caa92a3-fd22-47e0-b798-799b8cb4bea9'), +1))
rules_repository.save(players_repository.find_by_id('a3b711af-01ae-4fea-8dbf-4abd8e5b5eef'), Rule(players_repository.find_by_id('8caa92a3-fd22-47e0-b798-799b8cb4bea9'), +1))
rules_repository.save(players_repository.find_by_id('a3b711af-01ae-4fea-8dbf-4abd8e5b5eef'), Rule(players_repository.find_by_id('603cb7f4-6163-467c-98d4-3d10915d00d5'), +2))
rules_repository.save(players_repository.find_by_id('d021718e-33c0-4712-b4b4-2211d75edf77'), Rule(players_repository.find_by_id('8caa92a3-fd22-47e0-b798-799b8cb4bea9'), +1))
rules_repository.save(players_repository.find_by_id('03c39eae-bad7-4c89-aa6f-2a29f06e1e79'), Rule(players_repository.find_by_id('8caa92a3-fd22-47e0-b798-799b8cb4bea9'), +1))
rules_repository.save(players_repository.find_by_id('17ee46e2-5dd2-481a-97c7-e539393ebfc7'), Rule(players_repository.find_by_id('8caa92a3-fd22-47e0-b798-799b8cb4bea9'), +1))
rules_repository.save(players_repository.find_by_id('8caa92a3-fd22-47e0-b798-799b8cb4bea9'), Rule(players_repository.find_by_id('17ee46e2-5dd2-481a-97c7-e539393ebfc7'), +1))
rules_repository.save(players_repository.find_by_id('8caa92a3-fd22-47e0-b798-799b8cb4bea9'), Rule(players_repository.find_by_id('03c39eae-bad7-4c89-aa6f-2a29f06e1e79'), +1))
rules_repository.save(players_repository.find_by_id('8caa92a3-fd22-47e0-b798-799b8cb4bea9'), Rule(players_repository.find_by_id('bd427f45-ef20-4325-b24a-5d5a581d7379'), +1))
rules_repository.save(players_repository.find_by_id('8caa92a3-fd22-47e0-b798-799b8cb4bea9'), Rule(players_repository.find_by_id('d021718e-33c0-4712-b4b4-2211d75edf77'), +1))
rules_repository.save(players_repository.find_by_id('4b249bc6-a0c0-4c43-b501-222fc3f09547'), Rule(players_repository.find_by_id('d021718e-33c0-4712-b4b4-2211d75edf77'), +1))
rules_repository.save(players_repository.find_by_id('a2b04543-31b8-4d43-bf75-45f8b21f4eb5'), Rule(players_repository.find_by_id('d021718e-33c0-4712-b4b4-2211d75edf77'), +1))
rules_repository.save(players_repository.find_by_id('603cb7f4-6163-467c-98d4-3d10915d00d5'), Rule(players_repository.find_by_id('34542d1c-fb56-40d9-b13f-9cd97dd15ba0'), +1))


def main() -> None:
    players_per_team = 5
    players = players_repository.find_by_ids(
        [
            "00ab89bf-f479-4be6-b3a2-0401815ae678",
            "bd427f45-ef20-4325-b24a-5d5a581d7379",
            "4b249bc6-a0c0-4c43-b501-222fc3f09547",
            "4d654ffe-b901-4cad-afc7-ebeb8cfa06a3",
            "8caa92a3-fd22-47e0-b798-799b8cb4bea9",
            "caa92a3-fd22-47e0-b798-799b8cb4bea9",
            "0d206713-915f-4d9f-92e1-8ad9d176a1de",
            "d021718e-33c0-4712-b4b4-2211d75edf77",
            "a2b04543-31b8-4d43-bf75-45f8b21f4eb5",
            "314489bf-2479-4be6-b3a2-0401815ae678",
            "a3b711af-01ae-4fea-8dbf-4abd8e5b5eef",
            "444489bf-2479-4be6-b3a2-0401815ae678",
            "6aab89bf-f479-4be6-b3a2-0401815ae678",
            "424489bf-2479-4be6-b3a2-0401815ae678",
            "111189b0-2479-4be6-b3a2-0401815ae678",
        ]
    )
    strategies = [
        TopPairsStrategy(players, players_per_team, rules_repository),
        PickTopOneByOneStrategy(players, players_per_team, rules_repository)
    ]
    happiness_function = HappinessFunction([
        DiffByDefenseFactor(),
        DiffByOffenseFactor(),
        DiffByPhysicalFactor(weight=1.0),
        DiffByTeamPlayFactor(weight=1.0),
        DiffByVisionFactor(),
        DiffByMentalityFactor(weight=1.0),
        DiffByTotalRatingFactor(),
        TeamsAreFull(),
    ])
    composer = TeamsComposer(strategies, happiness_function)
    teams = composer.create_teams()
    for team in teams:
        print(team)
        print()


if __name__ == "__main__":
    main()
