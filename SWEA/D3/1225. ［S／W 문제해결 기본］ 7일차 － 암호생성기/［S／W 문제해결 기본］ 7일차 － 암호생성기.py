#import sys
#sys.stdin = open("input.txt", "r")
from collections import deque

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    tc_num = int(input())
    nums = list(map(int, input().split()))
                
    dq = deque(nums)
    cycle = [1, 2, 3, 4, 5]
    step = 0
                
    while True:
        value = dq.popleft()
        subtract = cycle[step % 5]
        value -= subtract
        step +=1 
                
        if value <=0:
                dq.append(0)
                break
        else:
                dq.append(value)
                
    print(f'#{tc}', *dq)      