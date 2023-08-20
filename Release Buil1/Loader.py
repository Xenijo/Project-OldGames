import os
import threading
import string
import sys
import requests
import patoolib
from tqdm import tqdm

def search_disk(disk_letter, filename):
    print(f"Thread {threading.get_ident()}: Searching for {filename} on disk {disk_letter}")
    root_dir = f"{disk_letter}:\\"
    for root, dirs, files in os.walk(root_dir):
        if filename in files:
            file_path = os.path.join(root, filename)
            print(f"Thread {threading.get_ident()}: File found at: {file_path}")
            # Add your desired action here
            print(f"Thread {threading.get_ident()}: Performing an action...")
            download_and_unpack("https://raw.githubusercontent.com/Xenijo/project-Fix-Old/main/Testo.rar", "FixFiles.rar", os.path.dirname(file_path))

def download_and_unpack(url, filename, extraction_dir):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get("content-length", 0))

    with open(filename, "wb") as handle:
        for data in tqdm(response.iter_content(chunk_size=8192), total=total_size // 8192, unit="B", unit_scale=True):
            handle.write(data)

    # Unpack the RAR file
    patoolib.extract_archive(filename, outdir=extraction_dir)

    # Remove the downloaded RAR file
    os.remove(filename)

    print("Downloads and unpacking complete!")

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <num_threads>")
        return

    num_threads = int(sys.argv[1])

    disks = [letter for letter in string.ascii_uppercase if os.path.exists(f"{letter}:")]

    filename = "DKII-DX.exe"
    
    threads = []
    for disk in disks:
        thread = threading.Thread(target=search_disk, args=(disk, filename))
        threads.append(thread)
        thread.start()
        print(f"Thread {thread.ident} started for disk {disk}")

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
