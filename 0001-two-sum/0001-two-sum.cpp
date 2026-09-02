class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> valueToIndex;

        for (int i = 0; i < nums.size(); ++i) {
            int currentNum = nums[i];
            int complement = target - currentNum;

            if (valueToIndex.find(complement) != valueToIndex.end()) {
                return {valueToIndex[complement], i};
            }

            valueToIndex[currentNum] = i;
        }

        return {};
    }
};