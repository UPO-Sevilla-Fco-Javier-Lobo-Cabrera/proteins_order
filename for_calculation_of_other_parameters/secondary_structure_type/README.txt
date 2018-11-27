Just execute main_percentage_beta_strand.py on a terminal (Note: Biopython needs to be installed).
For example, if the terminal session is in the present directory, it would
work with the instruction: python main_percentage_beta_strand.py pdb_entry_type.txt

Explanation:
The script main_percentage_beta_strand.py receives as parameter the
path to the pdb_entry_type.txt file, and proceeds as follows:
0)Creates a file named "pdb_id_and_obtained_percent_beta.txt".
1)Reads a line (starting with the first) of the pdb_entry_type.txt file.
2)If the line is that corresponding to a protein --i.e if the line
contains the word "prot"-- then the pdb code contained in that line
is downloaded from the RCSB database. Then the pdb file is checked
to determine whether it has been resolved by X-Ray diffraction, and
if so, the percentage of residues in beta strand
is calculated.
3)Then, the pdb code and percentage are appended to the
pdb_id_and_obtained_percent_beta.txt file.
4)Proceeds in the same manner with the rest of lines of the
pdb_entry_type.txt file.

Already computed results are available in the already_computed_results 
directory.
