import numpy as np

err_const = 2.5/np.log(10)

def err_add(a, b):
    return np.sqrt(a**2 + b**2)

def flux2mag(f, df):
    mag = -2.5*np.log10(f)
    mag_err = mag*err_const*df/f
    return mag, mag_err