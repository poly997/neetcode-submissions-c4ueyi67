#Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

'''def mergesort(arr):

    if len(arr) <= 1:
        return arr
    
    middle = len(arr) // 2
    
    first_half = mergesort(arr[:middle])
    second_half = mergesort(arr[middle:])

    # def merge()
    pointer_1, pointer_2 = 0, 0
    result = []

    while pointer_2 < len(second_half):
        while pointer_1 < len(first_half) and second_half[pointer_2] >= first_half[pointer_1]:
            result.append(first_half[pointer_1])
            pointer_1 += 1
        result.append(second_half[pointer_2])
        pointer_2 += 1  

    while pointer_1 < len(first_half):
        result.append(first_half[pointer_1])
        pointer_1 += 1

    return result'''
        

class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:

        if len(pairs) <= 1:
            return pairs
        
        middle_coordinate = len(pairs) // 2

        first_half = self.mergeSort(pairs[:middle_coordinate])
        second_half = self.mergeSort(pairs[middle_coordinate:])

        # def merge

        pointer_1, pointer_2 = 0, 0
        result = []

        while pointer_2 < len(second_half):
            while pointer_1 < len(first_half) and second_half[pointer_2].key >= first_half[pointer_1].key:
                result.append(first_half[pointer_1])
                pointer_1 += 1
            result.append(second_half[pointer_2])
            pointer_2 += 1

        while pointer_1 < len(first_half):
            result.append(first_half[pointer_1])
            pointer_1 += 1

        return result

