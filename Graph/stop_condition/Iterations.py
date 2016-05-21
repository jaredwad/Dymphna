class Iterations:
    def __init__(self, num_iter=10):
        self.num_iter = num_iter

    def should_stop(self):
        if self.num_iter <= 0:
            return True
        self.num_iter -= 1
        return False
