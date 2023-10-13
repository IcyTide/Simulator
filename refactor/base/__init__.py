from sortedcontainers import SortedDict


class Timeline:
    def __init__(self):
        self.data = SortedDict()  # key -> value
        self.index = {}  # value -> key

    def set(self, key, value):
        # update
        if value in self.index:
            if self.index[value] < key:
                return
            self.data[self.index.pop(value)].remove(value)

        # insert
        if key not in self.data:
            self.data[key] = []
        self.data[key].append(value)
        self.index[value] = key

    @property
    def next(self):
        gap, actions = self.data.popitem(0)
        self.data = SortedDict((k - gap, v) for k, v in self.data.items())
        return gap, actions
