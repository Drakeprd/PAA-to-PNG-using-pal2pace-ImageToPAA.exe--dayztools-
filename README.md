# SWAP THE VIEW TO CODE OR RAW TO SEE THE FILE STRUCTURE

# PAA-to-PNG-PNG-to-PAA-using-pal2pace-ImageToPAA.exe--dayztools-
PAA to PNG Converter

# Credits: Zer0-zn

This Python script search and convert all the .paa files from the folder that is contained and subfolders (used in DayZ and other Bohemia Interactive games) to .png format and .png to .paa. It preserves the folder structure of your .paa files in the output folder and it automatically detect the -size of the file to convert and it set it automatically for the conversion.

# Requirements

- Python
Download and install Python from [https://www.python.org/downloads/](https://www.python.org/ftp/python/3.13.7/python-3.13.7-amd64.exe)
!Important Make sure to check ------“Add Python to PATH”------- during installation.

- DayZ Tools
You need DayZ Tools to get ImageToPAA.exe for the script to work.
Example path:
After installing dayz tools on steam you will find ImageToPAA.exe
C:\Program Files (x86)\Steam\steamapps\common\DayZ Tools\Bin\ImageToPAA\ImageToPAA.exe

- TQDM library (for progress bar)
Install via terminal:
pip install tqdm

# Setup
Download the zip with my scripts and extract the scripts in the folder you plan to work with the .PAA. (Extract it in the main folder you working so the scripts can search for the .paa/.png files in the folder you extracted it and the subfolders)
Download DayZ Tools on Steam.
After installing DayZ Tools add the ImageToPAA.exe folder "C:\Program Files (x86)\Steam\steamapps\common\DayZ Tools\Bin\ImageToPAA" to your system PATH so the script can use the argument pal2pace from ImageToPAA.exe on CMD
IF THE SCRIPTS ARE NOT WORKING THEN YOU MUST ADD THE ROUTE OF ImageToPAA.exe (C:\Program Files (x86)\Steam\steamapps\common\DayZ Tools\Bin\ImageToPAA) TO YOUR PATH WITHOUT WRITING ImageToPAA.exe AT THE END. JUST THE ROUTE OF THE FOLDER CONTAINING ImageToPAA.exe SO AT THE END IT MUST LOOKS LIKE THIS ...\steammapps\common\DayZ Tools\Bin\ImageToPAA

Adding to PATH on Windows
Open Settings → System → About → Advanced system settings → Environment Variables.
Under System variables, find Path and click Edit.
Add the folder containing ImageToPAA.exe. (C:\Program Files (x86)\Steam\steamapps\common\DayZ Tools\Bin\ImageToPAA)
Click OK to save changes.

Usage
After downloading the zip with the script just extract the scripts in the folder you planing to use for storing the .paa/.png files. You should place the scripts next to the addons folder you get after extracting the .pbo. You have an example on how the script works and keep the folder structure of the folder containing it and the child folders and files   
The script will automatically search all subfolders for .paa files. 
---The best usage for this script is extracting all the .pbo files you want to modify in one folder and mantaining the folder structure of the .pbo meaning to leave all the .paa in their original folders after extracting them from the .pbo because the script will search in all the subfolders and it will create the same folder structure of the origin with the same subfolders and the .paa files in their original folder so you can just extract convert modify and then convert 
Open a terminal (PowerShell or CMD) in the folder where your script is located and write the command python paa_to_png.py to convert from .PAA to .PNG and for the .PNG to .PAA use the command python png_to_paa.py. To convert from png to paa you will need the folder converted_png that creates the script paa_to_png.py because it will search for the png you got from the first conversion. This way the script keep the main original structure so you can just copy paste the main folder with all the edited files at once and not creating and searching manually the structure to include it on the .pbo file as it was extracted. Run the first script for getting the PAA into PNG to edit and then when you finished all the files then convert it back from PNG to PAA. 

-------Example of folder structure:

------Original file structure 
├─ addons/
│   ├─ animals/
│   │   ├─ bos_taurus/
│   │   │   ├─ data/
│   │   │   │   ├─ bull_white_nohq.paa
│   │   │   │   ├─ bull_white_smdi.paa
│   │   │   │   └─ bull_spotted_smdi.paa
│   │   ├─ vulpes_vulpes/
│   │   │   └─ data/
│   │   │       └─ red_fox_nohq.paa

Folder structure after using the script .paa to .png and .png to .paa.
grafmod/
├─ addons/
│   ├─ animals/
│   │   ├─ bos_taurus/
│   │   │   └─ data/
│   │   │       ├─ bull_white_nohq.paa
│   │   │       ├─ bull_white_smdi.paa
│   │   │       ├─ bull_spotted_smdi.paa
│   │   ├─ vulpes_vulpes/
│   │   │   └─ data/
│   │   │       └─ red_fox_nohq.paa
│   │   └─ lepus_europaeus/
│   │       └─ data/
│   │           └─ lepus_europaeus_co.paa
├─ converted_png/-----------------------------PAA-TO-PNG
│   ├─ addons/
│   │   ├─ animals/
│   │   │   ├─ bos_taurus/
│   │   │   │   └─ data/
│   │   │   │       ├─ bull_white_nohq.png
│   │   │   │       ├─ bull_white_smdi.png
│   │   │   │       ├─ bull_spotted_smdi.png
│   │   │   ├─ vulpes_vulpes/
│   │   │   │   └─ data/
│   │   │   │       └─ red_fox_nohq.png
│   │   │   └─ lepus_europaeus/
│   │   │       └─ data/
│   │   │           └─ lepus_europaeus_co.png
├─ converted_paa/-----------------------------PNG-TO-PAA
│   ├─ addons/
│   │   ├─ animals/
│   │   │   ├─ bos_taurus/
│   │   │   │   └─ data/
│   │   │   │       ├─ bull_white_nohq.paa
│   │   │   │       ├─ bull_white_smdi.paa
│   │   │   │       ├─ bull_spotted_smdi.paa
│   │   │   ├─ vulpes_vulpes/
│   │   │   │   └─ data/
│   │   │   │       └─ red_fox_nohq.paa
│   │   │   └─ lepus_europaeus/
│   │   │       └─ data/
│   │   │           └─ lepus_europaeus_co.paa


Run the script:
.PAA TO .PNG :
python paa_to_png.py
 .PNG TO .PAA
python png_to_paa.py

Remember

Converted .png files will be saved in a folder called converted_png keeping the folder structure of the folder/s containing your .paa files and the same for converting the .png to .paa it will scan the converted_png folder then convert all the .png to .paa and clone the structure to the folder converted_paa.

- Notes

Ensure ImageToPAA.exe works from the terminal. If it doesn't, check that its folder is correctly added to the PATH. Also if you want to convert only some files and not all the files in a folder/subfolder then put the scripts on the folder with the .paa you want to convert and run the script. If you want to convert huge amount of files like the whole animal folder from animals.pbo just put the script on the folder where you extracted the files from the .pbo and run the script, it will automatically scan the folder and subfolders for all the .paa files and cloning the folder structure to save time.

Credits to Zer0-zn.
