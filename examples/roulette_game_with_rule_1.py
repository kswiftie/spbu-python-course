from project.roulettegame import Bot, Table

table = Table(("ByMoves", 3, 100), player_bot_1=Bot("Fibonacci"), player_bot_2=Bot("Fibonacci"))
table.start_the_game()
