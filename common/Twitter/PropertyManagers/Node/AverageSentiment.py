from Data.DataAccess.TwitterDataAccessObject import TwitterDataAccessObject
from textblob import TextBlob


class AverageSentiment:

    def __init__(self, dao=TwitterDataAccessObject()):
        self.dao = dao
        pass

    def add_property(self, graph, node_id):
        statuses = self.dao.get_user_statuses(node_id)
        total_polarity = 0.0
        total_subjectivity = 0.0
        num = 0.0
        if statuses is not None:
            for status in statuses:
                blob = TextBlob(status['text'])
                sentiment = blob.sentiment
                total_polarity += sentiment.polarity
                total_subjectivity += sentiment.subjectivity
                num += 1
        if num > 0:
            graph.node[node_id]['Tweet_Average_Polarity'] = total_polarity / num
            graph.node[node_id]['Tweet_Average_Subjectivity'] = total_subjectivity / num
        else: #TODO: Should these even be added? Technically the values are not 0
            graph.node[node_id]['Tweet_Average_Polarity'] = 0.0
            graph.node[node_id]['Tweet_Average_Subjectivity'] = 0.0