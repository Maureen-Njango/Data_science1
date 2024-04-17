from collections import deque
m=deque()
m.append(3)
m.append(6)
m.append(7)
print(m)



from queue import Queue
x = Queue(maxsize=4)
print(x.qsize())
x.put("morin")
x.put("Njango")
x.put("mbira")

print(x.full())


print(x.get())
print(x.get())
print(x.get())
print(x.empty())
print(x.full())
