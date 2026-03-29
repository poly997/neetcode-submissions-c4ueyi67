# two stacks solution

class MinStack:

    def __init__(self):
        
        self.stack_main = [] 
        self.stack_min = [] 

    def push(self, val: int) -> None:

        self.stack_main.append(val)

        if self.stack_min:
            if self.stack_min[-1] > val:
                self.stack_min.append(val)
            else:
                self.stack_min.append(self.stack_min[-1])

        else:
            self.stack_min.append(val)
        

    def pop(self) -> None:

        if self.stack_main:
            self.stack_main.pop()
            self.stack_min.pop()

    def top(self) -> int:

        if self.stack_main:
            return self.stack_main[-1]

    def getMin(self) -> int:

        if self.stack_main:
            return self.stack_min[-1]
        
