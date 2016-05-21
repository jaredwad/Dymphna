class BasicSelector:
    def __init__(self):
        pass

    @staticmethod
    def get_next(fringe):
        if len(fringe) > 0:
            return fringe[0]
        return None
