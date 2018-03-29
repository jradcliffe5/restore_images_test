import os
import numpy as np
from astropy.io import fits
from matplotlib import pyplot as plt
from astropy.coordinates import SkyCoord
import pickle

def generate_simple_model(outname, phasecenter, delta, size, pixsize, frequency, flux):
    header = pickle.load( open( "FITStemplate.pkl", "rb" ))
    ### Adjust header
    header['NAXIS1'] = int(size[0])
    header['NAXIS2'] = int(size[1])
    ### Adjust central pix
    central_pix = [int(size[0]/2.),int(size[1]/2.)]
    print central_pix
    header['CRPIX1'] = float(central_pix[0])
    header['CRPIX2'] = float(central_pix[1])
    ### Adjust phasecenter
    c = SkyCoord(phasecenter[0],phasecenter[1],unit=('hour','deg'))
    header['CRVAL1'] = c.ra.degree
    header['CRVAL2'] = c.dec.degree
    header['CDELT1'] = -1*pixsize[0]
    header['CDELT2'] = pixsize[1]
    ### Adjust frequency info
    header['CRVAL3'] = frequency[0]
    header['CDELT3'] = frequency[1]

    ### Generate empty numpy array
    data = np.zeros((1,1,size[0],size[1]))
    data[0,0,central_pix[0],central_pix[1]] = flux
    hdu = fits.PrimaryHDU(data,header=header)
    hdul = fits.HDUList([hdu])
    hdul.writeto(outname,overwrite=True)


generate_simple_model(outname='delta_fcn1_insert.fits',phasecenter=['12:52:25.114','+56:34:28.661'],delta=True, size=[4096,4096],pixsize=[1e-6,1e-6],frequency=[5.07209e+09,5.12012744158e+08],flux=1)
generate_simple_model(outname='delta_fcn2_insert.fits',phasecenter=['12:52:28.114','+56:34:05.661'],delta=True, size=[4096,4096],pixsize=[1e-6,1e-6],frequency=[5.07209e+09,5.12012744158e+08],flux=1)
