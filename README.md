# Simple Linear Regression

-Only functional with bivariate data (x and y, where x is the sole feature and y is the target) and not multivariate data-
 
This is a class which can be used to calculate a least squares regression line with the dependent variable y
and independent variable x.

It can be fit with arrays x and y and then can predict a value or array of values. 

The model uses the formula y = ax + b where a is the gradient and b is the y-intercept of the regression line.

The equation used to calculate the gradient is:

a = SP<over>SS where SP is the sum of products and SS is the sum of squares in the data.

SP can be calculated by (x-x<sub>mean</sub>)<sup>2</sup> for each value of x and taking the sum of the results.

SS can be calculated by (x-x<sub>mean</sub>)(y-y<sub>mean</sub>) for each value of x and y and taking the sum of the results.

The equation used to calculate the y-intercept is:

b = y<sub>mean</sub> - bx<sub>mean</sub>

# How to use:

 The class needs to be defined, however takes no parameters upon initiation. 
 
 The fit method should be used to fit the linear regression with arrays x and y. 
 
 The predict method should be used to store predictions based on the equation of the least squares regression line.
