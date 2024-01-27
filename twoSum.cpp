class Solution 
{
public:
    vector<int> twoSum(vector<int>& nums, int target) 
    {

        map<int,int> result_map;
        for(int i=0;i<nums.size();i++)
        {
            int search_value = target - nums[i];
            if(result_map.find(search_value) != result_map.end())
            {
                return {result_map[search_value],i};
            }
            result_map[nums[i]] = i;
        }
        return {0,0};
    }
};
