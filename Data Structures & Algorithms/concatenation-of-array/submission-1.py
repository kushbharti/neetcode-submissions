class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = (len(nums)*2) + 1
        arr=[]
        counter = 0 
        for i in range(length):
            if len(nums) > i:
                arr.append(nums[i])
            if len(nums) < i:
                arr.append(nums[counter])
                counter += 1
            
        return arr