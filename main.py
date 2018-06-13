import os
import map
from functions import *

MAP_DIRECTORY = "./maps/"

fileList = [f[:-4].lower() for f in os.listdir(MAP_DIRECTORY) if f.lower().endswith(".txt")]

print("Bonjour, bienvenue dans le jeu Labyrinthe")
print("Merci de choisir une carte : ")

for i, fname in enumerate(fileList):
    print("{0} - {1}".format(i + 1, fname.rsplit('.', 1)[0]))

user_input_m = check_map_choice(len(fileList)) - 1

with open(MAP_DIRECTORY + fileList[user_input_m] + ".txt", 'r') as f:
    content = f.read()
    map = map.Map(fileList[user_input_m], content)

print(map.labyrinth.draw_it())

while True:
    user_input_g = enter_input()
    possible, win = map.labyrinth.move_robot(user_input_g)
    if not possible:
        print("!!!!!!!!! mouvement impossible !!!!!!!!!!!!!!!")
    if win:
        print("######### Vous avez gagné ####################")
        break
    print(map.labyrinth.draw_it())
