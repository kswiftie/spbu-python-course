# Available game rules

Currently, the following rule is available:

## 1. By Moves
This rule dictates a fixed number of rounds for the game. All players start with an equal amount of money. Players who lose all their money are no longer able to place bets.

#### Format: game_rules = ("ByMoves", number_of_moves, initial_money)

##### Aguments:
• name of the rule: always == "ByMoves"

• number_of_moves: The total number of rounds the game will last.

• initial_money: The starting amount of money each player receives. 

##### Example:
    game_rules = ("ByMoves", 10, 100)
This sets the game to last for 10 rounds, with each player starting with 100 units of currency.