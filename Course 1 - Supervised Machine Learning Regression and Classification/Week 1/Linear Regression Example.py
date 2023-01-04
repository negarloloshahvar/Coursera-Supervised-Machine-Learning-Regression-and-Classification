# Her we will see how a linear regression model is defined in code, and we can see plots that show how well a model fits
# some data given choices of w and b. We can also try different values of w and b to see if it improves the fit to the data.

import numpy as np
import matplotlib.pyplot as plt

#x_train is the input variable (Size in 1000 square feet)
#y_train is the output variable or target (Price in 1000s dollars)
x_train = np.array([1.0, 2.0])
y_train = np.array([300.0, 500.0])
print(f'x_train = {x_train}')
print(f'y_train = {y_train}')

# m is the number of training samples
print(f'x_train shape {x_train.shape}')
# m = x_train.shape[0]
m = len(x_train)
print(f'The number of training samples is {m}')

i = 0
print(f'the x^({i}) is {x_train[i]}')
print(f'the y^({i}) is {y_train[i]}')

plt.scatter(x_train, y_train, c= 'r', marker= 'X', label= 'Actual Values')
plt.title('Housing Prices')
plt.xlabel('Size in 1000 square feet')
plt.ylabel('Price in 1000s dollars')
# plt.show()

w = 200
b = 100

print(f'(w, b) = ({w}, {b})')

def compute_model_output (x, w, b):
    m = len(x)
    f_wb = np.zeros(m)
    for i in range(m):
        f_wb[i] = x[i] * w + b
    return f_wb

tmp_f_wb = compute_model_output(x_train, w, b)
plt.plot(x_train, tmp_f_wb, label= 'Our Prediction')
plt.legend()
# plt.show()

x_i = 1.2
price_1200sqf = x_i * w + b
print(f'The price of a 1200 square feet house is {price_1200sqf} thouasand dollars.')