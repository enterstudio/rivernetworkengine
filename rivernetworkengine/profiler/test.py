# Matplotlib is used in the tests but it might be unfair to require it for regular users
import matplotlib.pyplot as plt
from shapely.geometry import *



def thing(shortestpath, startid, endid):
    # This just helps us plot our geo graph. It's kind of ahack
    # pos = {v: v for k, v in enumerate(G.nodes())}
    #
    # # We'll create a shapely line from this path and measure the length of it.
    # ls = LineString(shortestpath)
    # f, (ax1, ax2) = plt.subplots(1, 2)
    #
    # ax1.set_aspect(1.0)
    # plt.sca(ax1)
    # plt.axis('off')
    # plt.rcParams["figure.figsize"] = (20, 3)
    #
    # # place a text box in upper left in axes coords
    # textstr = 'Edges: {0}\nNodes: {1}\nStartID: {2}\nEndID {3}\nPathDist: {4}'.format(len(G.nodes()), len(G.edges()),
    #                                                                                   STARTID, ENDID, ls.length)
    # props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    #
    # ax1.text(0.05, 0.95, textstr, transform=ax1.transAxes, fontsize=14,
    #          verticalalignment='top', bbox=props)
    #
    # nx.draw_networkx_edges(GG, pos, ax=ax1, edge_color='black', width=1)
    # nx.draw_networkx_edges(GG, pos, ax=ax1, edgelist=path_edges, edge_color='red', width=3)
    #
    # # Now the second plot
    # px, py = summarizeAttrib(path_edges, GG, 'Shape_Leng')
    # plt.sca(ax2)
    # plt.plot(px, py)
    #
    # plt.show()
