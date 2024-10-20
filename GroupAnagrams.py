def group_anagrams(words: list) -> list:
    anagrams = {}
    
    for word in words:
        # เรียงตัวอักษรในคำและใช้เป็นคีย์
        sorted_word = ''.join(sorted(word))
        
        # ถ้ายังไม่มีคีย์ในดิกชันนารี ให้สร้างรายการใหม่
        if sorted_word not in anagrams:
            anagrams[sorted_word] = []
        
        # เพิ่มคำในลิสต์ที่ตรงกับคีย์
        anagrams[sorted_word].append(word)
    
    # คืนค่าลิสต์ของลิสต์
    return list(anagrams.values())

# Example usage:
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))
# Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

words2 = ["listen", "silent", "enlist", "hello", "world"]
print(group_anagrams(words2))
# Output: [["listen", "silent", "enlist"], ["hello"], ["world"]]