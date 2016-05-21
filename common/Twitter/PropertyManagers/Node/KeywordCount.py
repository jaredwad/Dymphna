from Data.DataAccess.TwitterDataAccessObject import TwitterDataAccessObject


class KeywordCount:

    def __init__(self, keywords=['python', 'mongo'], dao=TwitterDataAccessObject()):
        self.keywords = keywords
        self.dao = dao
        pass

    def add_property(self, graph, node_id):
        statuses = self.dao.get_user_statuses(node_id)
        for keyword in self.keywords:
            count = 0
            if statuses is not None:
                for status in statuses:
                    if keyword in status:
                        count += 1
            property_count = keyword + '_count'
            graph.node[node_id][property_count] = count
