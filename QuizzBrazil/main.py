# from turtle import Screens
from screen import ScreenGame
from game_data import names

screen_game = ScreenGame()  # configurações de tela



while True:
    user_input = screen_game.input_answer()  # caixa para entrada de dados
        
    
    if user_input in names:
        print("OK")
    else:
        print("NOT OK")
    




# screen = Screen()
# screen.exitonclick()

