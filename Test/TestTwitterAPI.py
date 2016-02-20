from Data.API.TwitterAPI import TwitterAPI
import time


def test_search_keyword(keyword="#python"):
    api = TwitterAPI()
    start_time = time.time()
    count = api.get_statuses_from_keyword(search_query=keyword)
    print("--- %s seconds ---" % (time.time() - start_time))

    print "Downloaded {0} Statuses".format(count)
