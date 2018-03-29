import os
import numpy as np
import pyfits as fits


msfile = 'JVLA1_peeled_uvsub_mtmfsub_eMERGE_DR1_LLRR_averaged.ms'

delmod(vis=msfile,otf=True,scr=True)
for i in range(2):
    CASA_prefix = 'JVLA1S%d_mtmfs' % i+1
    if i>0:
        incremental=True
    else:
        incremental=False
    ft(vis=msfile, model=['%s.model.tt0' % CASA_prefix, '%s.model.tt1' % CASA_prefix, '%s.model.tt2' % CASA_prefix], nterms=3, incremental=incremental)

    importfits(fitsimage='S%d_model_cc2im_adjusted.fits' % i+1, imagename='S%d_model_cc2im_adjusted.im' % i+1)
    ft(vis=msfile, model=['S%d_model_cc2im_adjusted.im' % i+1], nterms=1, incremental=True)

uvsub(vis=msfile,reverse=True)
