# Week 1: Introduction to Machine Learning

For linear regression, the model is represented by 𝑓𝑤,𝑏(𝑥)=𝑤𝑥 + 𝑏 	 or 𝑓(𝑥)=𝑤𝑥 + 𝑏.
NumPy arrays have an attribute called ```shape``` that returns a tuple with each index having the number of corresponding elements.


General
- Notation	Description	Python (if applicable)
- 𝑎 	scalar, non bold	
- 𝐚 	vector, bold	

Regression		
- 𝐱 	Training Example feature values (in this lab - Size (1000 sqft))	x_train
- 𝐲 	Training Example targets (in this lab Price (1000s of dollars))	y_train
- 𝑥(𝑖) ,  𝑦(𝑖) 	 𝑖𝑡ℎ Training Example	x_i, y_i
- m	Number of training examples	m
- 𝑤 	parameter: weight	w
- 𝑏 	parameter: bias	b
- 𝑓𝑤,𝑏(𝑥(𝑖)) 	The result of the model evaluation at  𝑥(𝑖)  parameterized by  𝑤,𝑏 :  𝑓𝑤,𝑏(𝑥(𝑖))=𝑤𝑥(𝑖)+𝑏 	f_wb
