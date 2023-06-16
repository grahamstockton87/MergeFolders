import os
import shutil

def moveContentsToDirectedFolder(source_folder, destination_folder):
    # Iterate over the contents of the source folder
    for item in os.listdir(source_folder):
        item_path = os.path.join(source_folder, item)

        # Check if the item is a file
        if os.path.isfile(item_path):

            # Move the file to the destination folder
            shutil.move(item_path, destination_folder)
            print("Moving file to the destination folder: " + item_path)

        # Check if the item is a directory
        elif os.path.isdir(item_path):
            # Move the entire directory to the destination folder
            shutil.move(item_path, os.path.join(destination_folder, item))
            print("Moving entire directory to the destination folder: " + item_path)