<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


- [Leetcode](#leetcode)
  - [1 Two Sum](#1-two-sum)
  - [144 Binary Tree Preorder Traversal](#144-binary-tree-preorder-traversal)
  - [145 Binary Tree Postorder Traversal](#145-binary-tree-postorder-traversal)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Leetcode

## 1 Two Sum

**标签**
- Array
- HashTable

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


## 144 Binary Tree Preorder Traversal

**标签**
- Tree 
- Stack

**解题思路**
- 用一个栈，从根开始先入栈
- 然后循环判读栈是否为空
- 不为空，出栈，判断其右节点是否为空，不为空就入栈，然后就是左节点


## 145 Binary Tree Postorder Traversal 

**标签**
- Tree 
- Stack

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
- Math

**解题思路**
- 这题比较简单，在没看剑指offer前。
- 我的做法是用递归，分别用2，3，5除，除的尽的话递归调用，如果为1，就返回true
