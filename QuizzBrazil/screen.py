from turtle import Screen

IMAGE = "QuizzBrazil/data/brasil_sem_estados.gif"

class ScreenGame:

    def __init__(self):
        self.screen = Screen()
        self.screen.title("Brazil Game")
        self.screen.bgpic(IMAGE)
        self.screen.setup(width=800, height=510)

    
    def input_answer(self):
        user_input = self.screen.textinput("Guess the State", "What's another state name?")
        return user_input
    
