import numpy as np

class MyArray:
    def __init__(self, input_list):
        self.array = np.array(input_list, dtype="i")

    def myInsert(self, x, i):
        new_array = np.empty(len(self.array) + 1, dtype="i")
        new_array[:len(self.array)] = self.array
        n = len(new_array)
        
        # Shift elements to the right
        for idx in range(n - 2, i - 1, -1):
            new_array[idx + 1] = new_array[idx]
        
        new_array[i] = x
        self.array = new_array  # Update self.array
        return self.array

    def myIndex(self, x):
        n = len(self.array)
        for idx in range(n):
            if self.array[idx] == x:
                return idx
        return -1  # If the key is not found

    def myDelete(self, i):
        n = len(self.array)
        
        # Shift elements to the left
        for idx in range(i + 1, n):
            self.array[idx - 1] = self.array[idx]
        
        self.array = self.array[:n - 1]  # Update self.array
        return self.array

    def myRemove(self, x):
        i = self.myIndex(x)  # O(n)
        if i == -1:
            print("Element not found.")
            return self.array
        
        print("Element found at position:", i)
        self.myDelete(i)  # O(n)
        return self.array
