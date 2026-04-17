def hanoi(n, start, end, via):
    # 기저 조건: n == 1이면 print(start, end) 후 return
    if n == 1:
        print(start, end)
        return 0
    # 1) N-1개를 start -> via로 (재귀)
    hanoi(n-1, start, via, end)
    # print(start,via)
    # 2) 가장 큰 원판을 start -> end로 (출력)
    hanoi(1, start, end, via)
    # print(start,end)
    # 3) N-1개를 via -> end로 (재귀)
    hanoi(n-1, via, end, start)
    # print(via,end)

n = int(input())
print(2**n - 1)    # 이동 횟수 먼저 출력
hanoi(n, 1, 3, 2)