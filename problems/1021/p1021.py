# https://www.acmicpc.net/problem/1021


def input_data():
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    return N, M, a


def solve(N, M, a):
    from collections import deque

    dq = deque(range(1, N + 1))

    a = a[::-1]
    result = 0
    while len(a) > 0:
        target = a.pop()
        count = 0
        while True:
            first = dq[0]
            if first == target:
                dq.popleft()
                break
            else:
                dq.rotate(1)
                count += 1
        count = min(count, len(dq) + 1 - count)
        result += count
    return result


if __name__ == "__main__":
    N, M, a = input_data()
    result = solve(N, M, a)
    print(result)
