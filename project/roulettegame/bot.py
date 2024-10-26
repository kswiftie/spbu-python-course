import random
from .get_random_seq import get_random_seq
from .get_fibbonacci_number import get_fibbonaccci_number
from typing import Any

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
AVAILABLE_GAME_STRATEGIES = ["Fibonacci"]


class Bot:
    def __init__(self, game_strategy: str) -> None:
        """
        *Descripsion*

        Parameters
        ----------

        game_strategy: int
            Stategy for a game

        Returns
        -------

        """

        if game_strategy not in AVAILABLE_GAME_STRATEGIES:
            raise ValueError(
                f"Argument game_strategy must be in {AVAILABLE_GAME_STRATEGIES}"
            )

        self.game_strategy = game_strategy
        self.cur_fubonacci_index = 1
        self.cur_money = 0  # Later, perhaps, they can be
        # installed during the initialization of the bot

    def play_game_with_rule1(
        self, round_number: int, cur_money: int
    ) -> tuple[Any, ...]:
        """

        Parameters
        ----------
        round_number
        cur_money

        Returns
        -------
        tuple:
            bets_type, bets_amount

        """
        if round == 1:
            self.cur_money = cur_money
            self.cur_fubonacci_index = 1
            return self.get_bet(), get_fibbonaccci_number(self.cur_fubonacci_index)

        if self.cur_money < cur_money:
            self.cur_fubonacci_index = max(1, self.cur_fubonacci_index - 2)
        else:
            self.cur_fubonacci_index += 1

        return self.get_bet(), get_fibbonaccci_number(self.cur_fubonacci_index)

    def get_bet(self) -> tuple[Any, ...]:
        """
        A function that randomly generates a bet

        Returns
        -------
        bet: tuple
            A tuple format bid, where the first parameter
            is the name of the bid, and then, if required, the cell numbers
        """
        bet = AVAILABLE_BETS[random.randint(0, len(AVAILABLE_BETS) - 1)]
        if bet == "Dozen":
            return bet, random.randint(1, 3)
        elif bet == "Sixline":
            return bet, get_random_seq(6, 1, 36)
        elif bet == "Street":
            return bet, get_random_seq(3, 1, 36)
        elif bet == "Split":
            return bet, get_random_seq(2, 1, 36)
        elif bet == "Straight Up":
            return bet, random.randint(1, 36)

        return tuple([bet])

    def change_strategy(self) -> None:
        # TBA (probably)
        pass
