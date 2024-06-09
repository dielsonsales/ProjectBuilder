import shutil


def copy_folder(source_folder, destination_folder):
    """Copies the files in the source folder to the destination folder."""
    shutil.copytree(source_folder, destination_folder)
