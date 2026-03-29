class DynamicArray:
    
    def __init__(self, capacity: int):
        
        self.capacity = capacity
        self.length = 0
        self.arr = [0] * self.capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.capacity == self.length:
            self.resize()
        
        self.arr[self.length] = n
        self.length += 1


    def popback(self) -> int:

        p = self.arr[self.length - 1]
        self.arr[self.length - 1] = 0
        self.length = self.length - 1

        return p
 

    def resize(self) -> None:
        self.capacity = self.capacity * 2
        new_arr = [0] * self.capacity

        # Copy old elements

        for index in range(0, self.length):
            new_arr[index] = self.arr[index]
        self.arr = new_arr


    def getSize(self) -> int:
        return self.length
        
    
    def getCapacity(self) -> int:
        return self.capacity
