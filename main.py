import os

import CopyFolderContentstoDirectoryFolder
import ParentFolderProccess
import MoveContentsToOtherFolder

files_changed = 0;

parent_folder = input('Parent Folder:')
ParentFolderProccess.processFolder(parent_folder, files_changed)

# Create the temporary destination folder inside the parent folder
temp_destination_folder = os.path.join(parent_folder, "Temporary_Folder")
os.makedirs(temp_destination_folder, exist_ok=True)

print("Parent Folder: " + parent_folder + " Temp Destination Folder: " + temp_destination_folder)

# Copy children form parent's to temp folder
print("Coping children form parent's to temp folder")
CopyFolderContentstoDirectoryFolder.copyChildrenFolderContentsToSingleDirectoryFolder(parent_folder, temp_destination_folder, files_changed)
print("Done")

# Move Temp Folder contents back to parent folder
print("Moving Temp Folder contents back to parent folder")
MoveContentsToOtherFolder.moveContentsToDirectedFolder(temp_destination_folder, parent_folder)
print("Done")

# Print the total number of files changed
print(f'Total files changed: {files_changed}')

print("Done")
