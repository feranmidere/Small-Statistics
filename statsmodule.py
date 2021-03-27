import numpy as np
import pandas as pd

class SimpleLinearRegression:
    def __init__(self):
        self.attributes = {}

    def fit(self, x, y): # x and y should be numpy arrays, 1D dataframes, series or lists
        if type(x) not in [np.ndarray, pd.DataFrame, pd.Series, list]:
            raise TypeError('Incorrect input type - got', type(x))

        elif type(x) == pd.DataFrame or type(x) == pd.Series:
            if x.ndim == 1:
                x = x.toarray().reshape(-1)
            else:
                raise ValueError('Input is not 1D')

        elif type(x) == list:
            x = np.array(x).reshape(-1)

        if type(y) not in [np.ndarray, pd.DataFrame, pd.Series, list]:
            raise TypeError('Incorrect input type - got', type(y))

        elif type(y) == pd.DataFrame or type(y) == pd.Series:
            if y.ndim == 1:
                y = y.toarray().reshape(-1)
            else:
                raise ValueError('Input is not 1D')

        elif type(y) == list:
            x = np.array(x).reshape(-1)


        if len(x) == 1:
            raise ValueError('Cannot use scalar values')

        if len(y) == 1:
            raise ValueError('Cannot use scalar values')

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

        self.equation = 'y = {0}x + {1}'.format(self.attributes['a'],self.attributes['b'])
        return self

    def predict(self, x, dplaces=None): # provide rounding accuracy in decimal places, no rounding is done if not provided
                                        # x should be a numpy array, 1D dataframe, series or list

        if type(x) not in [np.ndarray, pd.DataFrame, pd.Series, list]:
            raise TypeError('Incorrect input type - got', type(x))

        elif type(x) == pd.DataFrame or type(x) == pd.Series:
            if x.ndim == 1:
                x = x.toarray().reshape(-1)
            else:
                raise ValueError('Input is not 1D')

        elif type(x) == list:
            x = np.array(x).reshape(-1)

        if dplaces != None:
            if type(x) != int or float:
                prediction = round(self.attributes['a']*x+self.attributes['b'], dplaces)
            else:
                prediction = np.around(self.attributes['a']*x+self.attributes['b'], dplaces)
        else:
            prediction = self.attributes['a']*x+self.attributes['b']
        return prediction

    def get_eq(self): # returns a string of the equation
        print(self.equation)

    def corr_coeff(self):
        return self.attributes['r']

    def __repr__(self):
        self.info_list = {key:self.attributes[key] for key in['Mx', 'My', 'SSx', 'SSy', 'SP', 'r']}
        return 'Simple Linear Regression Model - equation: {0}, info: {1}'.format(self.equation, self.info_list)

def pcovariance(x,y): # x and y should be numpy arrays, 1D dataframes, series or lists
    if type(x) not in [np.ndarray, pd.DataFrame, pd.Series, list]:
        raise TypeError('Incorrect input type - got', type(x))

    elif type(x) == pd.DataFrame or type(x) == pd.Series:
        if x.ndim == 1:
            x = x.toarray().reshape(-1)
        else:
            raise ValueError('Input is not 1D')

    elif type(x) == list:
        x = np.array(x).reshape(-1)

    if type(y) not in [np.ndarray, pd.DataFrame, pd.Series, list]:
        raise TypeError('Incorrect input type - got', type(y))

    elif type(y) == pd.DataFrame or type(y) == pd.Series:
        if y.ndim == 1:
            y = y.toarray().reshape(-1)
        else:
            raise ValueError('Input is not 1D')

    elif type(y) == list:
        x = np.array(x).reshape(-1)

    Sy = sum((x-np.mean(x))*(y-np.mean(y)))
    return Sy / len(x)

def scovariance(x,y): # x and y should be numpy arrays, 1D dataframes, series or lists
    if type(x) not in [np.ndarray, pd.DataFrame, pd.Series, list]:
        raise TypeError('Incorrect input type - got', type(x))

    elif type(x) == pd.DataFrame or type(x) == pd.Series:
        if x.ndim == 1:
            x = x.toarray().reshape(-1)
        else:
            raise ValueError('Input is not 1D')

    elif type(x) == list:
        x = np.array(x).reshape(-1)

    if type(y) not in [np.ndarray, pd.DataFrame, pd.Series, list]:
        raise TypeError('Incorrect input type - got', type(y))

    elif type(y) == pd.DataFrame or type(y) == pd.Series:
        if y.ndim == 1:
            y = y.toarray().reshape(-1)
        else:
            raise ValueError('Input is not 1D')

    Sy = sum((x-np.mean(x))*(y-np.mean(y)))
    return Sy / (len(x)-1)

def correlation(x,y): # x and y should be numpy arrays, 1D dataframes, series or lists
    if type(x) not in [np.ndarray, pd.DataFrame, pd.Series, list]:
        raise TypeError('Incorrect input type - got', type(x))

    elif type(x) == pd.DataFrame or type(x) == pd.Series:
        if x.ndim == 1:
            x = x.toarray().reshape(-1)
        else:
            raise ValueError('Input is not 1D')

    elif type(x) == list:
        x = np.array(x).reshape(-1)

    if type(y) not in [np.ndarray, pd.DataFrame, pd.Series, list]:
        raise TypeError('Incorrect input type - got', type(y))

    elif type(y) == pd.DataFrame or type(y) == pd.Series:
        if y.ndim == 1:
            y = y.toarray().reshape(-1)
        else:
            raise ValueError('Input is not 1D')

    SSy = sum((x-np.mean(x))*(y-np.mean(y)))
    cov = SSy / len(x)
    return cov /(np.std(x)*np.std(y))

def eucdistance(x1,x2): # each value of x should be an iterable with x and y coordinates in it
    if (not hasattr(x1, '__iter__')) or (not hasattr(x2, '__iter__')):
        raise TypeError('Input is not iterable')
    return np.sqrt((x2[0]-x1[0])**2+(x2[1]-x1[1])**2)
