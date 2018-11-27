#This script receives as parameters the path to the 
#pdb_id_and_obtained_quillo.txt file and proceeds as follows:
#0)Creates a file named "pdb_id_and_difference_from_expected_quillo.txt".
#1)Opens the pdb_id_and_obtained_quillo.txt file and stores its 
#information.
#2)For every entry in pdb_id_and_obtained_quillo.txt the difference (Å⁻²)
#with the expected quillo value is calculated, and the result is appended
#to "pdb_id_and_difference_from_expected_quillo.txt".

import os
import sys

#0)Creates a file named "pdb_id_and_difference_from_expected_quillo.txt":
f = open("pdb_id_and_difference_from_expected_quillo.txt", "w+")

#1)Opens the pdb_id_and_obtained_quillo.txt file and stores its 
#information:
g = open(sys.argv[1], "r")
lines_of_g = g.readlines()
g.close()

#2)For every entry in pdb_id_and_obtained_quillo.txt the difference (Å⁻²)
#with the expected quillo value is calculated, and the result is appended
#to "pdb_id_and_difference_from_expected_quillo.txt".
for i in lines_of_g:
    pdb_code = i.split()[0]
    dif = float(i.split()[1]) * float(i.split()[2]) - (-0.5863 + float(i.split()[2]) * 0.431 + float(i.split()[2]) * float(i.split()[2]) * 0.00003254)
    f.write(pdb_code + "\t" + str(dif) + "\n")

f.close()

