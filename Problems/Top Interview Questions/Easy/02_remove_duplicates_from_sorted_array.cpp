// https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size() <= 1) {
            return nums.size();
        }
        int k = 0;
        for (int i = 1; i < nums.size(); ++i) {
            if (nums[k] != nums[i]) {
                nums[++k] = nums[i];
            }
        }
        return ++k;
    }
};
