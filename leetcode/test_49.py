from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    """
    how do I group the anagrams together?
    - Brute forth
        1. Make All words in the strs to anagrams (O(N) * O(K) = O(N*K) = O(N^2))
        2. Compare current anagram is equal to the other anagram.
           If the result is true, then group them together. (gotta check the index and skip it) = O(N^2)
    """
    anagrams = [""] * len(strs)
    for idx, value in enumerate(strs):
        anagrams[idx] = make_anagram_from(value)

    result = []
    checked_index = {}
    for i, current in enumerate(anagrams):
        if checked_index.get(i) is None:
            checked_index[i] = True
        else:
            continue

        current_group = [strs[i]]
        for j, other in enumerate(anagrams):
            if i == j:
                continue
            if current == other:
                if checked_index.get(j) is None:
                    checked_index[j] = True
                else:
                    continue
                current_group.append(strs[j])

        result.append(current_group)

    return result


def make_anagram_from(value: str):
    """
    Time Complexity: O(N) \n
    Space Complexity: O(N)
    Args:
        value: the word that you wanted to change to anagram

    Returns: anagram of given word

    """
    anagram = {}

    for ch in value:
        if anagram.get(ch) is not None:
            anagram[ch] += 1
        else:
            anagram[ch] = 1

    return anagram


if __name__ == "__main__":
    print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
