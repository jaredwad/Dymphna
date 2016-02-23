import tweepy
import sys
from keys import keys


class TwitterAPI:
    def __init__(self):
        self.CONSUMER_KEY = keys['consumer_key']
        self.CONSUMER_SECRET = keys['consumer_secret']
        self.ACCESS_TOKEN = keys['access_token']
        self.ACCESS_TOKEN_SECRET = keys['access_token_secret']

        self.auth = tweepy.AppAuthHandler(self.CONSUMER_KEY, self.CONSUMER_SECRET)

        self.api = tweepy.API(self.auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

        if not self.api:
            print "Can't Authenticate"
            sys.exit(-1)

    def get_statuses_from_keyword(self, search_query, max_tweets=45000, tweets_per_qry=100
                                  , since_id=None, max_id=-1L):
        """
        Searches for all tweets for a given keyword
        Code adapted from "http://www.karambelkar.info/2015/01/how-to-use-twitters-search-rest-api-most-effectively./"
        18/Feb/2016

        :param search_query: what we're searching for
        :param max_tweets: The maximum number of tweets to retrieve
        :param tweets_per_qry: the number of tweets per 'page' (max=100)
        :param since_id: If results from a specific ID onwards are reqd, set since_id to that ID.
                          else default to no lower limit, go as far back as API allows
        :param max_id: If results only below a specific ID are, set max_id to that ID.
                        else default to no upper limit, start from the most recent tweet matching the search query.
        """
        tweet_count = 0
        print("Downloading max {0} tweets".format(max_tweets))
        tweets = []
        while tweet_count < max_tweets:
            try:
                if max_id <= 0:
                    if not since_id:
                        new_tweets = self.api.search(q=search_query, count=tweets_per_qry)
                    else:
                        new_tweets = self.api.search(q=search_query, count=tweets_per_qry,
                                                     since_id=since_id)
                else:
                    if not since_id:
                        new_tweets = self.api.search(q=search_query, count=tweets_per_qry,
                                                     max_id=str(max_id - 1))
                    else:
                        new_tweets = self.api.search(q=search_query, count=tweets_per_qry,
                                                     max_id=str(max_id - 1),
                                                     since_id=since_id)
                if not new_tweets:
                    print "No more tweets found"
                    break
                for tweet in new_tweets:
                    tweets.append(tweet)
                tweet_count += len(new_tweets)
                print "Downloaded {0} tweets".format(tweet_count)
                max_id = new_tweets[-1].id
            except tweepy.TweepError as e:
                # Just exit if any error
                print "some error : " + str(e)
                break
        return tweets

    def get_user_statuses(self, user_id):
        followers = []
        count = 0
        for user in tweepy.Cursor(self.api.user_timeline, user_id=user_id).items():
            followers.append(user)
            count += 1
            if count % 100 == 0:
                print "Downloaded {0} items".format(count)
        return followers

    def get_followers_by_user_id(self, user_id):
        followers = []
        count = 0
        for user in tweepy.Cursor(self.api.followers, user_id=user_id).items():
            followers.append(user)
            count += 1
            if count % 100 == 0:
                print "Downloaded {0} items".format(count)
        return followers

    def get_following_by_user_id(self, user_id):
        following = []
        count = 0
        for user in tweepy.Cursor(self.api.friends, user_id=user_id).items():
            following.append(user)
            count += 1
            if count % 100 == 0:
                print "Downloaded {0} items".format(count)
        return following
