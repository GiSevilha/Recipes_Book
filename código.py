import os
from pathlib import Path


def print_welcome_message():
    print("\033[1;30;45mWelcome to our recipes book!\033[m")


def get_recipes_path():
    return Path(os.getcwd(), "Recetas")


def count_recipes(path):
    """counter = 0
    for txt in path.glob("**/*.txt"):
        counter += 1
    return counter"""
    # we can do it this way as well
    return sum(1 for txt in Path(path).glob("**/*.txt"))


def choose_option_menu():
    options = ["Read recipe", "Create recipe", "Create category", "Delete recipe", "Delete category", "End program"]
    print("\nWhich option from the menu do you want (write the number of the option)?")
    for i, option in enumerate(options, 1):
        print(f"[{i}] {option}")
    option_index = int(input()) - 1
    if 0 <= option_index <= len(options):
        return options[option_index]
    else:
        print("Invalid choice. Please write a valid number.")
        return options[option_index]


def choose_category():
    categories = ["meat", "salad", "pasta", "dessert"]
    print("\nWhich category do you want (write the number of the option):")
    for i, category in enumerate(categories, 1):
        print(f"[{i}] {category}")
    category_index = int(input()) - 1
    if 0 <= category_index <= len(categories):
        return categories[category_index]
    else:
        print("Invalid category. Please, choose a valid option.")
        return categories[category_index]


def read_recipe(my_path):
    """
    Pide al usuario seleccionar una categoría.
Comprueba si la carpeta de esa categoría existe.
Si existe, lista todos los archivos de recetas en esa carpeta.
Lee y muestra el contenido de cada archivo de receta.
Cierra cada archivo después de leerlo.
Muestra mensajes apropiados si no hay recetas o si la categoría no existe.
    :param my_path: donde se encuentran los archivos
    :return: devuelve lo que esta en los archivos que hay dentro de la carpeta con el nombre de la categoria elegida
    """
    category = choose_category()
    category_path = Path(my_path, category)
    if category_path.exists():
        recipes = list(category_path.glob("*.txt"))
        if recipes:
            print("\nAvailable recipes:")
            for i, txt_file in enumerate(recipes, 1):
                print(f"[{i}] {txt_file.stem}")
            choice = int(input("\nWhich recipe do you want to read? Enter the number: ")) - 1
            if 0 <= choice < len(recipes):
                txt_file = recipes[choice]
                file = open(txt_file, "r")
                try:
                    print(file.read())
                finally:
                    file.close()
            else:
                print("Invalid choice. Please select a valid recipe number.")
        else:
            print(f"No recipes found in the {category} category.")
    else:
        print(f"Category {category} does not exist.")


def creat_recipe():
    my_path = Path(get_recipes_path(), choose_category())
    file_name = str(input("What is the name of the new file? "))
    new_dir = my_path / f"{file_name}.txt"
    with open(new_dir, "w") as file:
        content_recipe = input("Please, write your recipe: ")
        file.write(content_recipe)
        print("\nArchivo creado con éxito")


def creat_category(category_name):
    my_path = Path(get_recipes_path() / category_name)
    my_path.mkdir()
    print("Categoty created successfully")


def delete_recipe(category, path):




category_name = input("Please, write the name of the new category: ")
creat_category(category_name)