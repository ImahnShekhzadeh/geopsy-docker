#!/opt/conda/bin/python3 -i

import GeopsyPySciFigs as sf
import numpy as np
import GeopsyPyCoreWave as gp

nmodes=7

freq=np.logspace(np.log10(1), np.log10(50), 500)
omega=freq.copy()
omega*=2*np.pi

h=np.array([10,20])
vp=np.array([500,1000,3000])
vs=np.array([200,600,1500])
rho=np.array([2000,2000,2500])

slowRayleigh=gp.rayleighDispersionCurve(nmodes, 0, h, vp, vs, rho, omega)
slowRayleighGroup=gp.rayleighDispersionCurve(nmodes, 1, h, vp, vs, rho, omega)
ellRayleigh=gp.rayleighEllipticityCurve(nmodes, h, vp, vs, rho, omega)
ellRayleigh=np.arctan(ellRayleigh)*(180/np.pi)
slowLove=gp.loveDispersionCurve(nmodes, 0, h, vs, rho, omega)

def layoutAttributes(p, x, y, w, h):
  p.setAnchor("TopRight")
  p.xAxis().setSizeInfo(w)
  p.yAxis().setSizeInfo(h)
  p.setPrintX(x)
  p.setPrintY(y)

def frequencyAttributes(p):
  p.xAxis().setMin(1)
  p.xAxis().setMax(50)
  p.xAxis().setScaleType("Log")
  p.xAxis().setTitle("Frequency (Hz)")

def dispersionAttributes(p):
  frequencyAttributes(p)
  p.yAxis().setScaleType("InverseLog")
  p.yAxis().setMin(1/1500)
  p.yAxis().setMax(1/150)

s=sf.newSheet()

prp=sf.newPlot(s)
sf.addCurves(prp, freq, slowRayleigh)
layoutAttributes(prp, 12, 1, 11 ,6)
dispersionAttributes(prp)
prp.yAxis().setTitle("Rayleigh phase velocity (m/s)")

prg=sf.newPlot(s)
sf.addCurves(prg, freq, slowRayleighGroup)
layoutAttributes(prg, 23, 1, 11 ,6)
dispersionAttributes(prg)
prg.yAxis().setTitle("Rayleigh group velocity (m/s)")

per=sf.newPlot(s)
sf.addCurves(per, freq, ellRayleigh)
layoutAttributes(per, 12, 7, 11 ,6)
frequencyAttributes(per)
per.yAxis().setTitle("Angular ellipticity (deg)")
per.yAxis().setMin(-90)
per.yAxis().setMax(90)
per.graphContents().layer(0).setSignThreshold(45)

pl=sf.newPlot(s)
sf.addCurves(pl, freq, slowLove)
layoutAttributes(pl, 23, 7, 11 ,6)
dispersionAttributes(pl)
pl.yAxis().setTitle("Love phase velocity (m/s)")

s.setPaperOrientation("Landscape")
s.fileSave_2("/tmp/dc.page")
s.exportImage_2("/tmp/dc.pdf")
