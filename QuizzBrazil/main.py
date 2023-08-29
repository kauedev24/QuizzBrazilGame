from turtle import Screen
from screen import ScreenGame
from game_data import names

screen_game = ScreenGame()  # configurações de tela



while True:
    user_input = screen_game.input_answer()  # caixa para entrada de dados
        
    for name in names:
        if user_input == name:
            print("OK")
        else:
            print("ERROR")
    




screen = Screen()
screen.exitonclick()

