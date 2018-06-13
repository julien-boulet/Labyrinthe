import os
import pickle
from labyrinth import *


def check_map_choice(map_files, map_directory, map_extension):
    file_map_length = len(map_files)

    user_input_s = input("Entrez un numéro de labyrinthe pour commencer à jouer : ")
    try:
        user_input_i = int(user_input_s)
    except ValueError:
        print("Merci de choisir un chiffre entre 1 et {0}".format(file_map_length))
        return check_map_choice(map_files, map_directory, map_extension)

    if user_input_i < 1 or (user_input_i - 1) >= file_map_length:
        print("Merci de choisir un chiffre entre 1 et {0}".format(file_map_length))
        return check_map_choice(map_files, map_directory, map_extension)

    print("Vous avez choisi la carte", user_input_i)

    with open(map_directory + map_files[user_input_i - 1] + map_extension, 'r') as f:
        labyrinth = Labyrinth(f.read())

    if len(labyrinth.exits) < 1:
        print("!!!!!!!!! carte invalide, il n'y a pas de sortie !!!!!!!!!!!!!!!")
        return check_map_choice(map_files, map_directory, map_extension)

    if not labyrinth.robot:
        print("!!!!!!!!! carte invalide, il n'y a pas de robot !!!!!!!!!!!!!!!")
        return check_map_choice(map_files, map_directory, map_extension)

    return labyrinth


def enter_input():
    acceptabled_input = ['N', 'S', 'E', 'O', 'Q']

    user_input_s = input("Entrez une action {0} + un nombre facultatif: ".format(acceptabled_input)).upper()
    if len(user_input_s) < 1:
        print("Merci de choisir une lettre entre {0}".format(acceptabled_input))
        return enter_input()
    for i, char in enumerate(user_input_s):
        if i == 0:
            if not char.isalpha():
                print("Merci de choisir une lettre entre {0}".format(acceptabled_input))
                return enter_input()
            elif not char in acceptabled_input:
                print("Merci de choisir une lettre parmi {0}".format(acceptabled_input))
                return enter_input()
        else:
            if not char.isdigit():
                print("Merci de choisir une lettre parmi {0} puis un nombre facultatif".format(acceptabled_input))
                return enter_input()

    return user_input_s[0], user_input_s[1:]


def save_labyrinth(labyrinth, save_directory):
    with open(save_directory + "save", "wb") as save_file:
        mon_pickler = pickle.Pickler(save_file)
        mon_pickler.dump(labyrinth)
        save_file.close()


def load_labyrinth(save_directory):
    if os.path.exists(save_directory + "save"):
        with open(save_directory + "save", "rb") as save_file:
            mon_depickler = pickle.Unpickler(save_file)
            labyrinth = mon_depickler.load()
            save_file.close()
            return True, labyrinth

    return False, None
