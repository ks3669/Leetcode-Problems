'''
The time complexity would be O(n)
Also the space complexity would be O(1) because we are storing only 2 entries in the hashmap no matter how much the length of the nums is like
'''



class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        result_dict = {0:-1}
        result = 0
        running_sum = 0
        for i in range (len(nums)):
            if nums[i] == 0:
                running_sum -= 1
            else:
                running_sum += 1
            if running_sum in result_dict:
                result = max(i - result_dict.get(running_sum), result)
            else:
                result_dict[running_sum] = i
        return result
