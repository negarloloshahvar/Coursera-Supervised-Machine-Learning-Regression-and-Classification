# Week 1: Introduction to Machine Learning

## Chapter Objectives

- Define machine learning
- Define supervised learning
- Define unsupervised learning
- Write and run Python code in Jupyter Notebooks
- Define a regression model
- Implement and visualize a cost function
- Implement gradient descent
- Optimize a regression model using gradient descent

For linear regression, the model is represented by 𝑓𝑤,𝑏(𝑥)=𝑤𝑥 + 𝑏 	 or 𝑓(𝑥)=𝑤𝑥 + 𝑏.
NumPy arrays have an attribute called ```shape``` that returns a tuple with each index having the number of corresponding elements.

## Notations

### General
| Notation| Description	Python (if applicable) |
| ---------| -----------------------------------|
| 𝑎 | scalar, non bold	|
| 𝐚 |	vector, bold	|

### Regression		
- 𝐱 	Training Example feature values (in this lab - Size (1000 sqft))	x_train
- 𝐲 	Training Example targets (in this lab Price (1000s of dollars))	y_train
- 𝑥(𝑖) ,  𝑦(𝑖) 	 𝑖𝑡ℎ Training Example	x_i, y_i
- m	Number of training examples	m
- 𝑤 	parameter: weight	w
- 𝑏 	parameter: bias	b
- 𝑓𝑤,𝑏(𝑥(𝑖)) 	The result of the model evaluation at  𝑥(𝑖)  parameterized by  𝑤,𝑏 :  𝑓𝑤,𝑏(𝑥(𝑖))=𝑤𝑥(𝑖)+𝑏 	f_wb

## Cost Function

The cost function will tell us how well the model is doing so that we can try to get it to do better.

![image](https://user-images.githubusercontent.com/113103161/209154964-69601815-e54e-4887-a0f8-da489a85296f.png)

w and b are parameters of the model, adjusted as the model learns from the data. They’re also referred to as “coefficients” or “weights”

## Gradient Descent
Gradient descent is an algorithm for finding values of parameters w and b that minimize the cost function J.

![image](https://user-images.githubusercontent.com/113103161/209239755-88f25ad6-c6b1-4685-9c06-dc5640ea08a6.png)

