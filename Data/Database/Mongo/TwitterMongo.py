from pymongo import MongoClient


class TwitterMongo:
    def __init__(self):
        client = MongoClient('localhost', 27017)
        db = client.python_twitter

        self.users = db.Users
        self.statuses = db.Statuses

    def save_user(self, user):
        if self.get_user(user.id_str) is None:
            self.users.insert_one(user._json).inserted_id

    def save_status(self, status):
        if self.get_status(status.id_str) is None:
            self.statuses.insert_one(status._json).inserted_id
            self.save_user(status.user)

    def get_user(self, user_id):
        return self.users.find_one({"id_str": "{0}".format(user_id)})

    def get_status(self, status_id):
        return self.statuses.find_one({"id_str": "{0}".format(status_id)})
