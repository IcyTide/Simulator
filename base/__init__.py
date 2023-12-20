class Monitor(dict):
    def __missing__(self, key):
        return 0

    def __sub__(self, other: [int, float]):
        result = []
        for key, value in self.items():
            if value > other:
                self[key] = value - other
            else:
                result.append(key)
        return result

    def pop(self, __key):
        if __key in self:
            super().pop(__key)
