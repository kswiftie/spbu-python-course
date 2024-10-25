from typing import List, Dict, Callable, Any
import random

AVAILABLE_BETS = ["Black", "Red", "Even", "Odd", "Small", "Big", "Dozen", "Sixline", "Street", "Split",
                  "Straight Up"]

DOZENS = {1: lambda x: 0 < x < 13, 2: lambda x: 12 < x < 25, 3: lambda x: 24 < x}
WINNING_COEF = {"Black": lambda x: x, "Red": lambda x: x, "Even": lambda x: x, "Odd": lambda x: x, "Small": lambda x: x,
                "Big": lambda x: x, "Dozen": lambda x: x * 2, "Sixline": lambda x: x * 5, "Street": lambda x: x * 11,
                "Split": lambda x: x * 17,
                "Straight Up": lambda x: x * 35}
LOSING_COEF: Callable[[int], int] = lambda x: 0
BLACK = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
RED = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
AVAILABLE_GAME_RULES = [1]


def get_payment_based_on_bet(bettype: str) -> Callable[[int], int]:
    return WINNING_COEF[bettype]


class Table:
    """
    The class of the "table" of the roulette game
    It implements the game host

    """

    def __int__(self, rules: tuple[int, Any], **players) -> None:
        """
        *Description*

        Parameters
        ----------
        rules: int
            Variable for setting the rules in the game
            1 parameter is the type of rules, 2 parameter
            is the refinement of rules for those specified in 1 type
            The following types of rules are currently available:
            1 - The game will continue for a certain number of moves
        players: Dict[str, object]
            *description*
        """
        if rules[0] not in AVAILABLE_GAME_RULES:
            raise ValueError(f"Argument rules must be in {AVAILABLE_GAME_RULES}")
        self.rules = rules
        self.players: Dict[str, object] = players

    def get_round_results(self, bets: Dict[str, tuple]) -> Dict[str, Callable[[int], int]]:
        winners = {}
        result = random.randint(0, 36)
        for bettype, betvalues in bets.items():
            winners[bettype] = self.is_bet_win(bettype, betvalues, result)
        return winners

    def is_bet_win(self, bettype: str, betvalues: tuple[Any], result: int) -> Callable[[int], int]:
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
            return get_payment_based_on_bet(bettype) if DOZENS[betvalues[0]](result) else LOSING_COEF
        if bettype in ["Sixline", "Street", "Split", "Straight up"]:
            return get_payment_based_on_bet(bettype) if result in betvalues else LOSING_COEF

        return LOSING_COEF

    def start_the_game(self) -> None:
        if self.rules[0] == 1:
            self.game_with_rule_1(self.rules[1], self.rules[2])

    def game_with_rule_1(self, number_of_rounds, init_money) -> None:
        print("Game is starting...")
        print(f"""
Rules:
There will be {number_of_rounds} rounds in the game.
Initially, everyone has {init_money} money
""")
        print("The players at the table: ", end="")
        for x in self.players:
            print(x, end=" ")
        for round_number in range(number_of_rounds):
            print(f"The beginning of the {round_number} round. Place your bets")

    def add_player(self, player: tuple[str, object]) -> None:
        if player[0] in self.players:
            raise ValueError("A player with that name is already sitting at the table")
        print(f"Player {player[0]} sat down at the table")
        self.players[player[0]] = player[1]

    def remove_player(self, player: str) -> None:
        if player not in self.players:
            raise ValueError("There is no player with that name at the table")
        print(f"Player {player} left the table")
        self.players.pop(player)
