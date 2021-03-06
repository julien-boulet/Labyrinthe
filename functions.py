import os
import pickle
from labyrinth import Labyrinth
from actions.action import Drill, Build
from enums.ordinal import Ordinal


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
    accepted_action = [Drill.letter, Build.letter]
    accepted_ordinal = [member.letter for name, member in Ordinal.__members__.items()]
    accepted_input = accepted_ordinal + accepted_action
    accepted_input.append('Q')
    
    user_input_s = input(
        "Entrez une action {0} + un nombre facultatif ou {1} + {0} ou quitter avec 'Q' : ".format(accepted_ordinal, accepted_action)).upper()
    if len(user_input_s) < 1:
        print("Merci de choisir une lettre entre {0}".format(accepted_input))
        return enter_input()
    for i, char in enumerate(user_input_s):
        if i == 0:
            if not char.isalpha():
                print("Merci de choisir une lettre entre {0}".format(accepted_input))
                return enter_input()
            elif char not in accepted_input:
                print("Merci de choisir une lettre parmi {0}".format(accepted_input))
                return enter_input()
        else:
            if user_input_s[0] in accepted_action and len(user_input_s[1:]) > 1:
                print("Merci de choisir une direction {0} apres {1}".format(accepted_ordinal, accepted_action))
                return enter_input()
            elif user_input_s[0] in accepted_action and len(user_input_s[1:]) == 1 and not user_input_s[
                                                                                               1] in accepted_ordinal:
                print("Merci de choisir une direction {0} apres {1}".format(accepted_ordinal, accepted_action))
                return enter_input()
            elif user_input_s[0] not in accepted_action and not char.isdigit():
                print("Merci de choisir une lettre parmi {0} puis un nombre facultatif".format(accepted_input))
                return enter_input()

    return user_input_s[0], user_input_s[1:]


def save_labyrinth(labyrinth, save_directory):
    with open(save_directory + "save", "wb") as save_file:
        pickle.Pickler(save_file).dump(labyrinth)


def load_labyrinth(save_directory):
    if os.path.exists(save_directory + "save"):
        with open(save_directory + "save", "rb") as save_file:
            labyrinth = pickle.Unpickler(save_file).load()
            return True, labyrinth

    return False, None
