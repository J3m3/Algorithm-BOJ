import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

def is_palindrome(seq, l, r):
    if l >= r:
        return True
    
    if seq[l] != seq[r]:
        return False

    return is_palindrome(seq, l+1, r-1)

def is_akaraka(seq, l, r):
    if l >= r:
        return True
    
    if not is_palindrome(seq, l, r):
        return False

    mid = (l + r) // 2
    if (l + r) & 1:
        return is_akaraka(seq, l, mid)
    else:
        return is_akaraka(seq, l, mid-1)


seq = input().rstrip()
if is_akaraka(seq, 0, len(seq)-1):
    print("AKARAKA")
else:
    print("IPSELENTI")