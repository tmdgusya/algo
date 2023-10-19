from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    dict = {}

    for ele in nums:
        if ele in dict:
            return True
        dict[ele] = ele

    return False

def test_case():
    assert containsDuplicate([1, 2, 3, 1]) == True
    assert containsDuplicate([1, 2, 3, 4]) == False
    pass
