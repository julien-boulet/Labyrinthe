import os
from labyrinth import *
from functions import *

MAP_DIRECTORY = "./maps/"
MAP_EXTENSION = ".txt"
SAVE_DIRECTORY = "./save/"

save_files = os.listdir(SAVE_DIRECTORY)
map_files = [f[:-4].lower() for f in os.listdir(MAP_DIRECTORY) if f.lower().endswith(MAP_EXTENSION)]

print("Bonjour, bienvenue dans le jeu Labyrinthe")

load_save = False
if len(save_files) > 0:
    user_input_save = input("Voulez-vous charger la partie enregistrée ? [O/N]").upper()
    if user_input_save == 'O':
        result, labyrinth = load_labyrinth(SAVE_DIRECTORY)
        load_save = result

if not load_save:
    print("Merci de choisir une carte : ")

    for i, fname in enumerate(map_files):
        print("{0} - {1}".format(i + 1, fname.rsplit('.', 1)[0]))

    user_input_m = check_map_choice(len(map_files)) - 1

    with open(MAP_DIRECTORY + map_files[user_input_m] + MAP_EXTENSION, 'r') as f:
        content = f.read()
        labyrinth = Labyrinth(content)

    if len(labyrinth.exits) < 1:
        print("!!!!!!!!! carte invalide, il n'y a pas de sortie !!!!!!!!!!!!!!!")
        user_input_m = check_map_choice(len(map_files)) - 1

    if not labyrinth.robot:
        print("!!!!!!!!! carte invalide, il n'y a pas de robot !!!!!!!!!!!!!!!")
        user_input_m = check_map_choice(len(map_files)) - 1

while True:
    print(labyrinth.draw_it())
    user_input_c, user_input_n = enter_input()

    if user_input_c == 'Q':
        save_labyrinth(labyrinth, SAVE_DIRECTORY)
        print("Dommage de nous quitter :(")
        break

    possible, win = labyrinth.move_robot_number(user_input_c, user_input_n)

    if not possible:
        print("!!!!!!!!! mouvement impossible !!!!!!!!!!!!!!!")
    if win:
        print("######### Vous avez gagné ####################")
        break
