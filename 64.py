import sympy
import math
import numpy as np 

def find_inverse(matrix):
    try:
        inverse_matrix = np.linalg.inv(matrix)
        return inverse_matrix
    except np.linalg.LinAlgError:
        print("Matrix is singular and cannot be inverted.")
        return None
    
def matrix_multiply(matrix1, matrix2):
    try:
        result_matrix = np.dot(matrix1, matrix2)
        return result_matrix
    except ValueError:
        print("Invalid dimensions for matrix multiplication.")
        return None

Unsolved=True
i=3
while Unsolved:
    print(i)
    x=[[]]*(i+1)
    for j in range(i+1):
        x[j]=[j**k for k in range(i+1)]
    y=[2,1,0]*(i//3)+[2]

    a=find_inverse(x)
    if a is not None:
        ans=matrix_multiply(a,y)
        if ans is not None:
            myans=0
            for s in range(i+1):
                myans+=ans[s]*((i+1)**s)
            if myans>7000:
                Unsolved=False
            print(myans,i)
            i+=3
        else:
            i+=3
            continue
    else:
        i+=3

'''Answer is coming up for polynomial of 15th degree it means m=5'''
