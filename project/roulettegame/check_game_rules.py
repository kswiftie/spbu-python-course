from typing import Any

AVAILABLE_GAME_RULES = ["ByMoves"]


def check_game_rules(game_rules:tuple[Any, ...]) -> None:
    """
    Function to check the correctness of the game_rules parameter

    Parameters
    ----------
    game_rules: tuple[...]
        For more information, see docs/Roulette/game_rules

    Returns
    -------

    """
    if game_rules[0] not in AVAILABLE_GAME_RULES:
        raise ValueError(f"Argument game_rules must be in {AVAILABLE_GAME_RULES}")

    if game_rules[0] == "ByMoves":
        if len(game_rules) != 3 or type(game_rules[1]) is not int or type(game_rules[2]) is not int:
            raise ValueError(f"The game_rules parameter is set incorrectly. For more information, see docs/...")
