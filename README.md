# UPGMA

UPGMA (Unweighted Pair Group Method w/ Artithmetic Mean), is a heuristic algorithm that iteratively joins the two nearest clusters until one cluster is left.

INITIAL THOUGHTS FOR ALGORITHM IMPLEMENTATION:
- First, generate a matrix of size nxm, where this may be randomly generated or generated by user input (tbd). Also, it is likely that these will be numerically labeled from (1-x) since there are only 26 letters in the alphabet.
- Start with the first row of the matrix and find the shortest distance's row and column. From there, truncate the matrix to delete the row and column that the shortest distance is found in.
- Store the distance and half it between the two points (prob output this in a file) (also, recursion is probably the best way to implement this?)
