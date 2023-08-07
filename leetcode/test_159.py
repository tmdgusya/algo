def lengthOfLongestSubstringTwoDistinct(s: str) -> int:
    start = 0
    window = {}
    cache = 0
    _temp = ""
    result = ""
    while start < len(s):
        for i in range(start, len(s)):
            if s[i] not in window:
                cache += 1
                if cache > 2:
                    break


            frequent = window.get(s[i], 0)
            window[s[i]] = frequent + 1
            _temp += s[i]

        if len(_temp) > len(result):
            result = _temp

        start += 1
        cache = 0
        window = {}
        _temp = ""

    return len(result)


def test_159():
    assert lengthOfLongestSubstringTwoDistinct("eceba") == 3
    assert lengthOfLongestSubstringTwoDistinct("ccaabbb") == 5
