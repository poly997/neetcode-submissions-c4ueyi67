class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #creating counts for colors
        num_counts = set(nums)
        counts = [0 for i in range(max(num_counts)+1)]
        print(counts)

        for n in nums:
            counts[n] += 1
        print(counts)
        
        i = 0
        for color in range(len(counts)):
            for j in range(counts[color]):
                nums[i] = color
                i += 1

        