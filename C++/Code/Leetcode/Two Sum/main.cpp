/*
https://leetcode.com/problems/two-sum/
*/

#include <easy_include.hpp>


class Solution {
    public:
        std::vector<int> twoSum(std::vector<int>& nums, int target) {
            std::unordered_map<int, int> map;

            for(int i = 0; i < nums.size(); i++) {
                int search_for = target - nums[i];
                if(map.find(search_for) != map.end()) {
                    return std::vector<int> {map[search_for], i};
                }
                map[nums[i]] = i;
            }

            return std::vector<int> {};
        }
};


int main() {
    const int target = 12;
    std::vector<int> nums = {5, 10, 15, 20, 4, 6, 7};

    Solution solution;
    std::vector<int> solution_return = solution.twoSum(nums, target);
    for(int i = 0; i < solution_return.size(); i++) {
        std::cout << solution_return[i] << ' ';
    }
    std::cout << std::endl;

    return 0;
}
