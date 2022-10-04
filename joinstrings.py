#Resources Used:
# Please note: I didn't necessarily use code from all of them, but reading through them gave me ideas
# https://www.geeksforgeeks.org/linked-list-set-1-introduction/
# https://stackoverflow.com/questions/39585740/how-can-i-print-all-of-the-values-of-the-nodes-in-my-singly-linked-list-using-a
# https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm

from __future__ import print_function

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.tail = None
        self.used = False

n = int(raw_input())

if n == 1:
    print(raw_input())

else:
    #List of nodes to be linked
    nodes = list()
    for i in range(n):
        a = Node(raw_input())
        nodes.append(a)

    for i in range(n - 1):
        # 3 2
        line = raw_input() #'3 2'
        arr = line.split() #[3, 2]

        if nodes[int(arr[1]) - 1].used is False:
            nodes[int(arr[1]) - 1].used = True
            # If there is no tail
            if nodes[int(arr[0]) - 1].tail is None:
                nodes[int(arr[0]) - 1].next = nodes[int(arr[1]) - 1]

                if nodes[int(arr[1]) - 1].tail is None:
                    nodes[int(arr[0]) - 1].tail = nodes[int(arr[1]) - 1]
                else:
                    nodes[int(arr[0]) - 1].tail = nodes[int(arr[1]) - 1].tail

            # If there is a tail
            else:
                nodes[int(arr[0]) - 1].tail.next = nodes[int(arr[1]) - 1]

                if nodes[int(arr[1]) - 1].tail is None:
                    nodes[int(arr[0]) - 1].tail = nodes[int(arr[1]) - 1]
                else:
                    nodes[int(arr[0]) - 1].tail = nodes[int(arr[1]) - 1].tail

    node =  nodes[int(arr[0]) - 1]
    while node:
        print(node.data, end="")
        node = node.next
