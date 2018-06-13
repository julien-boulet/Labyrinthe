def check_map_choice(file_map_length):
    user_input_s = input("Entrez un numéro de labyrinthe pour commencer à jouer : ")
    try:
        user_input_i = int(user_input_s)
    except ValueError:
        print("Merci de choisir un chiffre entre 1 et {0}".format(file_map_length))
        return check_map_choice(file_map_length)

    if user_input_i < 1 or (user_input_i - 1) >= file_map_length:
        print("Merci de choisir un chiffre entre 1 et {0}".format(file_map_length))
        return check_map_choice(file_map_length)

    print("Vous avez choisi la carte", user_input_i)
    return user_input_i


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
