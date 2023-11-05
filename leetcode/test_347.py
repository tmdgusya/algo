import operator
import unittest
from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    """
    Return the k most frequent numbers.

    So, I'll just check the count of each number and save them into a hash map as shown below:
    { number: the number of occurrences }

    Then, loop over the keys and values of the map until k becomes zero
    """
    map = {}
    answer = []
    for num in nums:
        if map.get(num) is None:
            map[num] = 1
        else:
            map[num] += 1

    sorted_dict = dict(sorted(map.items(), key=operator.itemgetter(1), reverse=True))

    for key in sorted_dict:
        if k == 0:
            break
        answer.append(key)
        k -= 1
    return answer

if __name__ == "__main__":
    print(topKFrequent([1,2,2,3,3,3], k=2))