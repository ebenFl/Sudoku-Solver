import pygame
import random
import copy
import heapq
import numpy as np
import requests, os
from bs4 import BeautifulSoup
import re

class sudoku:
    def __init__(self,grid):
        self.w = 9
        self.grid = grid
        self.squares = {1 : [], 2 : [], 3 : [],
                        4 : [], 5 : [], 6 : [],
                        7 : [], 8 : [], 9 : []}

        for i in range(self.w):
            for j in range(self.w):
                if i < 3:
                    if j < 3:
                        self.squares[1].append((i,j))
                    elif j < 6:
                        self.squares[2].append((i,j))
                    else:
                        self.squares[3].append((i,j))
                elif i < 6:
                    if j < 3:
                        self.squares[4].append((i,j))
                    elif j < 6:
                        self.squares[5].append((i,j))
                    else:
                        self.squares[6].append((i,j))
                else:
                    if j < 3:
                        self.squares[7].append((i,j))
                    elif j < 6:
                        self.squares[8].append((i,j))
                    else:
                        self.squares[9].append((i,j))

        self.locToSquare = {}

        for i in range(1,10):
            locations = self.squares[i]
            for loc in locations:
                self.locToSquare[loc] = i

    # determines if placement of a number is okay at given location
    # (a, b) returns True if so and False otherwise
    def isOkayMove(self,a,b):
        square = self.squares[self.locToSquare[(a,b)]]

        #check the squares
        v = []
        for loc in square:
            if self.grid[loc[0]][loc[1]] != 0:
                v.append(self.grid[loc[0]][loc[1]])
        if len(v) != len(set(v)):
            return False

        # checking horizontal
        v = []
        for i in range(9):
            if self.grid[a][i] != 0:
                v.append(self.grid[a][i])
        if len(v) != len(set(v)):
            return False

        # checking the verticle
        v = []
        for i in range(9):
            if self.grid[i][b] != 0:
                v.append(self.grid[i][b])
        if len(v) != len(set(v)):
            return False

        return True

    def setSquare(self,i,j,v):
        self.grid[i][j] = v

    # solve the sodoku puzzle columnwise via backtracking
    # call with a = 0 and b = 0
    def solve(self,a,b):
        if(b == 9): # made it through the entire puzzle
            return True
        if self.grid[a][b]: #location already contains number
            if (a == 8): # we need to move to next column
                if(self.solve(0,b + 1)):
                    return True
            else:
                if(self.solve(a + 1,b)):
                    return True
        else:
            for i in range(1,10):
                self.setSquare(a,b,i)
                if(self.isOkayMove(a,b)):
                    if (a == 8): # we need to move to next column
                        if(self.solve(0,b + 1)):
                            return True
                    else:
                        if(self.solve(a + 1,b)):
                            return True
            # no moves were okay so we backtrack
            self.setSquare(a,b,0)
            return False

    # validates solution of puzzle
    def validate(self):
        numSet = set([1,2,3,4,5,6,7,8,9])
        # checking rows
        for i in range(9):
            if set(self.grid[i]) != numSet:
                return False

        #checking columns
        for i in range(9):
            col = []
            for j in range(9):
                col.append(self.grid[j][i])
            if set(col) != numSet:
                return False

        # checking squares
        for i in range(1,10):
            square = self.squares[i]
            s = []
            for loc in square:
                s.append(self.grid[loc[0]][loc[1]])
            if set(s) != numSet:
                return False

        return True
