import pandas as pd

archive_csv = pd.read_csv("QuizzBrazil/data/estados.csv")

names = archive_csv["NAMES"]
print(type(names))