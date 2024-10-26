from collections import deque


def get_fibbonaccci_number(i) -> int:
    if i < 3:
        return 1
    k = 3
    deq = deque([1, 1])
    while k <= i:
        deq.append(deq[0] + deq[1])
        deq.popleft()
        k += 1

    return deq[-1]
