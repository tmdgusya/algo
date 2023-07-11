from copy import deepcopy

def shortestWay(source: str, target: str) -> int:
    """
    subsequence of string is a new string that formed by original string 
    by deleting some of characters.
    
    Args:
        source (str): subsequence of string
        target (str): original string

    Returns:
        int: the minimum number of subsequence of target, their concatenation equals target. (If it is impossible, then we will return -1)
    """
    order = -1
    count_of_counsequence = 0
    _sources = list(source)
    _sub_string = 0
    
    _dict = {}
    
    for c in source:
        if c in _dict:
            _dict[c] += 1
        else:
            _dict[c] = 1
                
    init = deepcopy(_dict)
    
    i = 0
    while i < len(target):
        char = target[i]
        if char not in _sources:
            # can not construct by target
            return -1

        # we need to consider order when we use word and the word is already used
        try:
            order_or_char = _sources.index(char, order + 1, len(_sources))
        except ValueError:
            count_of_counsequence += 1
            order = -1
            order_or_char = 0
            _sub_string = 0
            _dict = deepcopy(init)
            continue

            
        already_used = _dict[char] == 0
        
        if _sub_string == len(_sources) or already_used:
            count_of_counsequence += 1
            order = -1
            _sub_string = 0
            i += 1
            _dict = deepcopy(init)
            continue
        
        order = order_or_char
        _sub_string += 1
        i += 1
    
    return count_of_counsequence + 1

def test_case_1():
    assert shortestWay("abc", "abcbc") == 2
    assert shortestWay("abc", "acdbc") == -1
    assert shortestWay("xyz", "xzyxz") == 3
    assert shortestWay("smfomnhk", "smfomnhksmfomnhksmfomnhksmfomnhksmfomnhksmfomnhksmfomnhk") == 7