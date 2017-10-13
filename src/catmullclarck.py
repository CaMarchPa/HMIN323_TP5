def catmullclark(gmap):
    # Compute a dictionary of face points equal to the face center
    # (use functions elements and element_center)
    face_elements = gmap.elements(2)
    facepoints = dict([  face for d in face_elements : face = gmap.element_center(d, 2) ])

    # Create a local function to access to the face point from any dart of the face
    # (use function get_embedding_dart with the right degree)
    def get_facepoint(fdart):
        return gmap.get_embedding_dart(fdart, facepoints, 2)

    # Define a function to compute the position of an edge points:
    # For this, list the positions of the edge vertices (use incident_cells and get_position)
    # and the face points of the edge faces (use incident_cells and get_facepoint) and
    # return the mean
    def compute_edgepoint(edart):
        import numpy as np
        e = gmap.incident_cells(edart, 0, 1)
        position_vertices = [position for d in e : position = gmap.get_embedding_dart(d, gmap.positions, 0)]
        f = gmap.incident_cells(edart, 1, 2)
        position_faces = [position for d in f : position = gmap.get_embedding_dart(d, facepoints, 2)]
        
        return np.mean(position_vertices + position_faces)

    # Compute a dictionary of edge points just as for facepoints
    edgepoints = dict([  ])

    # Create a local function to access the edgepoint from any dart of the edge
    def get_edgepoint(edart):
        return gmap.get_embedding_dart(edart, edgepoints, 1)

    # Define a function to compute the new position of a vertex:
    # For this, compute the mean of edgepoints of incident edges (E),
    # the mean of facepoints of incident faces (F) and the current
    # position of the vertex (V). (use incident_cells, get_position,
    # get_edgepoint and get_facepoint)
    # Use the valence of the vertex (k, number of incident edges) to 
    # compute the new position:
    # V* &lt;- ((k-3)V + 2E + F)/3
    def compute_vertexpoint(vdart):

    # Set the new position to the vertex points

    # Create new vertices in the topological structure corresponding
    # to edge points:
    # For this, go through all the edges and split them
    # (use split_edge) and set the position to the new vertex.
    # Doing so, fill a list with all the new inserted darts 
    # (vertex orbits of the new darts created by the split)
    edgepoint_darts = []

    # Finally, create the new vertices in the topological structure 
    # corresponding to face points, and connect them to the edge point 
    # vertices inserted previously:
    # Iterate over all the faces
        # Store the postion of the face point corresponding to the face
        # Iterate over all the incident vertices of the face
            # Check if the vertex corresponds to an edge point (inserted 
            # at the previous step)
                # If it is an edge point store it in a list to process
        # Iterate over all the edge points to process
            # Create a new edge from the vertex (use insert_edge)
            # Store the darts at the other end of the edge (vertex orbits
            # of the new darts created by the insertion) in a list to process
        # Iterate over all the end darts to process
            # If the dart d is free by alpha_1:
                # Find its next dart in the new (quad) face :
                # alpha_0(alpha_1(alpha_0(alpha_1(alpha_0(alpha_1(alpha_0(d)))))))
                # Link those two darts by alpha_1
        # Select one of the end darts and set is position to the face point