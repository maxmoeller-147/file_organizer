# Python File Organizer

## Overview
A simple and customizable Python based file organiztion tool designed to automate repetitive file management. It scans the directory you choose as targetand organizes the files into categorized folders based on their file extensions. 

## Features
- Organizes files into folders by type. (Pictures, Music, Videos, etc.)
- Ignores directories or unsuported files.
- Easy to add more supported files.
- Hanldes uppercase and lowercase file extensions.

## Technologies 
- **Python 3**
- **pathlib** - for modern file system path handling
- **shutil** - for moving files between directories

## Project Structure

    file_organizer/
    ├── main.py
    ├── README.md
    └── LICENSE


## Installation

### Prerequisites
- Python 3.9 or higher
- Access to the directory you want to organize

### Clone the Repository

    git clone https://github.com/maxmoeller-147/file_organizer.git

   

## How it works
1. The script scans a target directory
2. Each file's extension is checked with a predefined list
3. a matching folder is created if it doesn't exist.
4. The file is moved into the appropiate folder.
5. Files with unsupported extensions are skipped. (left as they are)

## Customization

### Change target directory:
You can choose the target directory you want to organize by changing the directory in main.py:

   
    directory = Path.home() / "Desktop" / "desktop_test"

For Example: If you want to organize "/Documents/Projects":

    directory = Path.home() / "Documents" / "Projects"

### Add or modify file categories:
You can add or modify file categories by editing the extensions dictionary in main.py:

    extensions = {
    "Pictures": [".jpg", ".png"],
    "Documents": [".pdf", ".txt"],
    }


## How to run
Once you costumized it the way you like, from the project directory run:

    python3 main.py


## Ethical Considerations and Safety Recommendations
This Automation script that moves files can potentially cause loss or unintended changes if misused. Responsible automation requires transparency, testing and user awareness.

Ethical considerations addresed in this project:
- Clearly documenting the script's behavior and limitations.
- Avoid deletion of files
- Is strongly recommended to test this script in a dedicated test and safe directory before using it in a real directory.

## Limitations
- Files with identical names may overwrite existing files.
- The script does not process subdirectories.
- No undo functionality is implemented in this current version.


