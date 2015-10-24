/*************************************************************************
    > File Name: 26.cpp
    > Author: Hat_Cloud
    > Mail: jijianfeng529@gmail.com 
    > Created Time: 2015-10-24 11:54
 ************************************************************************/

#include<iostream>
using namespace std;
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int len = nums.size();
        if(len==0)
            return 0;
        if(len==1)
            return 1;
        int p; //p指向当前发现的不重复数组的最后一个元素
        int q; //q指向当前迭代的元素进度
        for(p = 0, q = 1;q < len;++q){ 
            if(nums[p]!=nums[q]){ //如果不一样
                ++p;    //就p指向下一个位置
                nums[p] = nums[q];  //用新发现的替换，就算这时候p和q指向的一样，也没问题
            }
        }
        return p+1;
    }
};
