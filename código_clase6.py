import os
from pathlib import Path
from os import system

my_path = Path(os.getcwd(), "Recetas")


def count_recipes(path):
    """counter = 0
    for txt in path.glob("**/*.txt"):
        counter += 1
    return counter"""
    # we can do it this way as well
    return sum(1 for txt in Path(path).glob("**/*.txt"))


def start():
    system("cls")
    print("\033[1;32mWelcome to our recipes book!\033[m")
    print(f"You can find the recipes in this path: {my_path}")
    print(f"There're {count_recipes(my_path)} recipes in our book.")
    option_index = "x"
    while not option_index.isnumeric() or int(option_index) not in range(1,7):
        print("\nChoose an option: ")
        options = ["Read recipe", "Create recipe", "Create category", "Delete recipe", "Delete category", "End program"]
        for i, option in enumerate(options, 1):
            print(f"[{i}] {option}")
        option_index = input()

    return int(option_index)


def show_categories(path):
    print("\nCategories: ")
    categories_path = Path(path)
    categories_list = []
    counter = 1

    for file in categories_path.iterdir():
        file_str = str(file.name)
        print(f"{counter} {file_str}")
        categories_list.append(file)
        counter += 1

    return categories_list


def choose_category(lista):
    option_index = "x"
    while not option_index.isnumeric() or int(option_index) not in range(1, len(lista) + 1):
        option_index = input("\nChoose a category: ")

    return lista[int(option_index) - 1]


def show_recipes(path):
    print("Recipes: ")
    path_recipes = Path(path)
    list_recipes = []
    counter = 1

    for recipe in path_recipes.glob("*.txt"):
        recipe_str = str(recipe.name)
        print(f"[{counter}] {recipe_str}")
        list_recipes.append(recipe)
        counter += 1

    return list_recipes


def choose_recipes(lista):
    recipe_choice = "x" #so that the condition to be followed is not met

    while not recipe_choice.isnumeric() or int(recipe_choice) not in range(1, len(lista) + 1):
        recipe_choice = input("\nChoose a recipe: ")

    return lista[int(recipe_choice) - 1]


def read_recipe(recipe):
    print(Path.read_text(recipe))


def creat_recipe(path):
    exist = False

    while not exist:
        print("Write the name of your recipe: ")
        recipe_name = input() + ".txt"
        print("Write the recipe: ")
        content_recipe = input()
        new_path = Path(path, recipe_name)

        if not os.path.exists(new_path):
            Path.write_text(new_path, content_recipe)
            print(f"Your recipe {recipe_name} were created successfully")
            exist = True
        else:
            print("This recipe already exists.")


def creat_category(path):
    exist = False

    while not exist:
        print("Write the name of the new category: ")
        category_name = input()
        new_path = Path(path, category_name)

        if not os.path.exists(new_path):
            Path.mkdir(new_path) #crear una nueva carpeta
            print(f"Your new category {category_name} were created successfully")
            exist = True
        else:
            print("This category already exists.")


def eliminate_recipe(recipe):
    Path(recipe).unlink()
    print(f"The recipe {recipe.name} were deleted successfully!")


def eliminate_category(category):
    Path(category).rmdir() #remove directory
    print(f"The category {category.name} were deleted successfully!")


def start_again():
    choice = "a"

    while choice.lower() != "x":
        choice = input("\nPress X to start the program again.")

end_program = False

while not end_program:

    menu = start()

    if menu == 1:
        categories = show_categories(my_path)
        my_category = choose_category(categories)
        my_recipes = show_recipes(my_category)
        my_recipe = choose_recipes(my_recipes)
        read_recipe(my_recipe)
        start_again()
    elif menu == 2:
        categories = show_categories(my_path)
        my_category = choose_category(categories)
        creat_recipe(my_category)
        start_again()
    elif menu == 3:
        creat_category(my_path)
        start_again()
    elif menu == 4:
        categories = show_categories(my_path)
        my_category = choose_category(categories)
        my_recipes = show_recipes(my_category)
        my_recipe = choose_recipes(my_recipes)
        eliminate_recipe(my_recipe)
        start_again()
    elif menu == 5:
        categories = show_categories(my_path)
        my_category = choose_category(categories)
        eliminate_category(my_category)
        start_again()
    elif menu == 6:
        end_program = True
