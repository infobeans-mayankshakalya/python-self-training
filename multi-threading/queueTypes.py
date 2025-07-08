import queue

q = queue.Queue()
q.put(50)
q.put(500)
q.put(100)
q.put(200)

while not q.empty():
    print(q.get(), end=' ')

print()

lq = queue.LifoQueue()
lq.put(50)
lq.put(500)
lq.put(100)
lq.put(200)

while not lq.empty():
    print(lq.get(), end=' ')

print()

pq = queue.PriorityQueue()
pq.put(50)
pq.put(500)
pq.put(100)
pq.put(200)

while not pq.empty():
    print(pq.get(), end=' ')