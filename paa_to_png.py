import os
import subprocess
from pathlib import Path
from tqdm import tqdm


print("PAA to PNG Converter by Zer0")
print("Make sure to add 'C:\\Program Files (x86)\\Steam\\steamapps\\common\\DayZ Tools\\Bin\\ImageToPAA' to your system PATH if the command does not work.\n")

base_folder = Path(__file__).parent

output_folder = base_folder / "converted_png"

imageToPAA = Path(r"C:\Program Files (x86)\Steam\steamapps\common\DayZ Tools\Bin\ImageToPAA\ImageToPAA.exe")

paa_files = list(base_folder.rglob("*.paa"))

print(f"We found {len(paa_files)} .paa files.\n")

for file in tqdm(paa_files, desc="Converting files"):
    # Maintain folder structure
    relative_path = file.relative_to(base_folder)
    dest_file = output_folder / relative_path.with_suffix(".png")
    dest_file.parent.mkdir(parents=True, exist_ok=True)

    # Command: ImageToPAA source_file destination_file
    cmd = [str(imageToPAA), str(file), str(dest_file)]

    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error converting {file}: {e}")
