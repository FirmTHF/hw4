def group_anagrams(words: list) -> list:
    anagrams = {}

    for word in words:
        sorted_word = "".join(sorted(word))
        if sorted_word not in anagrams:
            anagrams[sorted_word]= []
        anagrams[sorted_word].append(word)
    return list(anagrams.values())

# Example usage:
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))
# Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

words2 = ["listen", "silent", "enlist", "hello", "world"]
print(group_anagrams(words2))
# Output: [["listen", "silent", "enlist"], ["hello"], ["world"]]