class Pool():
    def __init__(self):
        self.requests = []

    def push(self, request):
        self.requests.append(request)

    def pop(self):
        if len(self.requests) == 0:
            return None

        return self.requests.pop(0)



