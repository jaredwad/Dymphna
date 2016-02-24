import networkx as nx

from common.Twitter.TwitterPropertyManager import TwitterPropertyManager
from common.Twitter.TwitterSocialUnit import TwitterSocialUnit


class TwitterGraph:
    def __init__(self):
        pass

    @staticmethod
    def build_ego_network(user_id):
        tsu = TwitterSocialUnit(user_id)
        g = nx.DiGraph()
        user = tsu.inner_User
        TwitterGraph.add_node(user, g)

        out = tsu.get_outgoing_neighbors()

        for neighbor in out:
            TwitterGraph.add_node(neighbor, g)
            TwitterGraph.add_edge(user, neighbor, g)

        inn = tsu.get_incoming_neighbors()

        for neighbor in inn:
            TwitterGraph.add_node(neighbor, g)
            TwitterGraph.add_edge(user, neighbor, g)

        return g

    @staticmethod
    def add_node(node, graph):
        node_id = node['id_str']
        if not graph.has_node(node_id):
            graph.add_node(node_id)
            graph.node[node_id]['weight'] = 1
            TwitterPropertyManager.add_all(graph.node[node_id], node)
        else:
            graph.node[node_id]['weight'] += 1

    @staticmethod
    def add_edge(n1, n2, graph):
        n1_id = n1['id_str']
        n2_id = n2['id_str']
        if not graph.has_edge(n1_id, n2_id):
            graph.add_edge(n1_id, n2_id)
            graph[n1_id][n2_id]['weight'] = 1
