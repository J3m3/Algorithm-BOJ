input = __import__("sys").stdin.readline

def insert(trie, foods):
    t = trie
    for food in foods:
        if food not in t:
            t[food] = {}
        t = t[food]


def print_state(trie, depth):
    for food in sorted(trie.keys()):
        print(f"{'--' * depth}", food, sep="")
        print_state(trie[food], depth+1)

trie = {}
N = int(input())
for _ in range(N):
    _, *foods = input().split()
    insert(trie, foods)

print_state(trie, 0)