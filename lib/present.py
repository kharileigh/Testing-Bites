class Present:
    def __init__(self):
        self.contents = None

    def wrap(self, contents):
        # exception if call wrap function again a second time on contents already wrapped
        if self.contents is not None:
            raise Exception("A contents has already been wrapped.")
        # wrap contents & store them
        self.contents = contents

    def unwrap(self):
        # exception when call unwrap function and no contents are stored
        if self.contents is None:
            raise Exception("No contents have been wrapped.")
        # returns if there is contents already store
        return self.contents
