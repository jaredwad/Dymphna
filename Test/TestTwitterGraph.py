import time
import networkx as nx
from common.Twitter.TwitterGraph import TwitterGraph

DEFAULT_USER_ID = 1259825000


def test_build_ego_network(user_id=DEFAULT_USER_ID):
    start_time = time.time()
    graph = TwitterGraph.build_ego_network(user_id)
    print("--- test_get_user took {0} seconds ---".format(time.time() - start_time))
    print "There are {0} nodes".format(len(graph.nodes()))
    print graph.nodes()
    nx.write_graphml(graph, "graph.graphml")


def main():
    test_build_ego_network()


main()
