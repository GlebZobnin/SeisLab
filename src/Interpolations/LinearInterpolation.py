import numpy as np

def Interp1D(x, data):
    idx_pass = np.where((~np.isnan(data)) & (data != -99999))
    x_pass = x[idx_pass]
    data_pass = data[idx_pass]
    data_interpolated = np.interp(x, x_pass, data_pass)

    idx_pass_nan = np.where(data != -99999)
    data[idx_pass_nan] = data_interpolated[idx_pass_nan]
    return data
