def anagrams(string1, string2):
    """
    Returns True if the two strings are anagrams of each other, False otherwise.
    """
    return sorted(string1) == sorted(string2)

print(anagrams("tame", "meta"))  # True
print(anagrams("tame", "mate"))  # True
print(anagrams("tame", "team"))  # True
print(anagrams("tabby", "batty"))  # False
print(anagrams("python", "java"))  # False
