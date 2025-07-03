import numpy as np
import matplotlib.image as img
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from matplotlib.ticker import LinearLocator
from matplotlib import _cm
from mpl_toolkits.mplot3d import Axes3D
import csv

class MyData:
    def __init__(self):
        self.filename_point = "./data/point.csv"
        #유지보수 위해 데이터를 class의 속성으로 저장해놓자.

    def get_point(self):
        point = np.genfromtxt(self.filename_point, delimiter = ',')
        return point

