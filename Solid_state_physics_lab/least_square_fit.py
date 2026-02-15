import math
import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable

def least_square_fitting(X, Y,X_axis,Y_axis,plot,params):
    # TABLE DATA
    Σx2 = 0
    Σy = 0
    Σxy = 0
    Σx = 0
    count = 0
    Σxylist = []
    Σx2list = []
    Slno = [ ]

    for i in range(len(X)):
        Σx2 += X[i]**2
        Σx2list.append(round(X[i]**2,4))
        Σy += Y[i]
        Σxy += X[i]*Y[i]
        Σxylist.append(round(X[i]*Y[i],4))
        Σx += X[i]
        count += 1
        Slno.append(count)

    # Finding slope and intercept
    fit = np.polyfit(X,Y,1)
    A = fit[0]
    B = fit[1]
    def f(x):
      return A*x + B
    # Error analysis
    error_sum = 0
    for i in range(len(X)):
        error_sum += (Y[i] - f(X[i]))**2
    error_y = (error_sum/ (len(X) - 2))**0.5
    delta = len(X)*Σx2 - Σx**2
    error_slope = error_y * (len(X)/delta)**0.5
    error_intercept = error_y * (Σx2/delta)**0.5
    if params==True:
        #Printing slopes,intercepts and errors
        table2 = PrettyTable()
        table2.title = "Slope, Intercept and Errors"
        table2.add_row(["Slope" , round(A,3) ])
        table2.add_row(["Intercept" , round(B,3) ])
        table2.add_row(["Error in y", round(error_y,3) ])
        table2.add_row(["Delta" , round(delta,5) ])
        table2.add_row(["Error in slope", round(error_slope,5) ])
        table2.add_row(["Error in intercept", round(error_intercept,5) ])
        print(table2)
        print()

    if plot==True:
        #GRAPH PLOT
        plt.xlabel(X_axis)
        plt.ylabel(Y_axis)
        plt.title(X_axis + " vs " + Y_axis)
        plt.grid()
        plt.scatter(X,Y,label='Data Points',s=20,c='orange')
        fit = np.polyfit(X,Y,1)
        x_fit = np.linspace(min(X),max(X),1000)
        y_fit = fit[1]+fit[0]*x_fit
        plt.plot(x_fit,y_fit,'--', label = f'Least-square fit line : y = ({round(A,3)}±{round(error_slope,3)})x + ({round(B,3)}±{round(error_intercept,3)})')
        plt.legend()
        plt.show()

#Data for testing
# Y = [31.086,28.393,23.914,20.946,17.623] 
# X = [675,629,534,465,404]
# least_square_fit(X, Y,"X-axis","Y-axis",True,True)

Y =[] # temperture
for i in range(0,120):
    Y.append(i)

X = [0.00 ,0.04 ,0.08 ,0.12 ,0.16 ,0.20 ,0.24,0.28,0.32,0.36,0.40 ,0.44 ,0.48 ,0.52 ,0.56,0.60,0.64,0.68,0.72,0.76,0.80 ,0.84 ,0.88 ,0.92 ,0.96 ,1.00,1.04,1.08,1.12,1.16,1.20 ,1.24 ,1.28 ,1.32 ,1.36,1.40 ,1.44,1.49,1.53,1.57,1.61,1.65,1.69,1.73,1.77,1.81,1.85,1.90,1.94,1.98,2.02,2.06,2.10,2.14,2.18,2.23,2.27,2.31,2.35,2.39,2.43,2.47,2.51,2.56,2.60,2.64,2.68,2.72,2.76,2.80,2.85,2.89,2.93,2.97,3.01,3.05,3.10,3.14,3.18,3.22,3.26,3.30,3.35,3.39,3.43,3.47,3.51,3.56,3.60,3.64,3.68,3.72,3.76,3.81,3.85,3.89,3.93,3.97,4.01,4.06,4.10,4.14,4.18,4.22,4.26,4.31,4.35,4.39,4.43,4.47,4.51,4.55,4.60,4.64,4.68,4.72,4.76,4.80,4.84,4.88] # thermoelectric emf

least_square_fitting(X, Y,"Thermoelectric EMF (mV)","Temperature (°C)",True,True)