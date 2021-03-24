import numpy as np

class SimpleLinearRegression:
    def __init__(self):
        self.attributes = {}
       
    def fit(self, x, y): # x and y should be numpy arrays
        if type(x) != np.ndarray or type(y) != np.ndarray:
            raise ValueError('Input should be numpy ndarrays.')
    
        self.attributes['x'] = x
        self.attributes['y'] = y
        
        self.attributes['Mx'] = np.mean(x)
        self.attributes['My'] = np.mean(y)

        self.attributes['SSx'] = np.sum((x-self.attributes['Mx'])**2)
        self.attributes['SSy'] = np.sum((y-self.attributes['My'])**2)
        self.attributes['SP'] = np.sum((x-self.attributes['Mx'])*(y-self.attributes['My']))

        self.attributes['a'] = self.attributes['SP'] / self.attributes['SSx']
        self.attributes['b'] = self.attributes['My'] - (self.attributes['a']*self.attributes['Mx'])
        self.attributes['r'] = self.attributes['SP'] / np.sqrt(self.attributes['SSx'] * self.attributes['SSy'])  
        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # pearson product moment correlation coefficent
        
        return self
       
    def predict(self, x, dplaces=None): # provide rounding accuracy in decimal places, no rounding is done if not provided
        if dplaces != None:
            if type(x) != int or float:
                return round(self.attributes['a']*x+self.attributes['b'], dplaces)
            else:
                return np.around(self.attributes['a']*x+self.attributes['b'], dplaces)
        else:
            return self.attributes['a']*x+self.attributes['b']
   
    def get_eq(self): # returns a string of the equation
        print('y = {0}x + {1}'.format(self.attributes['a'],self.attributes['b']))
    
    def corr_coeff(self):
        return self.attributes['r']
    
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
