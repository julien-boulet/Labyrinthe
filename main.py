from functions import check_map_choice, enter_input, save_labyrinth, load_labyrinth

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

    labyrinth = check_map_choice(map_files, MAP_DIRECTORY, MAP_EXTENSION)

while True:
    print(labyrinth.draw_it())
    user_input_1, user_input_2 = enter_input()

    if user_input_1 == 'Q':
        save_labyrinth(labyrinth, SAVE_DIRECTORY)
        print("Dommage de nous quitter :(")
        break
    if user_input_1 == Drill.letter:
        win = False
        enum_ordinal = Ordinal.find_by_letter(user_input_2)
        possible = labyrinth.drill_wall(enum_ordinal)
    elif user_input_1 == Build.letter:
        win = False
        enum_ordinal = Ordinal.find_by_letter(user_input_2)
        possible = labyrinth.build_wall(enum_ordinal)
    else:
        enum_ordinal = Ordinal.find_by_letter(user_input_1)
        possible, win = labyrinth.move_robot_number(enum_ordinal, user_input_2)

    if not possible:
        print("!!!!!!!!! mouvement impossible !!!!!!!!!!!!!!!")
    if win:
        print("######### Vous avez gagné ####################")
        break
