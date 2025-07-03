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
        pass

    def compute_regression_polynomial(self, x, y, p=1, alpha = 0):
        x = x.reshape(-1, 1)
        y = y.reshape(-1, 1)
        A = self.matrix_A(x, p)
        theta = self.find_theta(A, y)
        f_hat = self.compute_model(theta)
        res = self.compute_residual(y , f_hat)
        loss = self.compute_loss(res)
        return f_hat
        pass

    def matrix_A(self, x, p):
        A = np.column_stack([x ** i for i in range(p)])
        return A
        
    def find_theta(self, A, y):
        theta = np.linalg.inv((self.A.T @ self.A) @ self.A.T) @ y
        return theta
    
    def compute_model(self, theta):
        f_hat = self.A @ theta
        return f_hat
        
    def compute_residual(self, y, f_hat):
        res = y - f_hat
        return res
    
    def compute_loss(self, res):
        n = len(res)
        loss = (1 / 2*n) * (res.T @ res)
        return loss
    

    

    
