import os
import subprocess
from pathlib import Path
from tqdm import tqdm
import sys

try:
    from PIL import Image
except ModuleNotFoundError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
    from PIL import Image

base_folder = Path(__file__).parent / "converted_png"
output_folder = base_folder.parent / "converted_paa"

imageToPAA = Path(r"C:\Program Files (x86)\Steam\steamapps\common\DayZ Tools\Bin\ImageToPAA\ImageToPAA.exe")

png_files = list(base_folder.rglob("*.png"))

print(f"We found {len(png_files)} PNG files.")

failed_files = []

for file in tqdm(png_files, desc="Converting PNG to PAA"):
    relative_path = file.relative_to(base_folder)
    dest_file = output_folder / relative_path.with_suffix(".paa")
    dest_file.parent.mkdir(parents=True, exist_ok=True)

    try:
        img = Image.open(file)
        max_dim = max(img.size)
        size_arg = f"-size={max_dim}"

        cmd = [
            str(imageToPAA),
            size_arg,
            str(file),
            str(dest_file)
        ]

        subprocess.run(cmd, check=True)
    except Exception as e:
        failed_files.append(file)
        print(f"Error converting {file} to PAA: {e}")
        print("Arguments used:")
        print(cmd)

if failed_files:
    print("\nThe following PNG files could not be converted to PAA:")
    for f in failed_files:
        print(f"- {f}")
    print("\nYou may need to convert them manually or check why they failed.")

print("Conversion completed. Credits to Zer0")
