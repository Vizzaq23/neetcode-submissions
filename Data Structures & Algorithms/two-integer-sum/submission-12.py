class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

      seen_map= {} 
        
      for i, num in enumerate(nums):
        current = target - num 
          

        if current in seen_map:
          return [seen_map[current], i]

        seen_map[num] = i 

     


            
        