input = __import__("sys").stdin.readline

def find(n):
    if people[n] == n:
        return n
    people[n] = find(people[n])
    return people[n]


def union(a, b):
    a = find(a)
    b = find(b)

    if a in know_set:
        people[b] = a
    else:
        people[a] = b


def is_union(a, b):
    a = find(a)
    b = find(b)
    return True if a == b else False

N, M = map(int, input().split())
know_count, *know_arr = map(int, input().split())
know_set = set(know_arr)

people = [i for i in range(N+1)]
graph = [[] for _ in range(M)]
for i in range(M):
    _, *arr = map(int, input().split())
    graph[i] = arr
    for j in range(len(arr)-1):
        union(arr[j], arr[j+1])

count = 0
for pl in graph:
    for p in pl:
        if find(p) in know_set:
            break
    else:
        count += 1
print(count)