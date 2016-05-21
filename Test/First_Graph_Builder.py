import time

import networkx as nx

from Graph.GraphBuilder import GraphBuilder
from common.Twitter.PropertyManagers.Node.AverageSentiment import AverageSentiment
from common.Twitter.PropertyManagers.Node.NumberOfTweets import NumberOfTweets
from common.Twitter.PropertyManagers.Node.KeywordCount import KeywordCount

from common.Twitter.TwitterGraph import TwitterGraph
from common.Twitter.TwitterSocialUnit import TwitterSocialUnit

DEFAULT_USER_ID = 1259825000


def add_node(builder, cur_node, new_node):
    builder.add_node(new_node)
    builder.add_edge(cur_node, new_node)


def add_nodes(builder, cur_node, nodes):
    for new_id in nodes:
        add_node(builder, cur_node, new_id)


def build_graph(user_id=DEFAULT_USER_ID):
    num_itter = 10
    start_time = time.time()
    builder = TwitterGraph()
    builder.add_node_property_manager(AverageSentiment())
    builder.add_node_property_manager(NumberOfTweets())
    builder.add_node_property_manager(KeywordCount())

    fringe = [user_id]

    while num_itter > 0:
        new_fringe = []
        for node in fringe:
            if num_itter <= 0:
                break
            num_itter -= 1

            print "Running Node: {0}, {1} more to go...".format(node, num_itter)

            fringe.remove(node)

            tsu = TwitterSocialUnit(node)
            neighbors = tsu.get_outgoing_neighbors_ids()
            neighbors.extend(tsu.get_incoming_neighbors_ids())

            add_nodes(builder, node, neighbors)
            new_fringe.extend(neighbors)

            print "Added {0} nodes to the fringe".format(len(neighbors))

        fringe = new_fringe

    graph = builder.get_graph()

    print("--- test_get_user took {0} seconds ---".format(time.time() - start_time))
    print "There are {0} nodes".format(len(graph.nodes()))
    print graph.nodes()
    nx.write_graphml(graph, "graph.graphml")


def test_graph_builder():
    start_time = time.time()

    builder = GraphBuilder()
    builder.build()
    graph = builder.graph
    print("--- test_get_user took {0} seconds ---".format(time.time() - start_time))
    print "There are {0} nodes".format(len(graph.nodes()))
    print graph.nodes()
    nx.write_graphml(graph, "graph2.graphml")


test_graph_builder()
