# https://www.acmicpc.net/problem/1072
import sys


def input_data():
    for line in sys.stdin:
        x, y = map(int, line.split())
        yield x, y


def solve(x, y):
    win_rate = y * 100 // x
    if win_rate >= 99:
        return -1

    left = 0
    right = 1000000001
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        new_win_rate = (y + mid) * 100 // (x + mid)
        if new_win_rate > win_rate:
            right = mid - 1
            answer = mid
        else:
            left = mid + 1
    # print(left, right, answer)
    return answer


if __name__ == "__main__":
    for x, y in input_data():
        result = solve(x, y)
        print(result)
