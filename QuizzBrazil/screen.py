import turtle as t

IMAGE = "QuizzBrazil/data/brasil_sem_estados.gif"

def settings_screen():
    screen = t.Screen()
    screen.title("Brazil Game")
    screen.bgpic(IMAGE)
    screen.setup(width=800, height=510)