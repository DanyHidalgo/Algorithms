'''
Calculate the sum of the rest of the first N natural number, 
using recursion
'''
import sys
sys.setrecursionlimit(2000)


def sum_of_n(n_param):


    n = n_param


    if n == 1: #Base case

        return 1

    else: #Return case

        return n + sum_of_n(n - 1)

