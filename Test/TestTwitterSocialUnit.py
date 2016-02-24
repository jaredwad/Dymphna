from common.Twitter.TwitterSocialUnit import TwitterSocialUnit
import time

DEFAULT_ID = 1259825000
# DEFAULT_ID = 216751904
# DEFAULT_ID = 813286


def test_get_statuses(user_id=DEFAULT_ID):
    tsu = TwitterSocialUnit(user_id)
    start_time = time.time()
    statuses = tsu.get_statuses()
    print("--- test_get_user_by_id took {0} seconds ---".format(time.time() - start_time))
    print "Retrieved {0} Statuses".format(statuses.count())


def test_get_incoming_neighbors(user_id=DEFAULT_ID):
    tsu = TwitterSocialUnit(user_id)
    start_time = time.time()
    neighbors = tsu.get_incoming_neighbors()
    print("--- test_get_user_by_id took {0} seconds ---".format(time.time() - start_time))
    print "Retrieved {0} Neighbors".format(len(neighbors))


def test_get_outgoing_neighbors(user_id=DEFAULT_ID):
    tsu = TwitterSocialUnit(user_id)
    start_time = time.time()
    neighbors = tsu.get_outgoing_neighbors()
    print("--- test_get_user_by_id took {0} seconds ---".format(time.time() - start_time))
    print "Retrieved {0} Neighbors".format(len(neighbors))


def test_get_keyword_count_in_statuses(user_id=DEFAULT_ID, keyword="link"):
    tsu = TwitterSocialUnit(user_id)
    start_time = time.time()
    count = tsu.get_keyword_count_in_statuses(keyword)
    print("--- test_get_user_by_id took {0} seconds ---".format(time.time() - start_time))
    print "{0} statuses contained the word {1}".format(count, keyword)


def main():
    #test_get_statuses()
    #test_get_incoming_neighbors()
    #test_get_outgoing_neighbors()
    test_get_keyword_count_in_statuses()

main()
