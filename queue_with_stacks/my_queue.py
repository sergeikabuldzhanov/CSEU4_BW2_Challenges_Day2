import collections

class MyQueue(object):
    # There's no way but to use two stacks
    # I we want to pop and peek like normal, we will have to use the second stack to add new element
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # main stack representing our queue
        self.s1 = []
        # secondary stack, used to add new elements
        self.s2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        # empty the first stack into the second stack
        while len(self.s1) != 0:  
            self.s2.append(self.s1.pop())  
        
        # Push item into the first stack  
        self.s1.append(x)  
  
        # Push everything back to s1  
        while len(self.s2) != 0:  
            self.s1.append(self.s2.pop())  
             

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        # if first stack is empty  
        if len(self.s1) == 0:  
            print("Q is Empty") 
        # Return top of self.s1  
        x = self.s1[-1]  
        self.s1.pop()  
        return x 

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.s1[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not bool(len(self.s1))


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()

print(param_2)
print(param_3)
print(param_4)