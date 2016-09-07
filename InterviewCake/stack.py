class Stack:

    # initialize an empty list
    def __init__(self):
        self.items = []

    # push a new item to the last index
    def push(self, item):
        self.items.append(item)

    # remove the last item
    def pop(self):
        # if the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        return self.items.pop()

    # see what the last item is
    def peek(self):
        if not self.items:
            return None
        return self.items[len(self.items) - 1]


# O(1) time and O(m) additional space for m operations called on the stack
class MaxStack(Stack):

    def __init__(self):
        super().__init__()
        self.maxes = Stack()

    def push(self, item):
        super().push(item)
        if not self.maxes.peek() or item > self.maxes.peek():
            self.maxes.push(item)

    def pop(self):
        item = super().pop()
        if item and item == self.maxes.peek():
            self.maxes.pop()
        return item

    # see what the max item is
    def get_max(self):
        return self.maxes.peek()
