# author: Gabrielle Chrysler
# this script is where the "meat" of the algorithm has been, or will be, implemented. Please refer 
# to the README for a high-level description of the algorithm.


# This is an implementation of the UPGMA (Unweighted Pair Group Method w/ Arithmetic Mean) algorithm.
import numpy


# finding the smallest value in the entire matrix. first, set the value to infinity so there are
# no numerical constraints. from there, find the min value by iterating through and searching for 
# the lowest value in the entire matrix.
def smallest_value(matrix):
        min_value = float("inf")
        row, col = 0, 0

        for i in range(len(matrix)):
                for j in range(len(matrix([i]))):
                        if table[i][j] < min_value:
                                min_value = matrix[i][j]
                                row, col = i, j
        print(row, col)                         
