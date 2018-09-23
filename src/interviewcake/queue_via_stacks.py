# O(m) time where m is number of m function calls and O(n) space
class QueueFromStacks:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, item):
        self.in_stack.append(item)

    def dequeue(self):
        if len(self.out_stack) == 0:
            # Move over stack1 onto stack2 to reverse the stack
            while len(self.in_stack) > 1:
                self.out_stack.append(self.in_stack.pop())

            result = self.in_stack.pop()

        else:
            result = self.out_stack.pop()

        return result
