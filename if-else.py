import math
import os
import random
import re
import sys

if __name__ == "__main__":
    n = int(input())
    if(n % 2) != 0:
        print("Weird")
    # elif n % 2 == 0 and n in range(2,5):
    elif n in range(1,6) and n % 2 == 0:
        print("Not Weird")
    # elif n % 2 == 0 and n in range(6,20):
    elif n in range(5,21) and n % 2 == 0:
        print("Weird")
    elif n % 2 == 0 and n > 20:
        print("Not Weird")


    
        
