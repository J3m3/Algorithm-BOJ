input = __import__("sys").stdin.readline

N = int(input())
books = {}
for _ in range(N):
    books[book] = books.get(book := input().rstrip(), 0) + 1

print(
    sorted(list(books.items()), key=lambda x: (-x[1], x[0]))[0][0]
)
