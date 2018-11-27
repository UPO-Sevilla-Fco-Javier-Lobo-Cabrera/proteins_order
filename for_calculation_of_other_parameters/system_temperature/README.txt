Just execute main_system_temperature.py on a terminal.
For example, if the terminal session is in the present directory, it would
work with the instruction: python main_system_temperature.py pdb_entry_type.txt brenda_download.txt


Explanation:
The script main_system_temperature.py receives as parameters i)the path to the
pdb_entry_type.txt file and ii) the path to the
BRENDA Database* (brenda_download.txt file) and proceeds as follows:
0)Creates a file named "pdb_id_and_obtained_system_temperature.txt".
1)Reads a line (starting with the first) of the pdb_entry_type.txt file.
2)If the line is that corresponding to a protein --i.e if the line
contains the word "prot"-- then the pdb code contained in that line
is downloaded from the RCSB database. Then the pdb file is checked
to determine whether it has been resolved by X-Ray diffraction, and
if so, the system temperature for the organism of which the protein
belongs is calculated.
3)Then, the pdb code and the correspondant system temperature are
appended to the pdb_id_and_obtained_system_temperature.txt file.
4)Proceeds in the same manner with the rest of lines of the
pdb_entry_type.txt file.


(*)BRENDA in 2017: new perspectives and new tools in BRENDA 
Placzek S., Schomburg I., Chang A., Jeske L., Ulbrich M., Tillack J.,
Schomburg D., Nucleic Acids Res.,45:D380-388 (2017) 
www.brenda-enzymes.org)

