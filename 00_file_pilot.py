import os
import shutil

# Maps user-friendly folder names to lists of associated file extensions.
EXTENSION_MAP = {
    "PDFs": [".pdf"],
    "Word Docs": [".docx"],
    "Excel Sheets": [".xlsx"],
    "PowerPoint Presentations": [".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".avi", ".mov", ".wmv"],
    "Audio Files": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z"],
    "Text Files": [".txt"],
    "Code Files": [".py", ".java", ".cpp", ".html", ".css", ".js"],
    "Spreadsheets": [".xls"],
    "Presentations": [".ppt"],
    "Databases": [".db", ".sqlite"],
    "Configuration Files": [".ini", ".cfg"],
    "Log Files": [".log"],
    "System Files": [".dll", ".sys"],
    "Executable Files": [".exe"],
}


def get_destination_folder(filename):
    """
    Determines the destination folder for a file based on its extension.

    Args:
        filename (str): The name of the file to categorize.

    Returns:
        str: The folder name from EXTENSION_MAP, or 'Others' if no match.
    """
    # Extract the file extension, normalize it to lowercase and strip spaces.
    ext = os.path.splitext(filename)[1].strip().lower()
    for folder, extensions in EXTENSION_MAP.items():
        if ext in extensions:
            return folder
    return "Others"


def sort_files(folder_path):
    """
    Sorts all files in the specified folder into sub-folders based on their extensions.

    Args:
        folder_path (str): Path to the folder whose files will be organized.
    """
    # Iterate over each item in the given directory.
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        # Process only files, skip directories.
        if os.path.isfile(file_path):
            # Determine the appropriate destination folder for this file.
            dest_folder = get_destination_folder(file)
            dest_path = os.path.join(folder_path, dest_folder)

            # Create the destination folder if it doesn't already exist.
            os.makedirs(dest_path, exist_ok=True)
            # Move the file into the destination folder.
            shutil.move(file_path, os.path.join(dest_path, file))
            print(f"📁 Moved: {file} to {dest_folder}")


if __name__ == "__main__":
    # Prompt user for a folder path; default to the current working directory if empty.
    folder = input("Enter the folder path or leave empty to use current folder: ").strip()
    folder = folder or os.getcwd()

    # Validate that the provided path is a directory.
    if not os.path.isdir(folder):
        print("Invalid folder path.")
        exit(1)
    # Perform the file sorting.
    sort_files(folder)
    print("✅ Files sorted successfully.")
