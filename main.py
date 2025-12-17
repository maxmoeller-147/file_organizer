# Handle file system paths (more readable than os path)
from pathlib import Path

# Move files between directories
import shutil

# Defines target directory to organize
directory = Path.home() / "Desktop" / "desktop_test"

# Dictionary that maps the extensions with their respective folders, easy to add more extensions.
extensions = {
    "Pictures": [".jpeg", ".jpg", ".gif", ".png"],
    "Music": [".mp3", ".wav", ".msv"],
    "Videos": [".mov", ".mp4", ".mkv", ".mpeg", ".mpg"],
    "Documents": [".pdf", ".doc",".docx", ".txt", ".numbers", ".pages"],
    "Zip": [".iso", ".tar", ".gz", ".rz", ".7z", ".dmg", ".rar", ".zip"],
    "Apps": [".exe",".app",".dmg"],
}

# Loops through every item in the target directory
for item in directory.iterdir():
   
   # Check if the item is a file, get the file extension and convert it to lowecase so it can handle uppercase extensions as well.
    if item.is_file():
        extension = item.suffix.lower()
        # Boolean that tracks if the file was moved. succesfully.
        moved = False

        # Loops through each category and list of extensions.
        for folder_name, ext_list in extensions.items():
            
            # If the extension matches one in the list. 
            if extension in ext_list:
                
                # Create a destination folder if it doesn't exist. 
                folder_path = directory / folder_name
                folder_path.mkdir(exist_ok=True)

                # Makes the destination path for the file.
                destination = folder_path / item.name

                # Moves the file to the destination.
                shutil.move(str(item), str(destination))
                
                # Gives feedback to the user.
                print(f"{item.name} moved to {folder_name} folder.")
                
                # Marks the file as moved and break the loop.
                moved = True
                break

        # If the file extension is not listed in any category.    
        if not moved:
            print(f"{item.name} couldn't be moved. Unknown file extension.")
    
    # If the item is not a file.
    else: 
        print(f"{item.name} is not a file.")

# Final Feedback to the user.
print("All the file had been organized")