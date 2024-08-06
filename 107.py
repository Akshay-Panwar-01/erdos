import numpy as np
import math

def cofactor_matrix(A):
    """Compute the cofactor matrix of A with integer values rounded to the nearest integer."""
    n = A.shape[0]
    cofactors = np.zeros((n, n), dtype=np.int64)  # Ensure integer type
    for i in range(n):
        for j in range(n):
            # Minor matrix Mij
            Mij = np.delete(np.delete(A, i, axis=0), j, axis=1)
            # Cofactor calculation
            determinant = np.linalg.det(Mij)
            cofactors[i, j] = int(round((-1) ** (i + j) * determinant))
    return cofactors

def adjoint_matrix(A):
    """Compute the adjoint (adjugate) matrix of A with integer values rounded to the nearest integer."""
    return cofactor_matrix(A).T

# Define the matrix A
A = np.array([[1, 0, 0, 0, 0, 0, 0],
              [1, 1, 1, 1, 1, 1, 1],
              [1, -1, 1, -1, 1, -1, 1],
              [1, 2, 4, 8, 16, 32, 64],
              [1, -2, 4, -8, 16, -32, 64],
              [1, 5, 25, 125, 625, 3125, 15625],
              [1, -5, 25, -125, 625, -3125, 15625]], dtype=np.int64)

det_A= int(round(np.linalg.det(A)))
print(det_A)

# Compute the adjoint of A
A_adjoint = adjoint_matrix(A)
a=[]
for i in A_adjoint:
    p=[j for j in i]
    a.append(p)

# print("Matrix A:")
# print(A)
# print("\nAdjoint of A (with values rounded to nearest integer):")
# print(a)

k=np.array(a)
u=np.array([1,1,-1,1,-1,1,-1])
phi=k.dot(u)
print(phi)

x=18289152000
for i in phi:
    y=math.gcd(i,x)
    x=y
print(x)
print("Answer to the problem is ",det_A//x)
        
#2903040
#Answer to the problem is  6300
