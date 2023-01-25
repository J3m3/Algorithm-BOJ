input = __import__("sys").stdin.readline

vowels = set("aeiou")
consonants = set(chr(c) for c in range(ord('a'), ord('z')+1)) - vowels

while (password := input().rstrip()) != "end":
    vowel_count = 0
    prev = ''
    continuous_v = 0
    continuous_c = 0

    for i, char in enumerate(password):
        if prev == char and char not in "oe":
            print(f"<{password}> is not acceptable.")
            break

        if char in vowels:
            vowel_count += 1

            continuous_v += 1
            continuous_c = 0

        elif char in consonants:
            continuous_c += 1
            continuous_v = 0
        
        if continuous_c >= 3 or continuous_v >= 3:
            print(f"<{password}> is not acceptable.")
            break

        prev = char
    
    else:
        if vowel_count != 0:
            print(f"<{password}> is acceptable.")
        
        else:
            print(f"<{password}> is not acceptable.")