from rivernetworkengine import Logger
from rivernetworkengine.util.shapefiles import Shapefile
import csv
from os import path
import networkx as nx


class Profile():

    def __init__(self, shpfile, inID, outID=None):
        """
        Profile a network from startID to endID

        If no outID is specified we go and found the outflow point and use that

        :param shpfile: The Shape file to open
        :param inID:  The ID of the input network segment
        :param outID:  The ID of the output network segment (Optional) Default is none
        """
        log = Logger("Main")

        # We need to open the shapefile first:
        log.info("Opening shapefile...")
        shape = Shapefile(shpfile)

        # Parse the network
        try:
            log.info("parsing shapefile into network...")
            G = nx.read_shp(shpfile, simplify=True)
            log.info("Shapefile successfully parsed into directed network")
        except Exception as e:
            log.error("Error parsing network", e)
        log = Logger("Main")

        startNode = self.findnodewithID(G, inID, shape.getIDField())

        if not startNode:
            raise Exception("Could not find start ID: {} in network.".format(inID))

        if outID:
            endNode = self.findnodewithID(G, outID, shape.getIDField())
            if not endNode:
                raise Exception("Could not find end ID: {} in network.".format(outID))
            # Make a depth-first tree from the first headwater we find
            try:
                shortestpath = nx.shortest_path(G, source=startNode[0], target=endNode[1])
                path_edges = zip(shortestpath, shortestpath[1:])
            except Exception, e:
                log.error("Path not found between these two points with id: '{}' and '{}'".format(inID, outID))
                raise e
        else:
            try:
                path_edges = list(nx.dfs_edges(G, startNode[0]))
            except Exception, e:
                log.error("Path not found between input point with ID: {} and outflow point".format(inID))


        outList = []
        cummulativelength = 0
        for edge in path_edges:
            # Get the ID for this edge
            shapeID = G.get_edge_data(*edge)[shape.getIDField()]

            shapelyObj = shape.featureToShapely(shapeID)
            # NetworkX stores the fields in attribute tables but we retrieve them from the shapefile directly
            # to remain consistent
            attrDic = shapelyObj['fields']

            # Calculate length and cummulative length
            attrDic['ProfileCalculatedLength'] = shapelyObj['geometry'].length
            cummulativelength += attrDic['ProfileCalculatedLength']
            attrDic['ProfileCummulativeLength'] = cummulativelength
            outList.append(attrDic)


        # Now let's calculate us some distances

        return outList

        # Could not find because those points are in two different subnetworks. Please fix your network
        # Could not find because stream flow was a problem. If you reverse your input and output then it works




    def findnodewithID(self, G, id, idField):
        """
        One line helper function to find a node with a given ID
        :param id:
        :return:
        """
        Logger("FindWithID")
        return next(iter([e for e in G.edges_iter() if G.get_edge_data(*e)[idField] == id]), None)

    def summarizeAttrib(self, G, attrlist, shortpath, csv):
        """
        Here's us summing all of the attrib ('Shape_Leng' in this case)
        :param path_edges:
        :param GG:
        :return:
        """
        Logger("SummAttrib")
        x = []
        counter = 0
        for pe in shortpath:
            counter += G.get_edge_data(*pe)[attrlist]
            x.append(counter)
        y = [(t[0][1] + t[0][0]) for t in shortpath]
        writeCSV(y, csv)


    def writeCSV(self, outdict, filename):
        """
        Separate out the writer so we can test without writing files
        :param outdict:
        :param csv:
        :return:
        """

        with open(filename, 'wb') as csv_file:

            writer = csv.writer(csv_file)
            writer.we
            for key, value in outdict.items():
               writer.writerow([key, value])