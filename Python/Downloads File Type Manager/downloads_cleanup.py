# Did notice that this could interrupt virus scans, so probably want to use this to clean up
# downloads folder after scans have been completed
from os import scandir, rename
from os.path import splitext, exists, join
from shutil import move
from time import sleep

import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# https://youtu.be/NCvI-K0Gp90
# Working with files in python: https://realpython.com/working-with-files-in-python/
# Watchdog library: https://pythonhosted.org/watchdog/

# File Destinations
source_dir = "/Users/Thomas/Downloads"
dest_dir_sfx = "/Users/Thomas/Desktop/Python Downloads File Manager/Sound"
dest_dir_music = "/Users/Thomas/Desktop/Python Downloads File Manager/Music"
dest_dir_video = "/Users/Thomas/Desktop/Python Downloads File Manager/Video"
dest_dir_image = "/Users/Thomas/Desktop/Python Downloads File Manager/Image"
dest_dir_document = "/Users/Thomas/Desktop/Python Downloads File Manager/Document"
dest_dir_email = "/Users/Thomas/Desktop/Python Downloads File Manager/Email"
dest_dir_executable = "/Users/Thomas/Desktop/Python Downloads File Manager/Executable"
dest_dir_programming = "/Users/Thomas/Desktop/Python Downloads File Manager/Programming"
dest_dir_compressed = "/Users/Thomas/Desktop/Python Downloads File Manager/Compressed"

# Supported image types
image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp",
                    ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw", ".k25", ".bmp",
                    ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf",
                    ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]
# Supported Video types
video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg", ".mp4", ".mp4v",
                    ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]
# Supported Audio types
audio_extensions = [".m4a", ".flac", "mp3", ".wav", ".wma", ".aac"]
# Supported Document types
document_extensions = [".doc", ".docx", ".odt", ".pdf", "txt", ".xls", ".xlsx", "csv", ".ppt", ".pps",
                       ".pptx", ".key", ".db", ".dbf", ".dat", ".mdb", ".log", ".sav", ".sql", ".xml"]
# Supported Email types
email_extensions = [".email", ".eml", ".emlx", ".msg", ".oft", ".ost", ".pst", ".vcf"]
# Supported Executable and Disc types
executable_extensions = [".exe", ".apk", ".bat", ".cgi", ".pl", ".com", ".gadget", ".jar", ".msi", ".wsf", ".iso",
                         ".bin", ".dmg", ".toast", ".vcd"]
# Supported Programming types
programming_extensions = [".htm", "html", ".xhtml", ".css", ".js", ".php", ".c", ".cpp", ".cgi", ".pl",
                          ".class", ".java", ".h", ".cs", ".sh", ".vb"]
# Supported Compressed types
compressed_extensions = [".7z", ".arj", ".deb", ".pkg", ".rar", ".rpm", ".z", ".zip"]


def make_unique(dest, name):
    filename, extension = splitext(name)
    counter = 1
    # IF FILE EXISTS, ADDS NUMBER TO THE END OF THE FILENAME
    while exists(f"{dest}/{name}"):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1
    return name


def move_file(dest, entry, name):
    if exists(f"{dest}/{name}"):
        unique_name = make_unique(dest, name)
        oldName = join(dest, name)
        newName = join(dest, unique_name)
        rename(oldName, newName)
    move(entry, dest)


class MoveHandler(FileSystemEventHandler):
    # THIS FUNCTION WILL RUN WHENEVER THERE IS A CHANGE IN "source_dir"
    # .upper is for not missing out on files with uppercase extensions
    def on_modified(self, event):
        with scandir(source_dir) as entries:
            for entry in entries:
                name = entry.name
                self.check_audio_files(entry, name)
                self.check_video_files(entry, name)
                self.check_image_files(entry, name)
                self.check_document_files(entry, name)
                self.check_email_files(entry, name)
                self.check_executable_files(entry, name)
                self.check_programming_files(entry, name)
                self.check_compressed_files(entry, name)

    def check_audio_files(self, entry, name):  # Checks all Audio Files
        for audio_extension in audio_extensions:
            if name.endswith(audio_extension) or name.endswith(audio_extension.upper()):
                if entry.stat().st_size < 10_000_000 or "SFX" in name:  # 10Megabytes
                    dest = dest_dir_sfx
                else:
                    dest = dest_dir_music
                move_file(dest, entry, name)
                logging.info(f"Moved audio file: {name}")

    def check_video_files(self, entry, name):  # Checks all Video Files
        for video_extension in video_extensions:
            if name.endswith(video_extension) or name.endswith(video_extension.upper()):
                move_file(dest_dir_video, entry, name)
                logging.info(f"Moved video file: {name}")

    def check_image_files(self, entry, name):  # Checks all Image Files
        for image_extension in image_extensions:
            if name.endswith(image_extension) or name.endswith(image_extension.upper()):
                move_file(dest_dir_image, entry, name)
                logging.info(f"Moved image file: {name}")

    def check_document_files(self, entry, name):  # Checks all Document Files
        for documents_extension in document_extensions:
            if name.endswith(documents_extension) or name.endswith(documents_extension.upper()):
                move_file(dest_dir_document, entry, name)
                logging.info(f"Moved document file: {name}")

    def check_email_files(self, entry, name):  # Checks all Video Files
        for email_extension in email_extensions:
            if name.endswith(email_extension) or name.endswith(email_extension.upper()):
                move_file(dest_dir_email, entry, name)
                logging.info(f"Moved email file: {name}")

    def check_executable_files(self, entry, name):  # Checks all Video Files
        for executable_extension in executable_extensions:
            if name.endswith(executable_extension) or name.endswith(executable_extension.upper()):
                move_file(dest_dir_executable, entry, name)
                logging.info(f"Moved executable file: {name}")

    def check_programming_files(self, entry, name):  # Checks all Video Files
        for programming_extension in programming_extensions:
            if name.endswith(programming_extension) or name.endswith(programming_extension.upper()):
                move_file(dest_dir_programming, entry, name)
                logging.info(f"Moved programming file: {name}")

    def check_compressed_files(self, entry, name):  # Checks all Video Files
        for compressed_extension in compressed_extensions:
            if name.endswith(compressed_extension) or name.endswith(compressed_extension.upper()):
                move_file(dest_dir_compressed, entry, name)
                logging.info(f"Moved compressed file: {name}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - %(message)s",
                        datefmt="%Y-%m-%d %M:%M:%S")
    path = source_dir
    event_handler = MoveHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
