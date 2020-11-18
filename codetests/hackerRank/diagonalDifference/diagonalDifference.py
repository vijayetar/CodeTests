import math
import os
import random
import re
import sys

def diagonalDifference(matrix):
  sum1 = 0
  sum2 = 0
  i = 0
  j = len(matrix)-1
  for arr in matrix:
    sum1+= arr[i]
    sum2+= arr[j]
    i +=1
    j -=1
  return abs(sum1-sum2)

if __name__ == "__main__":
  print(diagonalDifference([[1,1,5],[2,5,2],[5,3,3]]))
    