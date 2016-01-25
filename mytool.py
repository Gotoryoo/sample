Enter file contents here
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 14:59:47 2015

@author: ryousuke
"""
import cv2

def funcDouble(x):    
    return 2*x


def funcTriple(x):    
    return 3*x


def funcPower(x):
    return x*x

def funcGaussian(img,kernel):#
    gau_1 = cv2.GaussianBlur(img , (3,3),-1)
    gau_2 = cv2.GaussianBlur(gau_1 , (kernel,kernel),-1)
    sub = cv2.subtract(gau_2 ,gau_1)
    return sub


def funcThreshold(img,kernel,threshold): 
    thre = cv2.threshold(funcGaussian(img,kernel), threshold , 255, cv2.THRESH_BINARY);
    return thre


def funcCountNonZero(img,kernel,threshold):
    count = cv2.countNonZero(funcThreshold(img,kernel,threshold));
    return count




if __name__ == '__main__':

    
    print "testcode for funcDouble"        
    assert funcDouble(0) == 0
    assert funcDouble(-5) == -10
    assert funcDouble(3.0) == 6.0
    assert funcDouble(200.0) == 400.0    
    print "test OK"

    
    print "testcode for funcTriple"        
    assert funcTriple(0) == 0
    assert funcTriple(-5) == -15
    assert funcTriple(3.0) == 9.0
    assert funcTriple(200.0) == 600.0    
    print "test OK"
    
    
    print "testcode for funcPower"        
    assert funcPower(0) == 0
    assert funcPower(-5) == 25
    assert funcPower(3.0) == 9.0
    assert funcPower(20.0) == 400.0    
    print "test OK"
    
