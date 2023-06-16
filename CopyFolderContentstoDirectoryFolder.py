import os
import shutil

def copyChildrenFolderContentsToSingleDirectoryFolder(parent_folder, destination_folder, files_changed):
# copy Contents of child folders to directory folder
    for item in os.listdir(parent_folder):
        item_path = os.path.join(parent_folder, item)

        # Check if the item is a directory
        if os.path.isdir(item_path):
            # Iterate over the contents of the subfolder
            for subitem in os.listdir(item_path):
                subitem_path = os.path.join(item_path, subitem)

                # Check if the subitem is a file
                if os.path.isfile(subitem_path):
                    # Move the file to the destination folder with a new name
                    destination_file = os.path.join(destination_folder, subitem)
                    shutil.move(subitem_path, destination_file)
                    print("Moving: " + subitem_path + " to " + destination_file)

                    # Increment the counter
                    files_changed += 1

                # Optionally, check if the subitem is a directory and perform recursive merge
                elif os.path.isdir(subitem_path):
                    # Create the destination subfolder if it doesn't exist
                    destination_subfolder = os.path.join(destination_folder, subitem)
                    os.makedirs(destination_subfolder, exist_ok=True)

                    # Merge the contents of the subfolder recursively
                    shutil.copytree(subitem_path, destination_subfolder, dirs_exist_ok=True)

                    # Increment the counter
                    files_changed += 1

                    # Optionally, remove the now empty subfolder
                    shutil.rmtree(subitem_path)
                    print("Removing TempFolder: " + subitem_path)