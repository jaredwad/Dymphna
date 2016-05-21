import sys
from elasticsearch import Elasticsearch, NotFoundError


class TwitterElasticSearch:
    def __init__(self, max_return_size=10000):
        self.es = Elasticsearch()
        self.max_return_size = max_return_size

    def save_status(self, status):
        self.es.index(index="twitter", doc_type="statuses", id=status.id_str, body=status._json)
        return status.id_str

    def save_statuses(self, statuses):
        for status in statuses:
            self.save_status(status)

    def get_status(self, status_id):
        try:
            return self.es.get(index='twitter', doc_type='statuses', id=status_id)
        except NotFoundError:
            return None

    def get_user_statuses(self, user_id):
        try:
            statuses = self.es.search(index='twitter', q='user.id_str:"{0}"'.format(user_id), size=self.max_return_size)
            if statuses['hits']['total'] <= 0:
                return None

            sources = []

            for status in statuses['hits']['hits']:
                sources.append(status['_source'])

            return sources
        except NotFoundError:
            return None

    def get_user(self, user_id):
        statuses = self.get_user_statuses(user_id)
        if statuses is not None:
            return statuses[0]['user']
        return None

    def get_followers(self, user_id):
        followers = self.es.search(index="twitter_follow", q='following:"{0}"'.format(user_id), size=self.max_return_size)

        if followers['hits']['total'] <= 0:
            return None
        return followers['hits']['hits']

    def get_following(self, user_id):
        following = self.es.search(index="twitter_follow", q='user:"{0}"'.format(user_id), size=self.max_return_size)

        if following['hits']['total'] <= 0:
            return None
        return following['hits']['hits']

    def set_followers(self, user_id, followers):
        for follow in followers:
            self.es.index(index='twitter_follow', doc_type='follow',
                          body={'user': follow, 'following': user_id})

    def set_following(self, user_id, following):
        for follow in following:
            self.es.index(index='twitter_follow', doc_type='follow',
                          body={'user': "{0}".format(user_id), 'following': follow})
