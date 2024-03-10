import matplotlib.pyplot as plt
import networkx as nx
import random

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def inorder_traversal(root, colors, color_map):
    if root:
        inorder_traversal(root.left, colors, color_map)
        color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        colors.append(color)
        color_map[root.val] = color
        inorder_traversal(root.right, colors, color_map)

def breadth_first_traversal(root, colors, color_map):
    queue = [root]
    while queue:
        node = queue.pop(0)
        color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        colors.append(color)
        color_map[node.val] = color
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

def visualize_tree(root, traversal_type):
    colors = []
    color_map = {}
    
    if traversal_type == 'inorder':
        inorder_traversal(root, colors, color_map)
    elif traversal_type == 'breadth_first':
        breadth_first_traversal(root, colors, color_map)
    else:
        print("Invalid traversal type. Choose 'inorder' or 'breadth_first'.")
        return
    
    G = nx.Graph()
    G.add_node(root.val, color=color_map[root.val])
    visualize_tree_recursive(root, G, color_map)
    
    pos = nx.spring_layout(G)
    node_colors = [color_map[node] for node in G.nodes()]
    
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color=node_colors)
    plt.show()

def visualize_tree_recursive(node, G, color_map):
    if node.left:
        G.add_node(node.left.val, color=color_map[node.left.val])
        G.add_edge(node.val, node.left.val)
        visualize_tree_recursive(node.left, G, color_map)
    if node.right:
        G.add_node(node.right.val, color=color_map[node.right.val])
        G.add_edge(node.val, node.right.val)
        visualize_tree_recursive(node.right, G, color_map)

root = None
keys = [50, 30, 70, 20, 40, 60, 80]

for key in keys:
    root = insert(root, key)

visualize_tree(root, 'inorder') 
visualize_tree(root, 'breadth_first')
