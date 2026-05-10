import heapq

for tc in range(1 ,11):
    dump = int(input())
    boxes = list(map(int, input().split()))
    
    min_heap = boxes[:]
    max_heap = [-b for b in boxes] 
    heapq.heapify(min_heap)
    heapq.heapify(max_heap)
    
    for _ in range(dump):
        max_val = - max_heap[0]
        min_val = min_heap[0]
        
        if max_val - min_val <= 1:
            break 
         
        heapq.heappop(max_heap)
        heapq.heappop(min_heap)
        
        new_max = max_val - 1
        new_min = min_val + 1
        
        heapq.heappush(max_heap, - new_max)
        heapq.heappush(min_heap, new_max)
        heapq.heappush(max_heap, -new_min)
        heapq.heappush(min_heap, new_min)
        
    print(f"#{tc} {-max_heap[0] -min_heap[0]}")