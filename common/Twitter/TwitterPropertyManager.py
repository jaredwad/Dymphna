class TwitterPropertyManager:

    def __init__(self):
        pass

    @staticmethod
    def add_user_info(node, user):
        node['screen_name'] = user['screen_name']
        node['name'] = user['name']
        node['lang'] = user['lang']
        node['friends_count'] = user['friends_count']
        return

    @staticmethod
    def add_all(node, user):
        TwitterPropertyManager.add_user_info(node,user)