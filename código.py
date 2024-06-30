import os
from pathlib import Path

print("\033[1;30;43m¡Welcome to our recipes book!\033[m")
my_path = Path(os.getcwd(), "Recetas")
print(f"The access path to the folder with the recipes is this: {my_path}")

def count_recipes(path):
    counter = 0
    for txt in Path(path).glob("**/*.txt"):
        counter += 1
    return counter


print("""
Choose an option:

[1] read recipe
[2] create a recipe
[3] create category
[4] delete a recipe
[5] delete a category
[6] end program
""")
while True:
    option = int(input("Option: "))
    if option == 6:
        break
    else:
        if option == 1:
            category = int(input("""
[1] meat
[2] salad
[3] pasta
[4] dessert

Which category you want (write the number of the option): """))
            if category == 1:
                meat_path = Path(my_path, "meat")
                for txt_file in meat_path.glob("*.txt"):
                    r = open(txt_file, "r")
                    print(r.read())
                print()



counter = count_recipes(my_path)
print(f"There's {counter} recipes in this book.")