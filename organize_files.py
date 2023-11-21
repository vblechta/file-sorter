import os

organize_folder_path = "data"  # Replace this with the path to your folder

def organize_files(folder_path):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    for file in files:
        # Split the filename into parts using ' - ' as a separator
        parts = file.split(' - ')

        if len(parts) > 1:
            # Extract the first part of the filename
            folder_name = parts[0]

            # Create a folder if it doesn't exist
            destination_folder = os.path.join(organize_folder_path, folder_name)
            os.makedirs(destination_folder, exist_ok=True)

            # Move the file to the corresponding folder
            source_path = os.path.join(folder_path, file)
            destination_path = os.path.join(destination_folder, file)
            os.rename(source_path, destination_path)

organize_files(organize_folder_path)
