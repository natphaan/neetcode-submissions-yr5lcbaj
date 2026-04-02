class DynamicArray:
    
    def __init__(self, capacity: int):

        self.capacity = capacity
        self.size = 0 # since there is nothing to populate the array just yet
        self.array = [0] * self.capacity



    def get(self, i: int) -> int:
        return self.array[i] # return the elem at index i


    def set(self, i: int, n: int) -> None:
        self.array[i] = n


    def pushback(self, n: int) -> None:

        if self.size == self.capacity:
            self.resize() # call resize func


        # this is if the size is less than capacity
        self.array[self.size] = n 
        self.size += 1
        


    def popback(self) -> int:
        # pop last elem and return the elem at the end of array
        if self.size > 0:
            self.size -= 1
        return self.array[self.size]


 

    def resize(self) -> None:
        # resize by doubling the capacity
        self.capacity = 2 * self.capacity
        # make a new array with the doubled size
        new_array = [0] * self.capacity

        # transfer old array content to new array
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array


    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity
