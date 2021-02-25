import numpy as np

class SimpleLinearRegression:
    def __init__(self):
        pass
       
    def fit(self, x, y):
        self.independent = x
        self.dependent = y
        
        self.Mx = np.mean(x)
        self.My = np.mean(y)

        self.SSx = sum((x-self.Mx)**2)
        self.SSy = sum((y-self.My)**2)
        self.SP = sum((x-self.Mx)*(y-self.My))

        self.a = self.SP/self.SSx
        self.b = self.My - (self.a*self.Mx)
        self.r = self.SP / np.sqrt(self.SSx * self.SSy) 
       
    def predict(self, x, dplaces=3):
        try:
            return round(self.a*x+self.b, dplaces)
        except:
            return np.around(self.a*x+self.b, dplaces)
   
    def geteq(self):
        return 'y = {0}x + {1}'.format(self.a,self.b)
