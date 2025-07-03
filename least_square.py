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
        self.filename_point = "./point.csv"
        #유지보수 위해 데이터를 class의 속성으로 저장해놓자.

    def get_point(self):
        point = np.genfromtxt(self.filename_point, delimiter = ',')
        return point

class MyPlot:
    def __init__(self):
        self.fig_size = (8, 8)
    
    def plot_point(self, x, y1, y2 = None):
        plt.figure(figsize = self.fig_size)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.scatter(x, y1, marker = '.', color = 'blue')
        if y2 is not None:
            plt.plot(y2, color = 'red')

class MyUtil:
    def __init__(self,A):
        self.A = None
        self.theta = None
        pass

    def compute_regression_polynomial(self, x, y, p=1, alpha = 0):
        pass

    def matrix_A(self, x, p):
        self.A = np.column_stack([x ** i for i in range(p)])
    
    def init_theta(self):
        theta = np.zeros(self.A.shape[0])
        return theta
    
    def compute_model(self, theta):
        self.f_hat = self.A @ theta
        
    
    def compute_residual(self, y):
        self.res = y - self.f_hat
    
    def compute_loss(self):
        n = self.A.shpae[0]
        loss = (1 / 2*n) * (self.res.T @ self.res)
        return loss
    

    

    
