class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums: number[], target: number): number[] {
        const numbersToIndex = new Map<number, number>();

      for ( let i = 0; i < nums.length; i++) {
        const current = nums[i];
        const needed = target - current;

        if (numbersToIndex.has(needed)){
            return [numbersToIndex.get(needed)!, i];
        }
         numbersToIndex.set(current, i);
        }
      }
    }
    
