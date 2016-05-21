import networkx as nx

from common.Twitter.PropertyManagers.Node.AverageSentiment import AverageSentiment
from common.Twitter.PropertyManagers.Node.KeywordCount import KeywordCount
from common.Twitter.PropertyManagers.Node.NumberOfTweets import NumberOfTweets
from common.Twitter.TwitterSocialUnit import TwitterSocialUnit


class TwitterGraph:
    def __init__(self, node_property_managers=None, edge_property_managers=None):
        if node_property_managers is None:
            node_property_managers = [AverageSentiment(), NumberOfTweets(), KeywordCount()]
        if edge_property_managers is None:
            edge_property_managers = []

        self.graph = nx.DiGraph()
        self.node_property_managers = node_property_managers
        self.edge_property_managers = edge_property_managers

    def get_graph(self):
        return self.graph

    def build_ego_network(self, user_id):
        tsu = TwitterSocialUnit(user_id)
        self.graph = nx.DiGraph()
        self.add_node(user_id)

        out = tsu.get_outgoing_neighbors_ids()

        for neighbor in out:
            self.add_node(neighbor)
            self.add_edge(user_id, neighbor)

        inn = tsu.get_incoming_neighbors_ids()

        for neighbor in inn:
            self.add_node(neighbor)
            self.add_edge(user_id, neighbor)

        return self.graph

    def add_node(self, node):
        if not self.graph.has_node(node):
            self.graph.add_node(node)
            self.graph.node[node]['weight'] = 1
            for manager in self.node_property_managers:
                manager.add_property(self.graph, node)
        else:
            self.graph.node[node]['weight'] += 1

    def add_edge(self, n1, n2):
        if not self.graph.has_edge(n1, n2):
            self.graph.add_edge(n1, n2)
            self.graph[n1][n2]['weight'] = 1
            for manager in self.edge_property_managers:
                manager.add_property(self.graph, n1, n2)
        else:
            self.graph[n1][n2]['weight'] += 1

    def add_node_property_manager(self, node_property_manager):
        self.node_property_managers.append(node_property_manager)

    def add_edge_property_manager(self, edge_property_manager):
        self.edge_property_managers.append(edge_property_manager)

    def get_node_all_neighbors(self, node):
        neighbors = []
        inn = self.get_node_incoming_neighbors(node)
        out = self.get_node_outgoing_neighbors(node)

        if inn is not None:
            neighbors.extend(inn)
        if out is not None:
            neighbors.extend(out)

        return neighbors

    @staticmethod
    def get_node_incoming_neighbors(node):
        return TwitterSocialUnit(node).get_incoming_neighbors_ids()

    @staticmethod
    def get_node_outgoing_neighbors(node):
        return TwitterSocialUnit(node).get_outgoing_neighbors_ids()
