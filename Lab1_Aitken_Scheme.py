import math
import numpy as np

def fun(x):
    func = math.exp(7*x**2 + 1)
    return func

global ans_list
ans_list = []
def aitken_scheme(X, Y, j):
    aitken = []
    for i in range(len(Y)-1):
        first = np.array([[x0 - X[i], Y[i]],
                          [x0 - X[i + 1 + j], Y[i + 1]]])
        aitken.append(np.linalg.det(first) / (X[i + 1 + j] - X[i]))
    ans_list.append(aitken[0])
    print(aitken)
    if len(X) <= 2 or len(aitken) == 1:
        return aitken[0]
    else:
        return aitken_scheme(X, aitken, j+1)

q_of_x = int(input("Input number of X values: "))
X = np.linspace(-0.5,0.5, q_of_x)
Y = [fun(i) for i in X]
print(X)
print(Y)
x0 = float(input("Input x0: "))
epsilon = float(input("Input required accuracy (epsilon): "))

aitken_scheme(X,Y,0)
#print(ans_list)
if len(X) > 2:
    for i in range(len(ans_list)):
        try:
            if abs(abs(ans_list[i+1] - ans_list[i]) - abs(ans_list[i+2] - ans_list[i+1])) < epsilon:
                print("Aitken Scheme answer: ", ans_list[i+1])
                break
        except IndexError:
            print("There is no approcimate answer for this list. Try again.")

else:
    print("Aitken Scheme answer: ", ans_list[0])
print("Python function answer: ", math.pow(math.e, 7*x0**2 + 1))
print("R(x) = ", abs(math.pow(math.e, 7*x0**2 + 1) - ans_list[i+1]))
