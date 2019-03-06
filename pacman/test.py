from queue import PriorityQueue
from queue import Queue

q = Queue()
q.put((-10, {'d':1, '4':3}))
q.put((1,'tetew'))
q.put((-155, "Ramin"))
q.put((50, [1,2,4]))
q.put((-60, "Jalali"))
while not q.empty():
    print(q.get())
