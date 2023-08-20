import os
import subprocess
import sys

# Get the current working directory
current_directory = os.getcwd()

# Construct the full path to 'regs.txt'
filename = os.path.join(current_directory, "NeededPackets.txt")

print("Current working directory:", current_directory)
print("Full path to regs.txt:", filename)

def install_packages(filename):
    with open(filename, "r") as file:
        package_list = file.readlines()

    for package in package_list:
        package = package.strip()
        if package:
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
                print(f"Installed {package}")
            except subprocess.CalledProcessError:
                print(f"Error installing {package}")

def main():
    if not os.path.exists(filename):
        print("File regs.txt not found.")
        return

    install_packages(filename)

if __name__ == "__main__":
    main()
