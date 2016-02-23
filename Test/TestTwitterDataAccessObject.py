from Data.DataAccess.TwitterDataAccessObject import TwitterDataAccessObject
import time

DEFAULT_USER_ID = 1259825000
# DEFAULT_USER_ID = 216751904
# DEFAULT_USER_ID = 813286
DEFAULT_NAME = '@JaredWads'
DEFAULT_KEYWORD = '#python'


def test_get_user(user_id=DEFAULT_USER_ID):
    dao = TwitterDataAccessObject()
    start_time = time.time()
    user = dao.get_user(user_id)
    print("--- test_get_user took {0} seconds ---".format(time.time() - start_time))
    print "Retrieved User {0}".format(user['screen_name'])


def test_get_user_statuses(user_id=DEFAULT_USER_ID):
    dao = TwitterDataAccessObject()
    start_time = time.time()
    statuses = dao.get_user_statuses(user_id)
    print("--- test_get_user took {0} seconds ---".format(time.time() - start_time))
    print "Retrieved {0} statuses".format(statuses.count())


def test_get_following(user_id=DEFAULT_USER_ID):
    dao = TwitterDataAccessObject()
    start_time = time.time()
    following = dao.get_following_by_user_id(user_id)
    print("--- test_get_user took {0} seconds ---".format(time.time() - start_time))
    print "Retrieved {0} following".format(len(following))


def test_get_followers(user_id=DEFAULT_USER_ID):
    dao = TwitterDataAccessObject()
    start_time = time.time()
    followers = dao.get_followers_by_user_id(user_id)
    print("--- test_get_user took {0} seconds ---".format(time.time() - start_time))
    print "Retrieved {0} following".format(len(followers))


def main():
    # test_get_user()
    # test_get_user_statuses()
    test_get_following()
    # test_get_followers()
