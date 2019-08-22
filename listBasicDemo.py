# List or Stacks
# last-in, first-out

fruits = ['orange','apple','pear','banana','kiwi','apple','banana']
print('fruits=',fruits)
fruits.append('apple') # apple will be add at the end of the list
print("fruits.append('apple'), fruits=",fruits)
print("fruits.count('tangerine')",fruits.count('tangerine'))
print("fruits.count('banana')",fruits.count('banana'))
print("fruits.index('banana')",fruits.index('banana'))
print("fruits.index('banana',4)",fruits.index('banana',4))
fruits.reverse()
print('fruits.reverse() ,fruits=',fruits)
fruits.sort()
print('fruits.sort() ,fruits=',fruits)
print('fruits.pop() ',fruits.pop())
print('fruits=',fruits)

# Queues

from collections import deque

queue = deque(fruits)
queue.append("newApple")
queue.appendleft("leftApple")
print('queue=',queue)
print('list(queue), fruits=',list(queue))
print('queue.popleft()',queue.popleft())
print('queue.pop()',queue.pop())

# lambda with list
print(range(10))
print(list(range(10)))
print([x**2 for x in range(10)])
print(list(map(lambda x:x*2,[1,2,3,4,5])))
print(list(map(lambda x:x*2,range(10))))
newList = [(x,y)
           for x in range(1,4)
           for y in [3,1,4]
           if x!=y]
print(newList)

from math import pi
piList=[str(round(pi,i)) for i in range(1,16)]
print(piList)


# () - tuple
# [] - list
# {} - dictionary or set

