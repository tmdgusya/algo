from typing import List

def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    # we have to rotate the element by k
    # So, if k is 3, the first element in the array is going to move at 3
    # However, What if the array size is smaller than k
    # For example, if the given array nums is [1,2,3], and the k is 3
    # Where will I put the first element in the array?
    # I should put it at 0(zero), because it moved for 3 to right
    # AS = 3, K = 3, INDEX = 0 -> 0, INDEX = 1 -> 1
    # AS = 4, K = 3, INDEX = 0 -> 3, INDEX = 1 -> 0
    # If the formula to get an index where the element will being put in the array is (K + INDEX) % AS,
    copied_list = nums.copy()
    for index, ele in enumerate(nums):
        at = (k + index) % len(nums)
        nums[at] = copied_list[index]



def test_case_1():
    nums = [1,2,3,4,5,6,7]
    k = 3
    expected = [5,6,7,1,2,3,4]

    rotate(nums, k)
    print(nums)

    assert nums[0] == expected[0]