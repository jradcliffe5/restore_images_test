import os
import numpy as np
import pyfits as fits
from matplotlib import pyplot as plt

## Inputs ##
msfile = '1252+5634.ms'
model_fits = ['delta_fcn1_insert.fits','delta_fcn2_insert.fits']
j = 0

clearcal(vis=msfile,addmodel=True)
for i in model_fits:
    importfits(fitsimage=i,imagename=i.split('.fits')[0]+'.im',overwrite=True)
    imagename = i.split('.fits')[0]+'.im'
    if j == 0:
        incremental = False
    else:
        incremental = True
    ft(vis=msfile,model=imagename,incremental=incremental)
    j = j+1

uvsub(vis=msfile,reverse=True)

tclean(vis="1252+5634.ms",selectdata=True,field="",spw="",timerange="",uvrange="",antenna="",scan="",observation="",intent="",datacolumn="corrected",imagename="offset_%s_image_model" % len(model_fits),imsize=4096,cell="0.01arcsec",phasecenter="",stokes="I",projection="SIN",startmodel="",specmode="mfs",reffreq="",nchan=-1,start="",width="",outframe="LSRK",veltype="radio",restfreq=[],interpolation="linear",gridder="standard",facets=1,chanchunks=1,wprojplanes=1,vptable="",aterm=True,psterm=False,wbawp=True,conjbeams=True,cfcache="",computepastep=360.0,rotatepastep=360.0,pblimit=0.2,normtype="flatnoise",deconvolver="clark",scales=[],nterms=2,smallscalebias=0.6,restoration=True,restoringbeam=[],pbcor=False,outlierfile="",weighting="natural",robust=0.5,npixels=0,uvtaper=[],niter=100000,gain=0.1,threshold=0.0,cycleniter=-1,cyclefactor=1.0,minpsffraction=0.05,maxpsffraction=0.8,interactive=True,usemask="user",mask="",pbmask=0.0,maskthreshold="",maskresolution="",nmask=0,sidelobethreshold=3.0,noisethreshold=5.0,lownoisethreshold=1.5,negativethreshold=0.0,smoothfactor=1.0,minbeamfrac=0.3,cutthreshold=0.01,growiterations=75,restart=True,savemodel="none",calcres=True,calcpsf=True,parallel=False)
