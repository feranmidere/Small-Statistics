# Simple-Linear-Regression
 
This is a function which can be used to display the equation of a least squares regression line with the dependent variable y
and independent variable x.

It takes numpy arrays for x and y and outputs the regression line equation. 

The function uses the formula y = ax + b where a is the gradient and b is the y-intercept of the regression line.

The equation used to calculate the gradient is:

a = SP<over>SS where SP is the sum of products and SS is the sum of squares in the data.

SP can be calculated by (x-x<sub>mean</sub>)$n^2$ for each value of x and taking the sum of the results.

SS can be calculated by (x-x<sub>mean</sub>)(y-y<sub>mean</sub>) for each value of x and y and taking the sum of the results.

The equation used to calculate the y-intercept is:

b = y<sub>mean</sub> - bx<sub>mean</sub>