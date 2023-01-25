input = __import__("sys").stdin.readline

def recursion(string, l, r, count):
    count += 1
    if l >= r:
        return (1, count)
    
    elif string[l] != string[r]:
        return (0, count)
    
    else:
        return recursion(string, l+1, r-1, count)

def is_palindrome(string):
    return recursion(string, 0, len(string)-1, 0)

N = int(input())
for _ in range(N):
    print(*is_palindrome(input().rstrip()))