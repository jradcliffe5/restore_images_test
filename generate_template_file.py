import pickle
import numpy as np
from astropy.io import fits
header = fits.open('PG1700_NA.fits')[0].header
del header['HISTORY']
f = open("FITStemplate.pkl","wb")
pickle.dump(header,f)
f.close()
