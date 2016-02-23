from Data.API.TwitterAPI import TwitterAPI
import time

#DEFAULT_ID = 1259825000
#DEFAULT_ID = 216751904
DEFAULT_ID = 813286
DEFAULT_NAME = '@JaredWads'
DEFAULT_KEYWORD = '#python'


def test_search_keyword(keyword=DEFAULT_KEYWORD):
    api = TwitterAPI()
    start_time = time.time()
    statuses = api.get_statuses_from_keyword(search_query=keyword, max_tweets=1000)
    print("--- test_search_keyword took {0} seconds ---".format(time.time() - start_time))
    print "Downloaded {0} Statuses".format(len(statuses))


def test_get_followers(user_id=DEFAULT_ID):
    api = TwitterAPI()
    start_time = time.time()
    followers = api.get_followers_by_user_id(user_id=user_id)
    print("--- test_get_followers took {0} seconds ---".format(time.time() - start_time))
    print "Downloaded {0} Users".format(len(followers))


def test_get_following(user_id=DEFAULT_ID):
    api = TwitterAPI()
    start_time = time.time()
    following = api.get_following_by_user_id(user_id=user_id)
    print("--- test_get_following took {0} seconds ---".format(time.time() - start_time))
    print "Downloaded {0} Users:".format(len(following))
    for user in following:
        print '\t' + user.screen_name


def test_get_user_statuses(user_id=DEFAULT_ID):
    api = TwitterAPI()
    start_time = time.time()
    statuses = api.get_user_statuses(user_id)
    print("--- test_search_keyword took {0} seconds ---".format(time.time() - start_time))
    print "Downloaded {0} Statuses".format(len(statuses))


def main():
    #test_search_keyword()
    #test_get_following()
    #test_get_followers()
    test_get_user_statuses()


# run tests
main()
