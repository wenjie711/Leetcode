/*************************************************************************
    > File Name: 292_Nim_Game.cpp
    > Author: Hat_Cloud
    > Mail: jijianfeng529@gmail.com 
    > Created Time: 2015-10-23 21:07
 ************************************************************************/

#include<iostream>
using namespace std;
class Solution {
public:
    bool canWinNim(int n) {
        // 这题简单
        // 4 s
        // 5 1 = 4 y
        // 6 2 = 4 y
        // 7 3 = 4 y
        // 8 s
        // 9 s
        if(n%4==0)
            return false;
        else
            return true;
    }
};
