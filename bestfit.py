import numpy as np

class SimpleLinearRegression:
    def __init__(self):
        pass
       
    def fit(self, x, y):
        self.independent = x
        self.dependent = y
        
        self.Mx = np.mean(x)
        self.My = np.mean(y)

        self.SS = sum((x-Mx)**2)
        self.SP = sum((x-Mx)*(y-My))

        self.a = SP/SS
        self.b = My - (a*Mx)
       
    def predict(self, x, dplaces=3):
        return round(a*x+b, dplaces)
