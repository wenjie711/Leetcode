/*************************************************************************
    > File Name: 19.cpp
    > Author: Hat_Cloud
    > Mail: jijianfeng529@gmail.com 
    > Created Time: 2015-10-24 16:08
 ************************************************************************/

#include<iostream>
using namespace std;
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* p = head;
        ListNode* q = head;
        for(int i=0;i<n;i++){
            q = q -> next;
        }
        if(q == NULL){
            head = p -> next;
            return head;
        }
        while(q->next != NULL){
            p = p->next;
            q = q->next;
        }
        p -> next = p -> next -> next;
        return head;
    }
};
