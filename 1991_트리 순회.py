input = __import__("sys").stdin.readline

def inorder(tree, start='A'):
    if tree[start][0] != '.':
        inorder(tree, tree[start][0])
    print(start, end="")
    if tree[start][1] != '.':
        inorder(tree, tree[start][1])


def preorder(tree, start='A'):
    print(start, end="")
    for child in tree[start]:
        if child != '.':
            preorder(tree, child)


def postorder(tree, start='A'):
    for child in tree[start]:
        if child != '.':
            postorder(tree, child)
    print(start, end="")

tree = {}
N = int(input())
for _ in range(N):
    parent, l, r = input().split()
    tree[parent] = [l, r]

preorder(tree)
print()
inorder(tree)
print()
postorder(tree)