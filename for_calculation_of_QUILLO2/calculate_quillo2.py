#This function receives as an argument the route of a pdb file and
#returns the relation index of that pdb structure.

def obtain_quillo2(route_of_pdb_file):
    '''Receives the route of a pdb file and return2 the quillo2 value of that pdb file''' 
    from coordinates_quillo2 import residue_3d_boxes_residues_centroid_coordinates
    from score_quillo2 import score_list 

    #Generate the list containing the coordinates of each residue (lista_coordenadas):
    lista_coordenadas = residue_3d_boxes_residues_centroid_coordinates(route_of_pdb_file)

    #Obtain the quillo2 value:
    quillo2 = score_list(lista_coordenadas) / len(lista_coordenadas)

    #Return the result:
    return(quillo2)



