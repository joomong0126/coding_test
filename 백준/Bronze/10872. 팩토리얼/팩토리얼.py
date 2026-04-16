def factorial(n):
    # 기저 조건을 작성하세요 (n == 0이면 1 반환)
    if n == 0:
        return 1
    # 재귀 호출을 작성하세요 (n * factorial(n-1))
    return n * factorial(n-1)

n = int(input())
print(factorial(n))