from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        heap = deque([])

        for i in s:
            if i in "({[":
                heap.append(i)
            elif i == ")" and ((heap == deque([])) or (heap.pop() != "(")):
                return False
            elif i == "]" and ((heap == deque([])) or (heap.pop() != "[")):
                return False
            elif i == "}" and ((heap == deque([])) or (heap.pop() != "{")):
                return False
                
        print(heap)
        if heap == deque([]):
            return True
                