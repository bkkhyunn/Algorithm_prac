import numpy as np

def indentity(x):
    return x

def step_function(x, threshold=0):
    return np.where(x <= threshold, 0, 1)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def tanh(x):
    return np.tanh(x)
    
def softmax(x):
    c = np.max(x)
    exp_x = np.exp(x - c)
    sum_exp = np.sum(exp_x)
    return exp_x / sum_exp

def relu(x):
    return np.maximum(0, x)

def relu6(x):
    return np.minimum(np.maximum(0, x), 6)

def softplus(x, beta=1):
    return 1/beta * np.log(1 + np.exp(beta * x))

def leaky_relu(x):
    return np.where(x > 0, x, x * 0.01)

def prelu(x, alpha=0.05):
    return np.where(x > 0, x, x * alpha)

def rrelu(x, lower=1/8, upper=1/3):
    alpha = np.random.uniform(low=lower, high=upper, size=x.shape)
    return np.where(x > 0, x, x * alpha)

def elu(x, alpha=1):
    return np.where(x > 0, x, alpha * (np.exp(x) - 1))

def selu(x, l=1.0507, a=1.6733):
    return np.where(x>0, l*x, l*a*(np.exp(x)-1))

def gelu(x):
    return 0.5 * x * (1 + np.tanh(np.sqrt(2 / np.pi) * (x + 0.044715 * np.power(x, 3))))

def gelu2(x):
    return x * sigmoid(1.702 * x)

def swish(x, beta=1):
    return x * sigmoid(beta * x)

def mish(x):
    return x * tanh(softplus(x))