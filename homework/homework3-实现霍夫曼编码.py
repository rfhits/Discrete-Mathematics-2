import sys
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
global V
global E

def draw_graph(E):
    '''通过边集，画无向图'''
    G = nx.Graph()
    G.add_edges_from(E)
    nx.draw(G, node_size=200, node_color='r', with_labels=True, font_color='g')
    plt.show()
    return

class Node:
    def __init__(self, char, freq, code=None):
        self.char = char  # 字符
        self.freq = freq  # 字频
        self.code = code  # 编码
        self.left = None
        self.right = None
        self.father = None

    def is_left_child(self):
        """判断是否为左节点"""
        return self.father.left == self


def create_node_list(char_set, freq_set):
    """生成最初节点的list"""
    if(len(freq_set) != len(char_set)):
        print("length not match")
        sys.exit(0)
    nodes = []
    for i in range(len(char_set)):
        char = char_set[i]
        freq = freq_set[i]
        nodes.append(Node(char, freq))
    return nodes


def create_Huffman_tree(nodes):
    """创建哈夫曼树"""
    tree_nodes = nodes.copy()
    while len(tree_nodes) > 1:
        tree_nodes.sort(key=lambda node: node.freq)
        # 取出频率最小的节点
        left_node = tree_nodes.pop(0)
        right_node = tree_nodes.pop(0)

        # 做一父节点
        father_node_char = str(left_node.char) + '+' + str(right_node.char)
        father_node = Node(
            father_node_char, (left_node.freq + right_node.freq))
        father_node.left = left_node
        father_node.right = right_node
        left_node.father = right_node.father = father_node
        tree_nodes.append(father_node)
    tree_nodes[0].father = None  # 根节点父亲为None
    return tree_nodes[0]  # 返回根节点


def get_Huffman_code(nodes):
    """获取Huffman编码"""
    codes = {}
    for node in nodes:
        code = ''
        char = node.char
        while node.father != None:
            if node.is_left_child():
                code = '0' + code
            else:
                code = '1' + code
            node = node.father
        codes[char] = code
    return codes


def travel(root):
    if root == None:
        return 

    global V, E
    V.append(root.char)
    if (root.left != None): 
        E.append((root.char, root.left.char))
        travel(root.left)

    if (root.right != None):
        E.append((root.char, root.right.char))
        travel(root.right)
    return(V, E)


char_set = ['a', 'b', 'c', 'd', 'e']
freq_set = [0.4, 0.1, 0.2, 0.15, 0.15]
V = []
E = []
nodes = create_node_list(char_set, freq_set)
root = create_Huffman_tree(nodes)
codes = get_Huffman_code(nodes)

for key in codes.keys():
    print(key, ': ', codes[key])

travel(root)
draw_graph(E)