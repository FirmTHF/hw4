def length_of_longest_substring_k_distinct(s: str, k: int) -> tuple:
    if k == 0:
        return 0, []

    n = len(s)
    left = 0
    right = 0
    max_length = 0
    max_substrings = []
    char_count = {}

    while right < n:
        if s[right] in char_count:
            char_count[s[right]] += 1
        else:
            char_count[s[right]] = 1

        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1

        current_length = right - left + 1
        if current_length > max_length:
            max_length = current_length
            max_substrings = [s[left:right+1]]
        elif current_length == max_length:
            max_substrings.append(s[left:right+1])

        right += 1

    return max_length, max_substrings

# Example usage:
if __name__ == '__main__':
    print(length_of_longest_substring_k_distinct("eceba", 2))  # Output: (3, ["ece"])
    print(length_of_longest_substring_k_distinct("aa", 1))     # Output: (2, ["aa"])
    print(length_of_longest_substring_k_distinct("a", 2))      # Output: (1, ["a"])
    print(length_of_longest_substring_k_distinct("abcadcacacaca", 3))  # Output: (11, ["cadcacacaca"])