from Graph.node_selector.BasicSelector import BasicSelector
from Graph.stop_condition.Iterations import Iterations
from common.Twitter.TwitterGraph import TwitterGraph


class GraphBuilder:
    def __init__(self, init_fringe=None, graph=TwitterGraph(), node_selector=BasicSelector(),
                 stop_condition=Iterations()):
        if init_fringe is None:
            init_fringe = [1259825000]
        self.fringe = init_fringe
        self.graph = graph
        self.node_selector = node_selector
        self.stop_condition = stop_condition

    def build(self):
        while not self.stop_condition.should_stop():
            if self.fringe is None or len(self.fringe) == 0:
                break

            node = self.node_selector.get_next(self.fringe)

            self.fringe.remove(node)

            print "Building off node: {0}".format(node)

            self.graph.add_node(node)

            new_fringe = self.graph.get_node_all_neighbors(node)
            print "adding {0} nodes to the fringe".format(len(new_fringe))
            self.fringe.extend(new_fringe)
