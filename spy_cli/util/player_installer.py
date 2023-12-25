import subprocess
import py7zr
import os
import platform

def install_player():
    # Check if the operating system is Windows
    if platform.system() == 'Windows':
        # URL of the .7z file
        url = 'https://sourceforge.net/projects/mpv-player-windows/files/64bit/mpv-x86_64-20231224-git-0d47e48.7z/download'

        # Local file name to save the downloaded file
        downloaded_file = 'mpv.7z'

        # Directory to extract the files, set to C:/
        extraction_path = 'C:/mpv'

        # Download the file using curl
        try:
            subprocess.run(['curl', '-L', '-o', downloaded_file, url], check=True)
            print("Download complete.")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred during download: {e}")

        # Check if the file is downloaded
        if os.path.isfile(downloaded_file):
            # Create extraction directory if it doesn't exist
            os.makedirs(extraction_path, exist_ok=True)

            # Extract the archive
            try:
                with py7zr.SevenZipFile(downloaded_file, mode='r') as z:
                    z.extractall(path=extraction_path)
                print(f"Extracted to {extraction_path}")
            except Exception as e:
                print(f"An error occurred during extraction: {e}")

            # Delete the downloaded .7z file
            try:
                os.remove(downloaded_file)
                print(f"Deleted the file: {downloaded_file}")
            except Exception as e:
                print(f"An error occurred while deleting the file: {e}")
        else:
            print("Downloaded file not found.")
    else:
        print("This script is intended to be run on Windows only.")

# This allows the script to be run directly as before
if __name__ == '__main__':
    install_player()