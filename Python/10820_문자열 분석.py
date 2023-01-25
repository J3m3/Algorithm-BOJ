from sys import stdin

for strings in stdin.readlines():
    info_map = {"low": 0, "up": 0, "digit": 0, ' ': 0}

    for char in strings:
        if char == ' ':
            info_map[' '] = info_map.get(' ', 0) + 1
        elif char.isupper():
            info_map["up"] = info_map.get("up", 0) + 1
        elif char.islower():
            info_map["low"] = info_map.get("low", 0) + 1
        elif char.isdigit():
            info_map["digit"] = info_map.get("digit", 0) + 1

    print(*info_map.values())