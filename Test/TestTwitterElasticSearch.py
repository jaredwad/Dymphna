from Data.Database.ElasticSearch.TwitterElasticSearch import TwitterElasticSearch

# DEFAULT_ID = 1259825000
DEFAULT_USER_ID = 21950044
DEFAULT_STATUS_ID = 699939766620577796


def test_get_user(user_id):
    db = TwitterElasticSearch()
    user = db.get_user(user_id)
    if user is None:
        print "Couldn't find user"
    else:
        print "Found user: {0}".format(user['screen_name'])


def test_get_user_statuses(user_id):
    db = TwitterElasticSearch()
    statuses = db.get_user_statuses(user_id)
    if statuses is None:
        print "Couldn't find status"
    else:
        for status in statuses:
            print "Found status: {0}".format(status['text'].encode('utf-8'))


def test_get_status(status_id):
    db = TwitterElasticSearch()
    status = db.get_status(status_id)
    if status is None:
        print "Couldn't find status"
    else:
        print status['text']


def main():
    test_get_user(DEFAULT_USER_ID)
    test_get_user_statuses(DEFAULT_USER_ID)
    test_get_status(DEFAULT_STATUS_ID)

main()