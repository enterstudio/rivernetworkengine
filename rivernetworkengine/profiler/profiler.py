from rivernetworkengine import Logger
import csv
import networkx as nx

def main(shpfile, csvfile, idfield, csvattribs, inID, outID=None):

    """
    Profile a network from startID to endID
    :param shpfile:
    :param csvfile:
    :param csvattribs:
    :param inID: The input ID
    :param outID: (Optional) If specified will be
    :return:
    """
    G = nx.read_shp('../../shapefiles/FullNetwork.shp', simplify=True)

    log = Logger("Main")

    start = findnodewithID(inID)
    end = findnodewithID(outID)

    # Make a depth-first tree from the first headwater we find
    try:
        shortestpath = nx.shortest_path(G, source=start[0], target=end[0])
        path_edges = zip(shortestpath, shortestpath[1:])
    except:
        print "Path found between these two points"
        exit(0)


# Could not find because those points are in two different subnetworks. Please fix your network
# Could not find because stream flow was a problem. If you reverse your input and output then it works
# StartID does not exist
# EndID does not exist




def findnodewithID(G, id):
    """
    One line helper function to find a node with a given ID
    :param id:
    :return:
    """
    Logger("FindWithID")
    id = next(iter([e for e in G.edges_iter() if G.get_edge_data(*e)['OBJECTID'] == id]), None)
    return id

def summarizeAttrib(path_edges, GG, attrib):
    """
    Here's us summing all of the attrib ('Shape_Leng' in this case)
    :param path_edges:
    :param GG:
    :return:
    """
    Logger("SummAttrib")
    x = []
    counter = 0
    for pe in path_edges:
        counter += GG.get_edge_data(*pe)[attrib]
        x.append(counter)
    y = [(t[0][1] + t[0][0]) for t in path_edges]
    return x, y




