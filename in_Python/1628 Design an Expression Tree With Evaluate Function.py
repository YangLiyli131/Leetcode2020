import abc 
from abc import ABCMeta, abstractmethod 
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node:
    __metaclass__ = ABCMeta
    # define your fields here
    @abstractmethod
    def evaluate(self):
        pass

class ETreeNode(Node):
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    def evaluate(self):
        if self.val not in ['*','+','-','/']:
            return self.val
        else:
            left = self.left.evaluate()
            right = self.right.evaluate()
            return Eva.calc(left,right, self.val)

class Eva:
    apply = {
        '+': lambda a,b : a + b,
        '-': lambda a,b : a - b,
        '*': lambda a,b : a * b,
        '/': lambda a,b : a // b,
    }
    @staticmethod
    def calc(l,r,v):
        return Eva.apply[v](int(l), int(r))
        
"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix):
        """
        :type s: List[str]
        :rtype: int
        """
        st = []
        for x in postfix:
            if x.isnumeric():
                st.append(ETreeNode(x))
            else:
                a = st.pop()
                b = st.pop()
                st.append(ETreeNode(x,b,a))
        return st[0]
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
        