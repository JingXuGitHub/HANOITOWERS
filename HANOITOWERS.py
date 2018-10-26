# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 11:24:24 2018

@author: Jing
"""

moves = 0
def HANOITOWERS(n, fromPeg, toPeg):        
    if n == 1:
        global moves
        moves = moves + 1
        print("Move disk from peg ", fromPeg, " to peg ", toPeg)
        return
    unusedPeg = 6 - fromPeg - toPeg
    HANOITOWERS(n - 1, fromPeg, unusedPeg)
    print("Move disk from peg ", fromPeg, " to peg ", toPeg)
    moves = moves + 1
    HANOITOWERS(n - 1, unusedPeg, toPeg, )
    return
    
def Main():
    HANOITOWERS(3, 1, 3)
    print("It needs %d steps" % moves)
    
Main()