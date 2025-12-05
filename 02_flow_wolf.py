import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Folder to monitor for new files (user's Downloads folder)
WATCH_FOLDER = os.path.expanduser("~/Downloads")

# Dictionary mapping file extensions to destination folder names
FILE_DESTS = {
    ".pdf": "PDFs",
    ".docx": "Documents",
    ".xlsx": "Spreadsheets",
    ".pptx": "Presentations",
    ".jpg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".mp4": "Videos",
    ".mov": "Videos",
}


class FileMoverHandler(FileSystemEventHandler):
    """Handles file-system events; automatically moves new files to categorized folders."""

    def on_created(self, event):
        # Ignore if the new item is a directory
        if event.is_directory:
            return

        # Full path of the newly created file
        file_path = event.src_path
        # Extract lowercase file extension for lookup
        ext = os.path.splitext(file_path)[1].lower()

        # Determine destination folder name; default to "Others" if extension not listed
        folder_name = FILE_DESTS.get(ext, "Others")
        # Build full destination path inside the watched folder
        full_dest_path = os.path.join(WATCH_FOLDER, folder_name)
        # Ensure the destination folder exists (create if necessary)
        os.makedirs(full_dest_path, exist_ok=True)

        # Construct final path for the file after move
        move_to = os.path.join(full_dest_path, os.path.basename(file_path))
        try:
            # Move the file to its categorized folder
            shutil.move(file_path, move_to)
            print(f"✅ Moved: {file_path} to {move_to}")
        except Exception as e:
            # Print error message if the move fails
            print(f"❌ Error moving {file_path}: {e}")


if __name__ == "__main__":
    # Notify user which folder is being watched
    print(f"👁️‍🗨️ Watching folder: {WATCH_FOLDER}")
    # Instantiate the event handler
    event_handler = FileMoverHandler()
    # Create the observer object
    observer = Observer()

    # Register the handler to monitor the specified folder (non-recursive)
    observer.schedule(event_handler, path=WATCH_FOLDER, recursive=False)
    # Start the observer thread
    observer.start()

    try:
        # Keep the script running indefinitely until interrupted
        while True:
            pass
    except KeyboardInterrupt:
        # Gracefully stop the observer on Ctrl+C
        observer.stop()
        observer.join()
