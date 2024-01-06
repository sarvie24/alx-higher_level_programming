#!/usr/bin/python3
def magic_string():
    return '\n'.join(', '.join("BestSchool" for _ in range(i)) + '$' for i in range(1, 11))
print(magic_string())
