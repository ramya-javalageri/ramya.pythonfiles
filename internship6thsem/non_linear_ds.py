# class Node:
#     def __init__(self,key):
#         self.left=None
#         self.right=None
#         self.value=key
# class BinaryTree(Node):
#     def __init__(self,root_value):
#         self.root=Node(root_value)
#
#     def insert(self,c_n,value):
#         if value<c_n.value:
#             if c_n.left is None:
#                 c_n.left=Node(value)
#             else:
#                 self.insert(c_n.left,value)
#         else:
#             if c_n.right is None:
#                 c_n.right=Node(value)
#             else:
#                 self.insert(c_n.right,value)
#
#     def inorder(self,node):
#         if node:
#             self.inorder(node.left)
#             print(node.value,end=' ')
#             self.inorder(node.right)
#
#     def preorder(self,node):
#         if node:
#             print(node.value,end=' ')
#             self.preorder(node.left)
#             self.preorder(node.right)
#     def postorder(self,node):
#         if node:
#             self.inorder(node.left)
#             self.inorder(node.right)
#             print(node.value, end=' ')
    # def levelorder(self,node):
    #     if node:
    #         print(node.value,end=' ')
    #         self.levelorder(node.left)
    #         self.levelorder(node.right)
# bt=BinaryTree(5)
# bt.insert(bt.root,8)
# bt.insert(bt.root,4)
# bt.insert(bt.root,9)
# bt.insert(bt.root,6)
# bt.insert(bt.root,3)
# for i in range(5,10):
#     bt.insert(bt.root,i)
# bt.inorder(bt.root)
# print()
# bt.preorder(bt.root)
# print()
# bt.postorder(bt.root)
# print()
# bt.levelorder(bt.root)

# ...............................................................
# class Node:
#     def __init__(self,key):
#         self.left=None
#         self.right=None
#         self.value=key
# class BinaryTree(Node):
#     def __init__(self,root_value):
#         self.root=Node(root_value)
#
#     def insert(self,c_n,value):
#         if value<c_n.value:
#             if c_n.left is None:
#                 c_n.left=Node(value)
#             else:
#                 self.insert(c_n.left,value)
#         else:
#             if c_n.right is None:
#                 c_n.right=Node(value)
#             else:
#                 self.insert(c_n.right,value)
#
#     def inorder(self,node):
#         if node:
#             self.inorder(node.left)
#             print(node.value,end=' ')
#             self.inorder(node.right)
#     def update(self,node,pre,new):
#         if node:
#             if node.value==pre:
#                 node.value=new
#             self.update(node.left,pre,new)
#             print(node.value,end=' ')
#             self.update(node.right,pre,new)
#
#
# bt=BinaryTree(5)
# for i in range(3,10):
#     bt.insert(bt.root,i)
# bt.update(bt.root,6,10)

# ..........................................graph..........
# graph={
#     1:[2,4],
#     2:[3,1],
#     3:[4,2],
#     4:[1,3]
# }
# def traverse_graph(graph):
#     for node,neighbors in graph.items():
#         print(f"{node}-->{','.join(map(str,neighbors))}")
# traverse_graph(graph)

#..................Depth first search.......
# graph={
#     1:[2,4],
#     2:[3],
#     3:[4],
#     4:[1]
# }
#
# def dfs(graph,start):
#     visited=set()
#     stack=[start]
#     while stack:
#         node=stack.pop()
#         if node not in visited:
#             print(node,end='-->')
#             visited.add(node)
#             stack.extend(reversed(graph[node]))
#             print(stack,end='\n')
#     else:
#         print('Ended')
# print('dfs:')
# dfs(graph,1)

# .........................Breath first search...
# graph={
#     1:[2,4],
#     2:[3],
#     3:[4],
#     4:[1]
# }
# from collections import deque
# def bfs(graph,start):
#     visited=set()
#     queue=deque([start])
#     visited.add(start)
#     while queue:
#         node=queue.popleft()
#         print(node,end=' ')
#         for neighbor in graph[node]:
#             if neighbor not in visited:
#                 visited.add(neighbor)
#                 queue.append(neighbor)
# print("BFS:")
# print(bfs(graph,1))

# ..........
from collections import deque
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        # Dequeue a node from the front of the queue
        node = queue.popleft()
        print(node, end=" ")

        # Add all unvisited neighbors to the queue
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
graph={
    1:[2,4],
    2:[3],
    3:[4],
    4:[1]
}

# Perform BFS
print("\nBFS Traversal:")
bfs(graph,1)
