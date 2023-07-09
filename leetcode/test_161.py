def isOneEditDistance(s: str, t: str) -> bool:
    if s == t:
        return False

    t_len = len(t)
    s_len = len(s)
    if s_len == 0 and t_len == 0:
        return False

    _s = list(s)
    _t = list(t)
    is_operated = False

    if s_len > t_len:
        _t.append("")
    
    if t_len > s_len:
        _s.append("")
    
    for i in range(max(t_len, s_len)):
        if is_operated:
            continue
        
        if s_len > t_len and _s[i] != _t[i]:
            _s.pop(i)
            is_operated = True
            _t.remove('')
            continue
        
        if s_len < t_len and _s[i] != t[i]:
            _s = _s[0:i] + [t[i]] + _s[i:len(_s)]
            is_operated = True
            _s.remove('')
            continue
        
        if s_len == t_len and _s[i] != t[i]:
            _s[i] = t[i]
            is_operated = True
            continue

    return _s == _t


def test_161_case_1():
    assert isOneEditDistance("ab", "acb") == True