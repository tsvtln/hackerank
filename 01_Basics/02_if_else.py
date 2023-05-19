#!/bin/python3
import math, os, random, re, sys

if __name__ == '__main__':
    n = int(input().strip())

if n % 2 != 0:
    print('Weird')
elif n % 2 == 0 and 2 <= n <= 5:
    print('Not Weird')
elif n % 2 == 0 and 6 <= n <= 20:
    print('Weird')
elif n >= 20:
    print('Not Weird')
