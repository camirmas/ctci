"""
Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
"""
# def is_unique(word: str) -> bool:
#     """Naive implementation."""
#     for i1, x in enumerate(word):
#         for i2, y in enumerate(word):
#             if i1 != i2 and x == y:
#                 return False
#     return True

def is_unique(word: str) -> bool:
    """Optimal implementation."""
    words = {}

    for char in word:
        if char in words:
            words[char] += 1
        else:
            words[char] = 1

    for char in word:
        if words[char] > 1:
            return False

    return True

# def is_unique(word: str) -> bool:
#     """Without additional data structures."""
#     word = sorted(word)

#     count = 0

#     while count < len(word)-1:
#         if word[count] == word[count+1]:
#             return False

#         count += 1
    
#     return True