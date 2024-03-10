import heapq
import networkx as nx
import matplotlib.pyplot as plt
import uuid

class Node:
    def __init__(self, value=0, color="aqua"):
        self.left = None
        self.right = None
        self.value = value
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.value)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, key, color="aqua"):
        node = Node(key, color)
        heapq.heappush(self.heap, (key, node))
        return node

    def extract_min(self):
        if not self.heap:
            return None
        _, node = heapq.heappop(self.heap)
        return node

def build_heap():
    heap = MinHeap()
    root = heap.insert(3)
    heap.insert(8)
    heap.insert(5)
    heap.insert(2)
    heap.insert(7)
    heap.insert(9)
    heap.insert(1)
    heap.insert(4)
    heap.insert(6)

    return root

def visualize_heap(heap_root):
    heap = nx.DiGraph()
    pos = {heap_root.id: (0, 0)}
    heap = add_edges(heap, heap_root, pos)

    colors = [node[1]['color'] for node in heap.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in heap.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(heap, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()
    
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

draw_tree(root)

heap_root = build_heap()
visualize_heap(heap_root)

