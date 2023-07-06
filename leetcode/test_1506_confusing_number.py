def confusingNumber(n: int) -> bool:
    map = rotatedNumber()
    str_int = str(n)
    rotated = ""
    
    for i in range(len(str_int) - 1, -1, -1):
        if map[str_int[i]] == -1:
            return False
        rotated += str(map[str_int[i]])
    
    if trim(rotated) == trim(str_int):
        return False

    return True

def trim(int_str: str) -> str:
    trimed = ""
    for char in int_str:
        if len(trimed) == 0 and char == '0':
            continue
        trimed += char
    return trimed

def rotatedNumber():
    """
    -1 means that is invalid number
    """
    map = {}
    map['0'] = 0
    map['1'] = 1
    map['2'] = -1
    map['3'] = -1
    map['4'] = -1
    map['5'] = -1
    map['6'] = 9
    map['7'] = -1
    map['8'] = 8
    map['9'] = 6
    return map

def test_case_1():
    assert confusingNumber(6) == True

def test_case_2():
    assert confusingNumber(89) == True