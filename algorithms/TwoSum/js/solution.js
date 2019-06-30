// Given an array of integers, return indices of the two numbers such that they add up to a specific target
// For example:
// Given nums = [2, 7, 11, 15], target = 9,

// Because nums[0] + nums[1] = 2 + 7 = 9,
// return [0, 1].

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    var findNum;
    var arrTemp = [];

    var firstIdx;

    for(i=0; i < nums.length; i++) {
        firstIdx = i;

        findNum = target - nums[i];
        arrTemp = nums.slice(i+1);

        findIdx = arrTemp.findIndex((element) => {
            return (element-findNum) == 0
        });

        if ( findIdx !== -1) {
            findIdx += firstIdx;
            break;
        }
    }

    return [firstIdx, findIdx+1];
};

console.log(twoSum([2, 7, 11, 15], 9));
