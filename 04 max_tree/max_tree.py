import numpy as np
from collections import deque
import matplotlib.pyplot as plt

class max_tree():
    def __init__(self, buffer_size):
        self.tree_index = buffer_size - 1 # define max_tree leaf node index.
        self.array_tree = [0 for i in range((buffer_size * 2) - 1)] # set max_tree size (double of buffer size)
        self.buffer_size = buffer_size

    def update_tree(self, index):
        # index is a starting leaf node point.
        while True:
            index = (index - 1)//2 # parent node index.
            left = (index * 2) + 1 # left child node inex.
            right = (index * 2) + 2 # right child node index
            if self.array_tree[left] > self.array_tree[right]: # if a left child node is bigger than right.
                self.array_tree[index] = self.array_tree[left]
            else:
                self.array_tree[index] = self.array_tree[right]
            if index == 0: ## if index is a root node.
                break

    def add_data(self, priority):
        if self.tree_index == (self.buffer_size * 2) - 1: # if min tree index achive last index.
            self.tree_index = self.buffer_size - 1 # change frist leaf node index.
        
        self.array_tree[self.tree_index] = priority # append priority at current max_tree leaf node index.
        self.update_tree(self.tree_index) # update max_tree node. propagate from leaf node to root node.
        self.tree_index += 1 # count current max_tree index

def main():
    buffer_size = 8
    priority_list = [5,10,2,8,1,100,15,35] # priority list
    Max_tree = max_tree(buffer_size) # max_tree.

    for p in priority_list: # add 8 test data and priority.
        Max_tree.add_data(p)
    cnt = 1
    cnt2 = 1
    for i,d in enumerate(Max_tree.array_tree):
        if i == cnt:
            print()
            cnt = cnt + np.power(2,cnt2)
            cnt2 +=1
        print(d , end=' ')
    print()
    
  
if __name__ == '__main__':
    main()
    