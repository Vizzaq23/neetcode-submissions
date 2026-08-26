class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      seen_map = {} 

      for i , n in enumerate(nums):
        current = target - n 

        if current in seen_map: 
          return [seen_map[current], i]
        seen_map[n] = i
        