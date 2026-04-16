def fib(n):
    # 기저 조건 1: n == 0이면 0 반환
    if n == 0:
        return 0
    # 기저 조건 2: n == 1이면 1 반환
    if n == 1:
        return 1
    # 재귀 호출: fib(n-1) + fib(n-2)
    return fib(n-1) + fib(n-2)

n = int(input())
print(fib(n))