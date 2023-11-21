import os
import random
import shutil

generate_folder_path = "data" # Replace this with the path to your folder where you want the files to be generated

def generate_random_name():
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "," "," "," "," "," "," "," ",]
    name = ""
    for i in range(1,10):
        name+=random.choice(letters)

    return name.strip()

def create_files():
    # Create a subdirectory named "data" if it doesn't exist
    if not os.path.exists(generate_folder_path):
        os.makedirs(generate_folder_path)

    for i in range(1, 1001):
        if i % 100 == 1:
            # Create a new set of words for every 100 files
            file_begin_name = generate_random_name()
        file_end_name = generate_random_name()
        file_name = f"{generate_folder_path}/{file_begin_name} - {file_end_name}.txt"
        with open(file_name, 'w') as file:
            file.write("This is a sample file.")

if __name__ == "__main__":
    create_files()
