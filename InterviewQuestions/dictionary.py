class Dictionary:
    def __init__(self):
        self.keys = []
        self.values = []

    def add(self, key, value):
        has_updated = False
        for i, k in enumerate(self.keys):
            if k == key:
                self.keys[i] = key
                self.values[i] = value
                has_updated = True

        if not has_updated:
            self.keys.append(key)
            self.values.append(value)

    def remove(self, key):
        has_removed = False
        old_values = self.values
        for i, k in enumerate(self.keys):
            if has_removed:
                self.keys.append(k)
                self.values.append(old_values[i])
            if k == key:
                self.keys = self.keys[0:i - 1]
                self.values = self.values[0:i - 1]
                has_removed = True
