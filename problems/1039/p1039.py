# https://www.acmicpc.net/problem/1072
import sys
from collections import deque


def input_data():
    for line in sys.stdin:
        n, k = map(int, line.split())
        return n, k


def solve(n, k):
    n = str(n)
    answer = -1
    dq = deque()
    dq.appendleft((str(n), 0))
    visited = dict()
    while len(dq) > 0:
        num, count = dq.pop()
        if count == k:
            answer = max(answer, int(num))
            continue

        for i in range(len(num)):
            for j in range(i + 1, len(num)):
                new_num = num[:i] + num[j] + num[i + 1 : j] + num[i] + num[j + 1 :]
                if new_num[0] != "0":
                    next_node = (new_num, count + 1)
                    if visited.get(next_node, None) is None:
                        visited[next_node] = True
                        dq.appendleft(next_node)
    return answer


if __name__ == "__main__":
    n, k = input_data()
    result = solve(n, k)
    print(result)
