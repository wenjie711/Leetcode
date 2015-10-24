/*************************************************************************
    > File Name: 77.cpp
    > Author: Hat_Cloud
    > Mail: jijianfeng529@gmail.com 
    > Created Time: 2015-10-24 22:36
 ************************************************************************/

#include<vector>
#include<iostream>
using namespace std;
class Solution {
public:
    vector<vector<int> > permute(vector<int>& nums) {
        vector<vector<int> > results;
        internal(nums, 0, results);
        return results;
    }
    void internal(vector<int>& nums,int b,vector<vector<int> >& results){
        if(b+1==nums.size()){
            results.push_back(nums);
            return;
        }
        for(int i=b;i<nums.size();i++){
            int t = nums[i];
            nums[i] = nums[b];
            nums[b] = t;
            internal(nums, b+1, results);
            t = nums[i];
            nums[i] = nums[b];
            nums[b] = t;
        }
     }
};
