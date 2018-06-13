import os
from labyrinth import *
from functions import *

MAP_DIRECTORY = "./maps/"
MAP_EXTENSION = ".txt"

fileList = [f[:-4].lower() for f in os.listdir(MAP_DIRECTORY) if f.lower().endswith(MAP_EXTENSION)]

print("Bonjour, bienvenue dans le jeu Labyrinthe")
print("Merci de choisir une carte : ")

for i, fname in enumerate(fileList):
    print("{0} - {1}".format(i + 1, fname.rsplit('.', 1)[0]))

user_input_m = check_map_choice(len(fileList)) - 1

with open(MAP_DIRECTORY + fileList[user_input_m] + MAP_EXTENSION, 'r') as f:
    content = f.read()
    labyrinth = Labyrinth.read_content(content)

print(labyrinth.draw_it())

while True:
    user_input_g = enter_input()
    possible, win = labyrinth.move_robot(user_input_g)
    if not possible:
        print("!!!!!!!!! mouvement impossible !!!!!!!!!!!!!!!")
    if win:
        print("######### Vous avez gagné ####################")
        break
    print(labyrinth.draw_it())
