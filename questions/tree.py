class TreeNode:
    def __init__(self, value):
        self.value = value
        self.nodes = []

    def insert(self, node):
        self.nodes.append(node)


class Tree:
    def __init__(self, root: TreeNode):
        self.root = root

    def sum_levels(self):
        """
               3
              /| \
             1 4 11
            / / \ \
           0  2 5  3
        :return: [3, 16, 10]
        """
        result = []
        to_sum = []
        if not self.root:
            return result

        to_sum.append(self.root)
        while len(to_sum) > 0:
            sum = 0
            next_to_sum = []
            for node in to_sum:
                sum += node.value
                next_to_sum.extend(node.nodes)
            result.append(sum)
            to_sum = next_to_sum

        return result
