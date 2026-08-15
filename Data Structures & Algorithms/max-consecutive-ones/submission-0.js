class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    findMaxConsecutiveOnes(nums) {
        let tempMax = 0;
        let currentMax = 0;

        for (let i = 0; i < nums.length; i++) {
            if (nums[i] === 1) {
                tempMax++;
            } else {
                if (tempMax > currentMax) {
                    currentMax = tempMax; 
                }
                tempMax = 0;
            }
        }

        return currentMax > tempMax ? currentMax : tempMax;
    }
}
