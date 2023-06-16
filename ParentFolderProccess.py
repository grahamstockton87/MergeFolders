import os

# Check if folder is empty when size is 0
def is_folder_empty(folder_path):
    return len(os.listdir(folder_path)) == 0

# Delete Empty Folders
def delete_empty_folders(folder_path, filesChanged):
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)

        # Check if the item is a directory
        if os.path.isdir(item_path):
            # Recursively check and delete empty folders
            delete_empty_folders(item_path, filesChanged)

            # Check if the current folder is empty
            if is_folder_empty(item_path):
                # Delete the empty folder
                os.rmdir(item_path)
                print("Deleting EmptyFolders: " + item_path)
                filesChanged += 1

def processFolder(parent_folder, filesChanged):
    # Delete empty folders from the parent folder
    delete_empty_folders(parent_folder, filesChanged)