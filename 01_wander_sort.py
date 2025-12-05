import os

def batch_rename(folder, base_name, extension):
    """
    Rename all files with the given extension inside the specified folder.
    
    Parameters:
        folder (str): Path to the target directory.
        base_name (str): New name prefix for each file.
        extension (str): File extension to filter (e.g., '.jpg').
    """
    # Collect all files in the folder that end with the specified extension (case-insensitive)
    files = [f for f in os.listdir(folder) if f.lower().endswith(extension)]

    # If no matching files are found, notify the user and exit the function
    if not files:
        print("❌ No files found with the specified extension.")
        return

    # Preview the new filenames without actually renaming
    for i, file in enumerate(files, start=1):
        new_name = f"{base_name}_{i}{extension}"
        print(f"Renamed: {file} to {new_name}")

    # Ask user for confirmation before performing the actual rename
    confirm = (
        input("Are you sure you want to rename all files? (y/n): ").strip().lower()
    )
    if confirm == "y":
        # Perform the renaming operation
        for i, file in enumerate(files, start=1):
            new_name = f"{base_name}_{i}{extension}"
            dest = os.path.join(folder, new_name)  # Full path for the new name
            src = os.path.join(folder, file)      # Full path for the original file
            os.rename(src, dest)                  # Rename the file on disk
            print(f"Renamed: {file} to {new_name}")
    else:
        print("❌ Operation canceled.")


if __name__ == "__main__":
    # Prompt user for the folder path; default to current working directory if empty
    folder = (
        input("Enter the folder path or leave empty to use current folder: ").strip()
        or os.getcwd()
    )

    # Validate the provided folder path
    if not os.path.isdir(folder):
        print("❌ Invalid folder path.")
        exit(1)
    else:
        # Gather remaining user inputs: base name and file extension
        base_name = input("Enter the base name for renaming: ").strip()
        extension = (
            input("Enter the file extension to filter (e.g., .jpg, .png): ")
            .strip()
            .lower()
        )
        # Execute the batch rename function
        batch_rename(folder, base_name, extension)
        print("✅ Batch rename completed.")
