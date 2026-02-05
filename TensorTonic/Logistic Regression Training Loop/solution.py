import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    # Write code here
    num = len(X)
    dim = len(X[0])
    w = np.zeros(dim)
    b = 0.0
    for i in range(steps):
        p_i = _sigmoid(X@w + b)
        theta_w = (X.T @(p_i-y))/num
        theta_b = np.mean(p_i-y)
        w -= lr * theta_w
        b -= lr * theta_b
    return (w,b)
