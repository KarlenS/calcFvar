#!/usr/bin/python

import numpy as np
import argparse
import sys

#parsing arguments
parser = argparse.ArgumentParser(description='Requires input file with columns: mjd, flux, mdj_err, flux_err.')
parser.add_argument('infile', nargs='+',type=str, default="input.dat", help="Input file name")
args = parser.parse_args()

f = np.genfromtxt(args.infile[0],names=['mjd','flux','mjd_err','fluxerr'])

mjd = f['mjd']
mjd_err = f['mjd_err']
flux = f['flux']
fluxerr = f['fluxerr']

lc_mean = flux.mean()
lc_std = flux.std()

N = flux.size

#dist_to_mean = (flux - lc_mean)
fluxerr_sq = np.power(fluxerr,2)
mse = fluxerr_sq.mean()
var = np.power(lc_std,2)

Fvar = np.sqrt(np.abs((np.power(var,2) - mse)/np.power(lc_mean,2)))

Fvar_err = (1./(2.*N)*mse**2/(lc_mean**4*Fvar**2)+mse/(N*lc_mean**2))**0.5
#Fvar_err = (Fvar**2. + (2.*mse**2./(N*lc_mean**4.) + 4.*mse*Fvar**2./(N*lc_mean**2.))**0.5)**0.5 - Fvar

print Fvar, Fvar_err
