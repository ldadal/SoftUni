from collections import deque

break_count = 0
quantity_of_food = int(input())
order_queue = deque(int(x) for x in input().split())
print(max(order_queue))
while order_queue and order_queue[0] <= quantity_of_food:
    quantity_of_food -= order_queue.popleft()
if order_queue:
    print("Orders left:", *order_queue)
else:
    print("Orders complete")
