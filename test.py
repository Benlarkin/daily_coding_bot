#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"

import random
import requests
from bs4 import BeautifulSoup as bs

def main():
    qstring = "Two Sum,Longest Substring Without Repeating Characters,Longest Palindromic Substring,Container With Most Water,3Sum,Remove Nth Node From End of List,Valid Parentheses,Merge Two Sorted Lists,Merge k Sorted Lists,Search in Rotated Sorted Array,Combination Sum,Rotate Image,Group Anagrams,Maximum Subarray,Spiral Matrix,Jump Game,Merge Intervals,Insert Interval,Unique Paths,Climbing Stairs,Set Matrix Zeroes,Minimum Window Substring,Word Search,Decode Ways,Validate Binary Search Tree,Same Tree,Binary Tree Level Order Traversal,Maximum Depth of Binary Tree,Construct Binary Tree from Preorder and Inorder Traversal,Best Time to Buy and Sell Stock,Binary Tree Maximum Path Sum,Valid Palindrome,Longest Consecutive Sequence,Clone Graph,Word Break,Linked List Cycle,Reorder List,Maximum Product Subarray,Find Minimum in Rotated Sorted Array,Reverse Bits,Number of 1 Bits,House Robber,Number of Islands,Reverse Linked List,Course Schedule,Implement Trie (Prefix Tree),Add and Search Word - Data structure design,Word Search II,House Robber II,Contains Duplicate,Invert Binary Tree,Kth Smallest Element in a BST,Lowest Common Ancestor of a Binary Search Tree,Product of Array Except Self,Valid Anagram,Meeting Rooms,Meeting Rooms II,Graph Valid Tree,Missing Number,Alien Dictionary,Encode and Decode Strings,Find Median from Data Stream,Serialize and Deserialize Binary Tree,Longest Increasing Subsequence,Coin Change,Number of Connected Components in an Undirected Graph,Counting Bits,Top K Frequent Elements,Sum of Two Integers,Pacific Atlantic Water Flow,Longest Repeating Character Replacement,Non-overlapping Intervals,Subtree of Another Tree,Palindromic Substrings"
    qs = qstring.split(",")
    randomq = qs[random.randint(0,73)]
    randomq = randomq.replace(' ', '-')
    url = "https://leetcode.com/problems/" + randomq
    print(url)


    # # initialise browser
    # browser = webdriver.Chrome(os.getcwd() + '/chromedriver')
    # # load page
    # browser.get('https://leetcode.com/problems/two-sum/')

    # # execute java script
    # browser.execute_script("return document.getElementsByTagName('html')[0].innerHTML")

    # # wait page to load
    # sleep(5)

    # # get selected content
    # problem_description = browser.find_element_by_class_name('question-content__JfgR')
    # print(problem_description.text)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
