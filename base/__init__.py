class Monitor(dict):
    def __init__(self, default):
        super().__init__()
        self.default = default

    def __missing__(self, key):
        return self.default

    def __sub__(self, other: [int, float]):
        result = []
        for key, value in self.items():
            if value > other:
                self[key] = value - other
            else:
                result.append(key)
        return result

    def __add__(self, other: dict):
        result = {}
        for key, value in self.items():
            result[key] = value
        for key, value in other.items():
            result[key] = value
        return result.items()

    def pop(self, __key):
        if __key in self:
            super().pop(__key)
