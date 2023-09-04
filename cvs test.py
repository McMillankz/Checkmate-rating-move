import os
import csv
import chess.pgn
from stockfish import Stockfish

directory = "C:/Users/mcmil/OneDrive/Documents/Telegram bot/games"
file_list = os.listdir(directory)
for filename in file_list:
    file_path = os.path.join(directory, filename)

    with open(file_path, "r") as file:
        stockfish = Stockfish(path='C:/Users/mcmil/OneDrive/Documents/Telegram bot/stockfish/stockfish.exe', depth=23)
        mygame = chess.pgn.read_game(file)
        url = mygame.headers["Site"]
        opening = mygame.headers["Opening"]

        if mygame.headers["White"] == "deniskorobitsin":
            player_color = "White"
        else:
            player_color = "Black"

        print(player_color)
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

        test = [
            {"Site": f"{url}", "Opening": f"{opening}", "Error": f"{message}"},
        ]
        with open('eggs.csv', "a", newline="", encoding="utf-8", errors="Ignore") as csvfile:
            fieldnames = test[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            for row in test:
                writer.writerow(row)