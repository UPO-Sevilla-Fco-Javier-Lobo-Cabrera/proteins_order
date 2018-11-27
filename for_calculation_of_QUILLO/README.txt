Just execute main_quillo.py on a terminal (Note: Biopython needs to be installed).
For example, if the terminal session is in the present directory, it would
work with the instruction: python main_quillo.py pdb_entry_type.txt

Explanation:
The main_quillo.py script receives as parameter the path to the
pdb_entry_type.txt file, and proceeds as follows:
0)Creates a file named "pdb_id_and_obtained_quillo.txt".
1)Reads a line (starting with the first) of the pdb_entry_type.txt file.
2)If the line is that corresponding to a protein --i.e if the line
contains the word "prot"-- then the pdb code contained in that line
is downloaded from the RCSB database.
3)The obtain_quillo function from
calculate_quillo.py if invoked with a try()
statement, passing as argument the route of the downloaded pdb file.
4)If the obtain_quillo function works, then the pdb code
and its corresponding quillo value are appended to 
pdb_id_and_obtained_quillo.txt .
5)Proceed in the same manner with the rest of lines of the
pdb_entry_type.txt file.

Already computed results are available in the already_computed_results 
directory.
