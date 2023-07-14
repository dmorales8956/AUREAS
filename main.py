import os 
from scipy.signal import savgol_filter
from scipy.signal import medfilt2d
import numpy as np
import scipy.io as sio
import skfuzzy as fuzz
import matplotlib.pyplot as plt
import cv2
from scipy.io import wavfile
import numpy.matlib
from scipy import signal
import scipy
from Bioacustica_Com import Metodologia

def main(ruta,band):
 ruta="H:\\Mi unidad\JOVEN INVESTIGADOR MINCIENCIAS 2022\Aureas\Audios"
 canal=1
 autosel=0
 visualize=0
 band=[2500,3000]
 table,datos_clasifi,mean_class,infoZC,gadso,repre,dispersion,frecuencia=Metodologia(ruta,band,canal,visualize,autosel)
 


