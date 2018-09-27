# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 06:02:30 2007

@author: student
"""

def binarysearch(alist,item):
    print("binary tree takes sorted array as input")
    print("sorted array is")
    alist.sort()
    print(alist)
    first =0
    last =len(alist)-1
    found =false
    print("first element="+str(alist[first]))
    pirnt("last element ="+str(alist[last]))
    print("searching")
    while first<=last and not found:
        midpoint=(first+last)//2
        print("mid element ="+str(alist[mid point]))
        if alist[mid point]==item:
            found=true
        else:
            if item<alist[mid point]:
                last=mid point-1
            else:
                first=mid point
                