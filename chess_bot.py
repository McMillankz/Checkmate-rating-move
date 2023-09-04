# lip_KF49HPZT8GEgnRlk2LJG
import berserk
import chess.pgn
from datetime import datetime
import csv
from stockfish import Stockfish

stockfish = Stockfish(path='C:/Users/mcmil/OneDrive/Documents/Telegram bot/stockfish/stockfish.exe', depth=23)

# session = berserk.TokenSession("lip_KF49HPZT8GEgnRlk2LJG")
# client = berserk.Client(session=session)

# start = berserk.utils.to_millis(datetime(2023, 5, 25))
# end = berserk.utils.to_millis(datetime(2023, 8, 25))
# user_game = client.games.export_by_player('deniskorobitsin', since=start, until=end, max=300)

# games = list(user_game)
# number = 1
# while number != 100:
#     game_id = games[number]['id']
#     pgn = client.games.export(game_id, as_pgn=True)
#     with open (f"C:/Users/mcmil/OneDrive/Documents/Telegram bot/games/game{number}.pgn", "w") as f:
#         f.write(pgn)
#     number = number + 1

game = open("C:/Users/mcmil/OneDrive/Documents/Telegram bot/games/game2.pgn")
mygame = chess.pgn.read_game(game)
check = mygame.headers["White"]
if check == "deniskorobitsin":
        player_color = "White"
    else:
        player_color = "Black"

old_result = 0
n = 1
while mygame.next():
    mygame = mygame.next()
    n = n+1
    if player_color == "White" and n % 2 != 0:
        continue

    if player_color == "Black" and n % 2 == 0:
        continue
        
    position = mygame.board().fen()
    stockfish.set_fen_position(position)
    result = stockfish.get_evaluation()
    if int(result['value']) - int(old_result) > 200:
        message = f"Долбаеб, ты с {n//2} хода потерял преимущество..."
        print(message)
        break
    old_result = int(result['value'])



# user = "https://lichess.org/YQLfyWC2/black"
# user = user.replace("https://lichess.org/", "")

# if "/black" in user:
#     user = user.replace("/black", "")
#     player_color = "Black"
# else:
#     player_color = "White"



# pgn = open("denis.pgn")
# mygame=chess.pgn.read_game(pgn)
# n = 1
# old_result = 0
# while mygame.next():
#     mygame = mygame.next()
#     n = n+1
#     if player_color == "White" and n % 2 != 0:
#         continue

#     if player_color == "Black" and n % 2 == 0:
#         continue
    
#     position = mygame.board().fen()
#     stockfish.set_fen_position(position)
#     result = stockfish.get_evaluation()
#     if int(result['value']) - int(old_result) > 200:
#         print ("Долбаеб, ты с", n//2, "хода потерял преимущество...")
#         break
#     old_result = int(result['value'])