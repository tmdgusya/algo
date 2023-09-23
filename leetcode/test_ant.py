def ant(n: int) -> str:
    start = "1"
    for i in range(0, n):
        start = next(start)
    return start


def next(s: str) -> str:
    length = 1
    head = s[0]
    result = ""
    for i in range(1, len(s)):
        if s[i] == head:
            length += 1
        else:
            result += str(length)
            result += head
            length = 1
            head = s[i]

    result += str(length)
    result += head
    return result

def test_1():
    print(ant(2))
    assert 1 == 1