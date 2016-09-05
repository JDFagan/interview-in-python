class TempTracker:
    # Insert: O(1) time and O(1) space
    # Getters: O(1) time

    def __init__(self):
        self.sum = 0
        self.count = 0
        self.temps_histogram = dict()

        self.max = None
        self.min = None
        self.mean = None
        self.mode = None

    def insert(self, temp):
        self.max = temp if self.max is None else max(self.max, temp)
        self.min = temp if self.min is None else min(self.min, temp)

        # Track the mean
        self.sum += temp
        self.count += 1
        self.mean = temp if self.mean is None else self.sum/self.count

        # Track the mode
        if temp in self.temps_histogram:
            self.temps_histogram[temp] += 1
        else:
            self.temps_histogram[temp] = 1

        if self.mode is None:
            self.mode = (temp, 1)
        elif self.mode[1] < self.temps_histogram[temp]:
            self.mode = (temp, self.temps_histogram[temp])

    def get_max(self):
        return self.max

    def get_min(self):
        return self.min

    def get_mean(self):
        return self.mean

    def get_mode(self):
        return None if self.mode is None else self.mode[0]
