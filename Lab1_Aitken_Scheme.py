import math
import numpy as np
import random

q_of_x = int(input("Input number of X values: "))
X = random.sample(range(-10,10), q_of_x)
Y = []
for i in range(len(X)):
    Y.append(math.pow(math.e, 7*X[i]**2 + 1))
print(X)
print(Y)
x0 = float(input("Input x0: "))

ans_list = []
def aitken_scheme(X, Y, j):
    aitken = []
    for i in range(len(Y)-1):
        first = np.array([[x0 - X[i], Y[i]],
                          [x0 - X[i + 1 + j], Y[i + 1]]])
        aitken.append(round(np.linalg.det(first) / (X[i + 1 + j] - X[i]), 3))
    ans_list.append(aitken[0])
    print(aitken)
    if len(X) <= 2 or len(aitken) == 1:
        return aitken[0]
    else:
        return aitken_scheme(X, aitken, j+1)

aitken_scheme(X,Y,0)
if len(X) > 2:
    for i in range(len(ans_list)):
        if abs(ans_list[i+1] - ans_list[i]) <= abs(ans_list[i+2] - ans_list[i+1]):
            print("Aitken Scheme answer: ", ans_list[i+1])
            break
else:
    print("Aitken Scheme answer: ", ans_list[0])
print("Python function answer: ", math.pow(math.e, 7*x0**2 + 1))
