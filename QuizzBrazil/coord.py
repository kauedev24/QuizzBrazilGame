import pandas as pd

coordenadas_x = [77.0, 47.0, 69.0, 23.0, 7.0, 95.0, 201.0, -110.0, -74.0, 29.0, 42.0, 83.0, 125.0, 243.0,      
                238.0, 213.0, 233.0, 223.0, 164.0, 131.0, 160.0, 69.0, 93.0, 66.0, 154.0, 192.0, 
                187.0]

coordenadas_y = [-91.0, -121.0, -155.0, -184.0, -67.0, 45.0, 67.0, 131.0, 206.0, 121.0, 193.0, 56.0,  
                120.0, 111.0, 91.0, 74.0, 58.0, 46.0, 32.0, -50.0, -95.0, -16.0, -16.0, -30.0, 
                77.0, 122.0, -61.0]      



estados = pd.read_csv("QuizzBrazil/data/estados.csv")
estados.insert(1, "x", coordenadas_x)
estados.insert(2, "y", coordenadas_y)

estados.to_csv("QuizzBrazil/data/estados.csv")