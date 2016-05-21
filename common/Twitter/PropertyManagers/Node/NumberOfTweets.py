from Data.DataAccess.TwitterDataAccessObject import TwitterDataAccessObject


class NumberOfTweets:

    def __init__(self, dao=TwitterDataAccessObject()):
        self.dao = dao
        pass

    def add_property(self, graph, node_id):
        statuses = self.dao.get_user_statuses(node_id)
        num = 0
        if statuses is not None:
            num = len(statuses)
        graph.node[node_id]['Number_of_Tweets'] = num
