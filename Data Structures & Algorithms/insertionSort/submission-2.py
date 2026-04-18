# Definition for a pair.
class Pair:
     def __init__(self, key: int, value: str):
         self.key = key
         self.value = value

# a bit more elegant solution

class Solution:

    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:

        sorted_list = [] # To stare snapshots of the pairs
        ln = len(pairs)

        for i in range(ln):
            j = i - 1
            while j >= 0 and pairs[j].key > pairs[j + 1].key:
                pairs[j], pairs[j + 1] = pairs[j + 1], pairs[j]
                j  -= 1
            sorted_list.append(pairs[:])

        return sorted_list


# more fussy solution
'''class Solution: 
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        
        sorted_list = []
        #sorted_list.append(pairs.copy())

        curr_list = 0
        i = -1
        j = 0

        while curr_list < len(pairs):
            while i >= 0:
                #print(pairs[j].value, pairs[i].value)
                if pairs[j].key < pairs[i].key:
                    pairs[i], pairs[j] = pairs[j], pairs[i]
                    j -= 1
                    i -= 1
                else: 
                    break
            curr_list += 1
            j = curr_list
            i = j - 1
            sorted_list.append(pairs.copy())

        return sorted_list'''



