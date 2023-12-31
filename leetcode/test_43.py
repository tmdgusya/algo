import unittest


def multiply(num1, num2):
    m, n = len(num1), len(num2)
    pos = [0] * (m + n)

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
            p1, p2 = i + j, i + j + 1
            total = mul + pos[p2]

            pos[p1] += total // 10
            pos[p2] = total % 10

    sb = []
    for p in pos:
        if not (len(sb) == 0 and p == 0):
            sb.append(str(p))

    return '0' if not sb else ''.join(sb)



def test_01():
    assert multiply("2", "3") == "6"
    pass