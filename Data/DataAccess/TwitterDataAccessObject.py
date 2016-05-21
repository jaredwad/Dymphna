from Data.API.TwitterAPI import TwitterAPI
from Data.Database.ElasticSearch.TwitterElasticSearch import TwitterElasticSearch
from Data.Database.Mongo.TwitterMongo import TwitterMongo


# TODO: Make this database agnostic rather than elasticsearch specific
class TwitterDataAccessObject:
    def __init__(self):
        self.api = TwitterAPI()
        self.db = TwitterElasticSearch()

    def get_user(self, user_id):
        user = self.db.get_user(user_id)
        if user is None:
            self.db.save_user(self.api.get_user_by_id(user_id))
            user = self.db.get_user(user_id)
        return user

    def get_user_statuses(self, user_id, force_refresh=False):
        # self.get_user(user_id)
        statuses = self.db.get_user_statuses(user_id)
        if statuses is None or force_refresh is True:
            self.db.save_statuses(self.api.get_user_statuses(user_id))
            statuses = self.db.get_user_statuses(user_id)
        return statuses

    def get_followers_ids_by_user_id(self, user_id, force_refresh=False):
        # self.get_user(user_id)
        followers = self.db.get_followers(user_id)
        if followers is None or force_refresh is True:

            followerids = []

            for follow in self.api.get_followers_by_user_id(user_id):
                followerids.append(follow._json['id_str'])

            self.db.set_followers(user_id, followerids)
            followers = self.db.get_followers(user_id)
        followerids = []

        if followers is not None:
            for hit in followers:
                followerids.append(hit['_source']['user'])

        return followerids

    def get_following_ids_by_user_id(self, user_id, force_refresh=False):
        # self.get_user(user_id)
        following = self.db.get_following(user_id)
        if following is None or force_refresh is True:

            followingids = []

            for follow in self.api.get_following_by_user_id(user_id):
                followingids.append(follow._json['id_str'])

            self.db.set_following(user_id, followingids)
            following = self.db.get_following(user_id)
        followingids = []

        if following is not None:
            for hit in following:
                followingids.append(hit['_source']['following'])

        return followingids
