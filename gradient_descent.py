### 💻 Problem: Gradient Descent for Simple Linear Regression (Find Intercept `c`)

""" 
You are given 4 data points for a simple linear regression problem of the form:

y = mx + c

You need to **find the optimal value of `c` (intercept)** using **gradient descent**, while keeping the slope `m` fixed.
"""
import numpy as np

# LOSS
def compute_sse_loss(x: np.ndarray, y: np.ndarray, m: float, c: float) -> float:
    """
    Compute the Sum of Squared Error (SSE) loss for y = mx + c
    """
    y_pred = m * x + c
    loss = np.sum((y - y_pred) ** 2)
    return loss

#### 🧮 Data Provided:
x = np.array([1, 2, 3, 4])
y = np.array([3, 5, 7, 9])
m = 2

### SOLUTION
def gradient_descent_find_c(x, y, m, lr=0.01, iterations=1000) -> float:
    c = 0
    ### Your solution here
    return c


result = gradient_descent_find_c(x=x, y=y, m=m, lr=0.01, iterations=1000)
print(result)
