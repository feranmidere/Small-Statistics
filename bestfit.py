# Line of Best fit module
import numpy as np

def leastsquares(x, y):
    Mx = np.mean(x)
    My = np.mean(y)

    SS = sum((x-Mx)**2)
    SP = sum((x-Mx)*(y-My))

    a = round(SP/SS,4)
    b = round(My - (a*Mx),4)
    yhat = '{0}x+{1}'.format(a, b)
    print('yhat='+yhat)