import os
import chess.pgn

directory = "C:/Users/mcmil/OneDrive/Documents/Telegram bot/games"
file_list = os.listdir(directory)
for filename in file_list:
    file_path = os.path.join(directory, filename)
    with open(file_path, "r") as file:
        mygame = chess.pgn.read_game(file)
        white = mygame.headers["White"]
        black = mygame.headers["Black"]
        result = mygame.headers["Result"]
    if white == "deniskorobitsin" and result == "1-0":
            os.remove(file_path)
            print (f"Файл {file_path} был удален")
    elif black == "deniskorobitsin" and result == "0-1":
            os.remove(file_path)
            print (f"Файл {file} был удален")
    else:
        pass
