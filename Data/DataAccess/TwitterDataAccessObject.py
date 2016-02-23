from Data.API.TwitterAPI import TwitterAPI
from Data.Database.Mongo.TwitterMongo import TwitterMongo


class TwitterDataAccessObject:
    def __init__(self):
        self.api = TwitterAPI()
        self.db = TwitterMongo()

    def get_user(self, user_id):
        user = self.db.get_user(user_id)
        if user is None:
            self.db.save_user(self.api.get_user_by_id(user_id))
            user = self.db.get_user(user_id)
        return user

    def get_user_statuses(self, user_id):
        statuses = self.db.get_user_statuses(user_id)
        if statuses.count() is 0:
            self.db.save_statuses(self.api.get_user_statuses(user_id))
            statuses = self.db.get_user_statuses(user_id)
        return statuses

    def get_followers_ids_by_user_id(self, user_id):
        followers = self.db.get_followers(user_id)
        if followers is None:
            self.db.set_followers(user_id, self.api.get_followers_by_user_id(user_id))
            followers = self.db.get_followers(user_id)
        return followers

    def get_following_ids_by_user_id(self, user_id):
        following = self.db.get_following(user_id)
        if following is None:
            self.db.set_following(user_id, self.api.get_following_by_user_id(user_id))
            following = self.db.get_following(user_id)
        return following

    def get_followers_by_user_id(self, user_id):
        followers_ids = self.get_followers_ids_by_user_id(user_id)
        followers = []
        for follower_id in followers_ids:
            followers.append(self.get_user(follower_id))
        return followers

    def get_following_by_user_id(self, user_id):
        following_ids = self.get_following_ids_by_user_id(user_id)
        following = []
        for following_id in following_ids:
            following.append(self.get_user(following_id))
        return following
