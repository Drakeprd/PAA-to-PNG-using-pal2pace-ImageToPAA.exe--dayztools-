# PAA-to-PNG-using-pal2pace-ImageToPAA.exe--dayztools-
# Python script to convert multiple files from .paa to .png using ImageToPAA.exe from dayztools. To use it just download it and extract the script to the folder that contains the .paa files, (The script will search for PAA files in the folder the script is stored and all the subfolders), execute it and you will get all the PAA files converted to PNG in a folder named converted_png keeping the original folder structure from the origin files.

import os
import subprocess
from pathlib import Path
from tqdm import tqdm

# Base folder (where this script is located)
base_folder = Path(__file__).parent

# Output folder
output_folder = base_folder / "converted_png"

# Path to the ImageToPAA.exe executable
# NOTE: If the script is not working then add this folder to your system PATH so the terminal can recognize 'pal2pace' "C:\Program Files (x86)\Steam\steamapps\common\DayZ Tools\Bin\ImageToPAA"
imageToPAA = Path(r"C:\Program Files (x86)\Steam\steamapps\common\DayZ Tools\Bin\ImageToPAA\ImageToPAA.exe")

# Search for all .paa files in the base folder and all subfolders
paa_files = list(base_folder.rglob("*.paa"))

print(f"Found {len(paa_files)} .paa files.")

for file in tqdm(paa_files, desc="Converting files"):
    # Create output path maintaining folder structure
    relative_path = file.relative_to(base_folder)
    dest_file = output_folder / relative_path.with_suffix(".png")
    dest_file.parent.mkdir(parents=True, exist_ok=True)

    # Command: only source and destination (do not use 'pal2pace' as argument)
    cmd = [str(imageToPAA), str(file), str(dest_file)]

    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error converting {file}: {e}")
