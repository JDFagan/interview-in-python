class QueueFromStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        # Move over entire stack1 onto stack2 to reverse the stack
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())

        result = self.stack2.pop()

        # Move over rest of stack2 back onto stack1 to receive new enqueue requests
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())

        return result

    def as_list(self):
        return self.stack1
