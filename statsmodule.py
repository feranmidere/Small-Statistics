import numpy as np

class SimpleLinearRegression:
    def __init__(self):
        pass
       
    def fit(self, x, y): # x and y should be numpy arrays
        self.independent = x
        self.dependent = y
        
        self.Mx = np.mean(x)
        self.My = np.mean(y)

        self.SSx = sum((x-self.Mx)**2)
        self.SSy = sum((y-self.My)**2)
        self.SP = sum((x-self.Mx)*(y-self.My))

        self.a = self.SP/self.SSx
        self.b = self.My - (self.a*self.Mx)
        self.r = self.SP / np.sqrt(self.SSx * self.SSy)  # pearson product moment correlation coefficent
       
    def predict(self, x, dplaces=None): # provide rounding accuracy in decimal places, no rounding is done if not provided
        try:
            try:
                return round(self.a*x+self.b, dplaces)
            except:
                return np.around(self.a*x+self.b, dplaces)
        except:
            return self.a*x+self.b
   
    def geteq(self): # returns a string of the equation
        return 'y = {0}x + {1}'.format(self.a,self.b)
    
def pcovariance(x,y): # x and y should be numpy arrays
    Sy = sum((x-np.mean(x))*(y-np.mean(y)))
    return Sy / len(x)

def scovariance(x,y): # x and y should be numpy arrays
    Sy = sum((x-np.mean(x))*(y-np.mean(y)))
    return Sy / (len(x)-1)

def correlation(x,y): # x and y should be numpy arrays
    SSy = sum((x-np.mean(x))*(y-np.mean(y)))
    cov = SSy / len(x)
    return cov /(np.std(x)*np.std(y))

def eucdistance(x1,x2): # each value of x should be an iterable with x and y coordinates in it
    return np.sqrt((x2[0]-x1[0])**2+(x2[1]-x1[1])**2)
