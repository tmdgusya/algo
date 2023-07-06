from typing import List

def wiggleSort(nums: List[int]) -> None:
        for i in range(len(nums)):
            # if count divide by 2 is even
            if i % 2 == 1 and i + 1 < len(nums):
                prev = nums[i]
                next = nums[i + 1]
                if prev < next:
                    nums[i + 1] = prev
                    nums[i] = next
            if i % 2 == 0 and i + 1 < len(nums):
                prev = nums[i]
                next = nums[i + 1]
                if prev > next:
                    nums[i + 1] = prev
                    nums[i] = next

def test_wiggle_sort():
    nums=[3,5,2,1,6,4]
    wiggleSort(nums)
    assert nums == [3,5,1,6,2,4]