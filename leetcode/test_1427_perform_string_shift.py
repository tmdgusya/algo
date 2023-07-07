from typing import List

def stringShift(s: str, shift: List[List[int]]) -> str:
        _s = list(s)
        for i in range(0, len(shift)):
            direction = shift[i][0]
            amount = shift[i][1]
            shouldBePoped = amount % len(s)

            if direction == 1:
                elements = []
                # To be right shift
                for j in range(shouldBePoped):
                    elements.insert(0, _s.pop(len(_s) - 1))
                _s = elements + _s

            else:
                elements = []
                # To be right shift
                for j in range(shouldBePoped):
                    elements.append(_s.pop(0))
                _s = _s + elements
    
        return "".join(_s)
    
def test_case_1():
    assert stringShift("abc", [[0,1],[1,2]]) == "cab"

def test_case_2():
    assert stringShift("abcdefg", [[1,1],[1,1],[0,2],[1,3]]) == "efgabcd"