# PAA-to-PNG-using-pal2pace-ImageToPAA.exe--dayztools-
PAA to PNG Converter

# Credits: Zer0

This Python script converts .paa files (used in DayZ and other Bohemia Interactive games) to .png format. It preserves the folder structure of your .paa files in the output folder.

# Requirements

- Python
Download and install Python from https://www.python.org/downloads/
Make sure to check “Add Python to PATH” during installation.

- DayZ Tools
You need DayZ Tools to get ImageToPAA.exe for the script to work.
Example path:
After installing dayz tools on steam you will find ImageToPAA.exe
C:\Program Files (x86)\Steam\steamapps\common\DayZ Tools\Bin\ImageToPAA\ImageToPAA.exe

- TQDM library (for progress bar)
Install via terminal:
pip install tqdm

# Setup

Add the ImageToPAA.exe folder "C:\Program Files (x86)\Steam\steamapps\common\DayZ Tools\Bin\ImageToPAA" to your system PATH so the script can use the argument pal2pace from ImageToPAA.exe on CMD

Windows:

Open Settings → System → About → Advanced system settings → Environment Variables.
Under System variables, find Path and click Edit.
Add the folder containing ImageToPAA.exe.
Click OK to save changes.

Usage
After downloading the zip with the script just extract it in the folder that contains the .paa files you want to convert.
The script will automatically search all subfolders for .paa files. 
---The best usage for this script is extracting all the .pbo files you want to modify in one folder and mantaining the folder structure of the .pbo meaning to leave all the .paa in their original folders after extracting them from the .pbo because the script will search in all the subfolders and it will create the same folder structure of the origin with the same subfolders and the .paa files in their original folder so you can just extract convert modify and then convert 
Open a terminal (PowerShell or CMD) in the folder where your script is located.

Run the script:

python your_script_name.py


Converted .png files will be saved in a folder called converted_png with the same folder structure as your .paa files.

Notes

Ensure ImageToPAA.exe works from the terminal. If it doesn't, check that its folder is correctly added to the PATH.

The script will show credits to Zer0 in the terminal at the start.

All .paa files in the current folder and all subfolders are processed automatically.
