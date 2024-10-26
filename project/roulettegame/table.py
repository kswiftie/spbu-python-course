import random
from typing import List, Dict, Callable, Any
from .check_game_rules import check_game_rules
from .bot import Bot

AVAILABLE_BETS = [
    "Black",
    "Red",
    "Even",
    "Odd",
    "Small",
    "Big",
    "Dozen",
    "Sixline",
    "Street",
    "Split",
    "Straight Up",
]

DOZENS = {1: lambda x: 0 < x < 13, 2: lambda x: 12 < x < 25, 3: lambda x: 24 < x}
WINNING_COEF = {
    "Black": lambda x: x,
    "Red": lambda x: x,
    "Even": lambda x: x,
    "Odd": lambda x: x,
    "Small": lambda x: x,
    "Big": lambda x: x,
    "Dozen": lambda x: x * 2,
    "Sixline": lambda x: x * 5,
    "Street": lambda x: x * 11,
    "Split": lambda x: x * 17,
    "Straight Up": lambda x: x * 35,
}
LOSING_COEF: Callable[[int], int] = lambda x: -x
BLACK = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
RED = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
AVAILABLE_PLAYERS = Bot


def get_payment_based_on_bet(bettype: str) -> Callable[[int], int]:
    return WINNING_COEF[bettype]


class Table:
    """
    The class of the "table" of the roulette game
    It implements the game host

    """

    def __init__(
        self, game_rules: tuple[Any, ...], **players: AVAILABLE_PLAYERS
    ) -> None:
        """
        *Description*

        Parameters
        ----------
        game_rules: int
            For more information, see docs/Roulette/game_rules

        players: Dict[str, object]
            *description*
        """

        check_game_rules(game_rules)

        self.game_rules = game_rules
        self.players: Dict[str, AVAILABLE_PLAYERS] = players

    def get_round_results(
        self, bets: Dict[str, tuple[Any, ...]]
    ) -> Dict[str, Callable[[int], int]]:
        round_results = {}
        result = random.randint(0, 36)
        print(f"{result} on the wheel!")
        for player_name, (bettype, *betvalues) in bets.items():
            round_results[player_name] = self.is_bet_win(
                bettype, tuple(betvalues), result
            )
        return round_results

    def is_bet_win(
        self, bettype: str, betvalues: tuple[Any, ...], result: int
    ) -> Callable[[int], int]:
        if bettype not in AVAILABLE_BETS:
            raise ValueError("Unknown Bet")

        if bettype == "Red":
            return get_payment_based_on_bet(bettype) if result in RED else LOSING_COEF
        if bettype == "Black":
            return get_payment_based_on_bet(bettype) if result in BLACK else LOSING_COEF
        if bettype == "Even":
            return get_payment_based_on_bet(bettype) if result % 2 == 0 else LOSING_COEF
        if bettype == "Odd":
            return get_payment_based_on_bet(bettype) if result % 2 else LOSING_COEF
        if bettype == "Big":
            return get_payment_based_on_bet(bettype) if 18 < result else LOSING_COEF
        if bettype == "Small":
            return get_payment_based_on_bet(bettype) if 0 < result < 19 else LOSING_COEF
        if bettype == "Dozen":
            return (
                get_payment_based_on_bet(bettype)
                if DOZENS[betvalues[0]](result)
                else LOSING_COEF
            )
        if bettype in ["Sixline", "Street", "Split", "Straight up"]:
            return (
                get_payment_based_on_bet(bettype)
                if result in betvalues
                else LOSING_COEF
            )

        return LOSING_COEF

    def start_the_game(self) -> None:
        print("Game is starting...")
        if self.game_rules[0] == "ByMoves":
            self.game_with_rule_1(self.game_rules[1], self.game_rules[2])

    def game_with_rule_1(self, number_of_rounds: int, init_money: int) -> None:
        print(
            f"""
Rules:
There will be {number_of_rounds} rounds in the game.
Initially, everyone has {init_money} money
"""
        )
        print("The players at the table: ", end="")
        players_status = dict().fromkeys(self.players.keys(), init_money)
        eliminated_players = []
        for player_name in self.players:
            print(player_name, end=" ")

        for round_number in range(1, number_of_rounds + 1):
            print(f"\nPlayer's money at the beginning of the round {round_number}:")

            for (
                player_name,
                player_money,
            ) in players_status.items():  # Players stats of current round
                print(f"{player_name} have {player_money} coins")
                if player_money < 1 and player_name not in eliminated_players:
                    print(f"{player_name} lost. He's not betting anymore")
                    eliminated_players.append(player_name)

            print(f"\nThe beginning of the {round_number} round. Place your bets")
            bets_types, bets_amount = {}, {}
            for (
                player_name,
                player_money,
            ) in players_status.items():  # Getting bets from players
                bets_types[player_name], bets_amount[player_name] = self.players[
                    player_name
                ].play_game_with_rule1(round_number, player_money)
                print(f"Player {player_name} bet on {bets_types[player_name]}")

            round_results = self.get_round_results(bets_types)
            print("\nRound results:")
            for player_name, player_money in players_status.items():
                player_result = round_results[player_name](bets_amount[player_name])
                print(
                    f"{player_name} has won {player_result}"
                    if player_result > 0
                    else f"{player_name} has lost {-player_result}"
                )
                players_status[player_name] += player_result
        print("\nThe results of the game:")
        max_money = max(players_status.values())
        for player_name, player_money in players_status.items():
            print(f"Player {player_name} has {player_money} coins")

        # todo: Write that there are several winners, if there are several of them
        # bc now im writing them as if they didn't win together
        for player_name, player_money in players_status.items():
            if player_money == max_money:
                print(f"\nPlayer {player_name} won the game!")

    def add_player(self, player: tuple[str, AVAILABLE_PLAYERS]) -> None:
        if player[0] in self.players:
            raise ValueError("A player with that name is already sitting at the table")
        print(f"Player {player[0]} sat down at the table")
        self.players[player[0]] = player[1]

    def remove_player(self, player: str) -> None:
        if player not in self.players:
            raise ValueError("There is no player with that name at the table")
        print(f"Player {player} left the table")
        self.players.pop(player)
