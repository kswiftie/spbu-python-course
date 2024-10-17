class Evaluated:
    def __init__(self, func):
        self.func = func

    def evaluate(self):
        return self.func()
