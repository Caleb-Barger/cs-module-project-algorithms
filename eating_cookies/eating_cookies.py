'''
Input: an integer
Returns: an integer
'''

class BSTNode:
    def __init__(self, value=0):
        self.value = value
        # self.prev = None
        self.node1 = None
        self.node2 = None
        self.node3 = None
    def is_leaf(self):
        if self.node1 is None and self.node2 is None and self.node3 is None:
            return True
        return False

def eating_cookies(n, count=0, current_node=BSTNode()):
    # Using a BST count the ways to eat n cookies
    # via eating them 1, 2, or 3 at a time

    # starting from 0
    # value = 0 
    # if the value of the current path
    # + 3 is less than or equal to n
    if current_node.value + 3 <= n:
        # value += 3
        # then create a new node with a value of 3
        new_node = BSTNode(3)
        # link up the current node's
        # .node3 with the newly made node
        current_node.node3 = new_node
        # return a call to self with (n, count, current_node)
        return eating_cookies(n, count, new_node)
    # ... same thing for 2
    if current_node.value + 2 <= n:
        new_node = BSTNode(2)
        current_node.node2 = new_node
        return eating_cookies(n, count, new_node)
    # ... same thing for 3
    if current_node.value + 1 <= n:
        new_node = BSTNode(1)
        current_node.node1 = new_node
        return eating_cookies(n, count, new_node)
    # if the current node does not lead anywhere
    if current_node.is_leaf():
    # increment count by 1
        count += 1

    return count


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
