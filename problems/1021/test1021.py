import p1021


def test(N, M, a, expected):
    result = p1021.solve(N, M, a)
    assert result == expected, "expected {}, got {}".format(expected, result)
    print("validated N={}, M={}, a={} result={}".format(N, M, a, result))


def test_1():
    N = 10
    M = 3
    a = [2, 9, 5]
    test(N, M, a, 8)


def test_2():
    N = 32
    M = 6
    a = [27, 16, 30, 11, 6, 23]
    test(N, M, a, 59)


def test_3():
    N = 10
    M = 10
    a = [1, 6, 3, 2, 7, 9, 8, 4, 10, 5]
    test(N, M, a, 14)


def test_4():
    N = 10
    M = 10
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    test(N, M, a, 0)


if __name__ == "__main__":
    test_1()
    test_2()
    test_3()
    test_4()
