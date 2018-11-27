Just execute main_surface_area_per_residue.py on a terminal 
For example, if the terminal session is in the present directory, it would
work with the instruction: python main_surface_area_per_residue.py pdb_entry_type.txt

(Note: the software vossolvox (Nucleic Acids Res. 2010 Jul 1 38 (Web Server issue): W555-562)
needs to be installed, and its files i)pdb_to_xyzr and ii)Volume.exe need
to be present in the same directory where main_surface_area_per_residue.py is located.
In this directory, those two files are present by default but they may not work in 
your computer because they were not compiled in your computer. So, you would need
to compile vossolvox in your computer and replace those two files by the ones compiled
in your machine.


Explanation:
The script main_surface_area_per_residue.py receives as parameter 
the path to the pdb_entry_type.txt file and proceeds as follows:
0)Creates a file named "pdb_id_and_obtained_surf_area_per_res.txt".
1)Reads a line (starting with the first) of the pdb_entry_type.txt file.
2)If the line is that corresponding to a protein --i.e if the line
contains the word "prot"-- then the pdb code contained in that line
is downloaded from the RCSB database. Then the pdb file is checked
to determine whether it has been resolved by X-Ray diffraction, and
if so, the surface area per residue is calculated.
The protein in the pdb code is assessed using software from
Nucleic Acids Res. 2010 Jul 1 38 (Web Server issue): W555-562 to
calculate the surface area per residue of the protein (without the
solvent, ions and heteroatoms).
3)The pdb code along with the surface area per residue ratio of
the protein without heteroatoms are appended to the
pdb_id_and_obtained_surf_area_per_res.txt file.
4)Proceeds in the same manner with the rest of lines of the
pdb_entry_type.txt file.


