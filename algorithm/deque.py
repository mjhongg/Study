from collections import deque

# 1. stack (append, pop)
'''
dq = deque('love')
print(dq)

dq.append('m')
print(dq)

print(dq.pop())
print(dq.pop())
print(dq.pop())

print(dq)
'''

# 2. queue (appendleft, pop)
'''
q = deque('love')
print(dq)

dq.appendleft('I')
print(dq)

print(dq.pop())
'''

# 3. deque 확장하기 (extend, extendleft)
'''
dq = deque('love')
print(dq)

dq.extend('you')
print(dq)

dq.extendleft('I')
print(dq)
'''

# 4. 리스트처럼 사용하기 (insert, remove)
'''
dq = deque('love')
print(dq)

dq.insert(0, 'I')
print(dq)
dq.insert(5, 'Y')
dq.insert(6, 'O')
dq.insert(7, 'U')
print(dq)

dq.remove('Y')
print(dq)
'''

# 5. deque 의 내용을 좌우로 반전 (reverse)
dq = deque('love')
dq.reverse()
print(dq)