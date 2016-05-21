from pymongo import MongoClient
from keys import keys

class TwitterMongo:
    def __init__(self):
        #client = MongoClient('localhost', 27017)
        #db = client.python_twitter
        client = MongoClient(keys['server'], keys['port'])
        db = client[keys['db_name']]
        db.authenticate(keys['user_name'], keys['password'])

        self.users = db.Users
        self.statuses = db.Statuses

    def save_user(self, user):
        return self.users.insert_one(user._json).inserted_id

    def save_users(self, users):
        for user in users:
            self.save_user(user)

    def save_status(self, status):
        if self.get_user(status.user.id_str) is None:
            self.save_user(status.user)
        return self.statuses.insert_one(status._json).inserted_id

    def save_statuses(self, statuses):
        for status in statuses:
            self.save_status(status)

    def get_user(self, user_id):
        return self.users.find_one({"id_str": "{0}".format(user_id)})

    def get_status(self, status_id):
        return self.statuses.find_one({"id_str": "{0}".format(status_id)})

    def get_user_statuses(self, user_id):
        return self.statuses.find({"user.id_str": str(user_id)})

    def get_followers(self, user_id):
        user = self.get_user(user_id)
        if "followers" in user:
            return user['followers']
        return None

    def get_following(self, user_id):
        user = self.get_user(user_id)
        if "following" in user:
            return user['following']
        return None

    def set_followers(self, user_id, followers):
        user = self.get_user(user_id)
        for follow in followers:
            self.users.update({"id_str": user["id_str"]}, {"$addToSet": {"followers": follow._json['id_str']}})

    def set_following(self, user_id, following):
        user = self.get_user(user_id)
        for follow in following:
            self.users.update({"id_str": user["id_str"]}, {"$addToSet": {"following": follow._json['id_str']}})
