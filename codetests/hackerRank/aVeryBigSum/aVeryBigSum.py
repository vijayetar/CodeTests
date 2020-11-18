import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    sum = 0
    for n in ar:
        sum += n
    return sum


if __name__ == '__main__':
    print(aVeryBigSum([1,2,3]))