/*************************************************************************
    > File Name: 7.cpp
    > Author: Hat_Cloud
    > Mail: jijianfeng529@gmail.com 
    > Created Time: 2015-10-24 23:14
 ************************************************************************/

#include<iostream>
using namespace std;
class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> results;
        vector<int> nums;
        nums.resize(k);
        dfs(1, n, k, nums, nums.size(), results);
        return results;
    }
    void dfs(int i, int n, int k, vector<int>& nums, int len, vector<vector<int>>& results){ //k表示还差k个元素要组合
        while(i<=n){
            nums[len-k] = i++;
            if(k>1)
                dfs(i, n, k - 1, nums, len, results);
            else
                results.push_back(nums);
        }
    }
    
};
