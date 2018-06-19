<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


- [Leetcode](#leetcode)
  - [1 Two Sum](#1-two-sum)
  - [19 Remove Nth Node From End of List](#19-remove-nth-node-from-end-of-list)
  - [26 Remove Duplicates from Sorted Array](#26-remove-duplicates-from-sorted-array)
  - [46 Permutations](#46-permutations)
  - [77 Combinations](#77-combinations)
  - [144 Binary Tree Preorder Traversal](#144-binary-tree-preorder-traversal)
  - [145 Binary Tree Postorder Traversal](#145-binary-tree-postorder-traversal)
  - [263 Ugly Number(丑数)](#263-ugly-number%E4%B8%91%E6%95%B0)
  - [292 Nim Game](#292-nim-game)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Leetcode

## 1 Two Sum

**标签**
- `Array`
- `HashTable`

**解题思路1**
- 先排序这个数组
- 两个指针
    - 一个从左边
    - 一个从右边
- 两个指针所指的的元素相加的和s和target比较
    - 如果s比target大，移动右指针
    - 如果s比target小，移动左指针
    - 如果相等就找到了
- 如果题目要求返回元素在原数组中的索引，一开始用一个map记录下，元素和索引信息就可以了。
    － 或者再遍历下原数组，找到它们的索引。


## 19 Remove Nth Node From End of List

**标签**
- `Linked List`
- `Two Pointers`

**解题思路1**
- 两个指针
    - p，q一开始都指向head
    - 为了让p和q之间包含n-2个元素
    - 但为了删除掉倒n个元素，让p和q之间相差n-1个元素
    - 即q先走，q先走n步。
- 接着q一直迭代，直到q的下个next是NULL，这时q为最后一个元素
- 此时的p为倒n个元素的上一个元素。
- 然后就是标准的链表删除元素操作
- 要注意的是q一开始先走的时候，如果q走到了NULL，说明题目要删的是链表的第一个元素，这时候要特殊处理下


## 20 Valid Parentheses

**标签**
- `String`
- `Stack`

**解题思路1**
- 用栈来解决，这题就不说了，很简单。


## 26 Remove Duplicates from Sorted Array

**标签**
- `Array`
- `Two Pointers`

**解题思路1**
- 两个指针
    - p指向当前发现的不重复数组的最后一个元素
    - q指向当前迭代的元素进度
- 如果不一样
- 就p指向下一个位置
- 用新发现的替换，就算这时候p和q指向的一样，也没问题
   

## 46 Permutations

**标签**
- `Backtracking(dfs)`

**解题思路1**
- 这题标签是回溯，就是用递归可以将大问题分成子问题
- 把数组看成第一个元素，和剩下的数组
- 每次确定第一个元素，以这个第一个元素开始的数组的全排列，可以看出是剩下数组全排列的所有的可能再在头部加上这个元素
- 每次让第一个元素和剩下的元素一一交换，再求剩下数组元素的全排列
- 求剩下元素的全排列是个类似的子问题。
-            根节点
-       1       2       3
-     2   3   1   3   1   2     
-     3   2   2   1   2   3   
     

## 77 Combinations

**标签**
- `Backtracking1

**解题思路1**
- 这题标签是回溯，就是用递归可以将大问题分成子问题
- 与46题全排列类似

## 144 Binary Tree Preorder Traversal

**标签**
- `Tree`
- `Stack`

**解题思路**
- 用一个栈，从根开始先入栈
- 然后循环判读栈是否为空
- 不为空，出栈，判断其右节点是否为空，不为空就入栈，然后就是左节点


## 145 Binary Tree Postorder Traversal 

**标签**
- `Tree`
- `Stack`

**解题思路**
- 用一个栈和一个Set
- 也时从根开始，先放入栈和Set
- Set用于判断元素的左右子节点是否被处理过，如果没有就在Set中，如果有就移除Set，但是此时可能还还没出栈。
- 也是循环判断栈是否为空
- 不为空出栈，先判断是否在Set中，
    - 如果不在说明其左右节点已经处理过了，这时候就出栈，加入结果集
    - 如果在Set中，就处理下其左右子节点，也是放入栈和Set中，处理完的时候记得从Set中移除


## 263 Ugly Number(丑数)

**标签**
- 暂无

**解题思路**
- 这题比较简单，只要不是4的倍数就可以赢


## 292 Nim Game 

**标签**
- `Math`

**解题思路**
- 这题比较简单，在没看剑指offer前。
- 我的做法是用递归，分别用2，3，5除，除的尽的话递归调用，如果为1，就返回true
