class Solution {
    /**
     * @param {number[]}
     * @return {boolean}
     */
    hasDuplicate(nums: number[]): boolean {
        const seen = new Set();

        for(const num of nums){
            if(seen.has(num)) {
                return true
            }
            seen.add(num)
        }
       return false
    }

}