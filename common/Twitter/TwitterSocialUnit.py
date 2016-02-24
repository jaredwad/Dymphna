from Data.DataAccess.TwitterDataAccessObject import TwitterDataAccessObject
from common.SocialUnit import SocialUnit


class TwitterSocialUnit(SocialUnit):
    def __init__(self, id):
        SocialUnit.__init__(self)
        self.id = id
        self.incoming_Neighbors = None
        self.outgoing_Neighbors = None
        self.incoming_Neighbors_ids = None
        self.outgoing_Neighbors_ids = None
        self.statuses = None

        self.dao = TwitterDataAccessObject()

        self.inner_User = self.dao.get_user(id)

    def get_incoming_neighbors(self, force_refresh=False):
        if force_refresh or self.incoming_Neighbors is None:
            self.incoming_Neighbors = self.dao.get_followers_by_user_id(self.id)
        return self.incoming_Neighbors

    def get_outgoing_neighbors(self, force_refresh=False):
        if force_refresh or self.outgoing_Neighbors is None:
            self.outgoing_Neighbors = self.dao.get_following_by_user_id(self.id)
        return self.outgoing_Neighbors

    def get_incoming_neighbors_ids(self, force_refresh=False):
        if force_refresh or self.incoming_Neighbors_ids is None:
            self.incoming_Neighbors_ids = self.dao.get_followers_ids_by_user_id(self.id)
        return self.incoming_Neighbors_ids

    def get_outgoing_neighbors_ids(self, force_refresh=False):
        if force_refresh or self.outgoing_Neighbors_ids is None:
            self.outgoing_Neighbors_ids = self.dao.get_following_ids_by_user_id(self.id)
        return self.outgoing_Neighbors_ids

    def get_statuses(self, force_refresh=False):
        if force_refresh or self.statuses is None:
            self.statuses = self.dao.get_user_statuses(self.id)
        return self.statuses

    def get_keyword_count_in_statuses(self, keyword):
        statuses = self.get_statuses()
        count = 0
        for status in statuses:
            if keyword in status['text']:
                count += 1
        return count
