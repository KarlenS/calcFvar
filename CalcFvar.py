#!/usr/bin/python

import numpy as np

filename = "lcdata_420_1TeV.txt"

mjd,flux,fluxerr = np.loadtxt(filename,unpack=True)

lc_mean = flux.mean()
lc_std = flux.std()

N = flux.size

#dist_to_mean = (flux - lc_mean)
fluxerr_sq = fluxerr**2
mse = fluxerr_sq.mean()

print lc_std**2.
print lc_mean**2.
print mse

Fvar = ((lc_std**2. - mse)/lc_mean**2.)**0.5

Fvar_err = (Fvar**2. + (2.*mse**2./(N*lc_mean**4.) + 4.*mse*Fvar**2./(N*lc_mean**2.))**0.5)**0.5 - Fvar

print Fvar
print Fvar_err
