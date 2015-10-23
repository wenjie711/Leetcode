/*************************************************************************
    > File Name: 263.cpp
    > Author: Hat_Cloud
    > Mail: jijianfeng529@gmail.com 
    > Created Time: 2015-10-23 22:27
 ************************************************************************/

#include<iostream>
using namespace std;
class Solution {
public:
    bool isUgly(int num) {
        if(num<=0)
            return false;
        if(num == 1)
            return true;
        return isUglyInternal(num);
    }
    bool isUglyInternal(int num){
        if(num == 2 || num == 3 || num == 5)
            return true;
        if(num % 2 == 0)
            return isUglyInternal(num/2);
        if(num % 3 == 0)
            return isUglyInternal(num/3);
        if(num % 5 == 0)
            return isUglyInternal(num/5);
        return false;
    }
};
