Just execute main_deviations.py on a terminal. 
For example, if the terminal session is in the present directory, it would 
work with the instruction: python main_deviations.py pdb_id_and_obtained_quillo.txt 

Explanation:
The main_deviations.py receives as parameter the path to the pdb_id_and_obtained_quillo.txt file, and proceeds as follows:
#0)Creates a file named "pdb_id_and_difference_from_expected_quillo.txt".
#1)Opens the pdb_id_and_obtained_quillo.txt file and stores its 
#information.
#2)For every entry in pdb_id_and_obtained_quillo.txt the difference
#with the expected quillo value is calculated, and the result is appended
#to "pdb_id_and_difference_from_expected_quillo.txt".

Already computed results are available in the already_computed_results 
directory.
