class RequestForm:
    def __init__(self):
        self.order = None
        self.version = None
        self.loader = None
        self.search = None
        self.page = 1

    def clear(self):
        self.order = None
        self.version = None
        self.loader = None
        self.search = None
        self.page = 1
