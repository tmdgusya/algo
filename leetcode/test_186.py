from typing import List

def reverseWords(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    left = 0
    right = len(s) - 1
    while left < right:
        tmp = s[left]
        s[left] = s[right]
        s[right] = tmp
        left += 1
        right -= 1
    
    start = 0
    point = 0
    while start <= len(s):
        if  start == len(s) or s[start] == " ":
            r = start - 1
            while point < r:
                tmp = s[point]
                s[point] = s[r]
                s[r] = tmp
                point += 1
                r -= 1
            point = start + 1
        start += 1

def test_case_1():
    s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
    expected = ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
    reverseWords(s=s)
    assert s == expected