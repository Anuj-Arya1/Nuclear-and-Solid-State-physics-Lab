
# magneto resistance 

import numpy as np
import matplotlib.pyplot as plt


B1 = [-5.67,-5.44,-5.10,-4.66,-4.22,-3.74,-3.25,-2.18,-1.61,-1.75,-0.599,0.536,1.05,1.556,2.10,3.13,3.61,4.05,4.5,4.89,5.21,5.45] # KGauss
V1 = [0.025,0.024,0.023,0.022,0.020,0.019,0.017,0.015,0.012,0.011,0.011,0.013,0.014,0.015,0.017,0.020,0.022,0.023,0.024,0.025,0.026,0.028]
Ip1=185.1 # mA probe current
Voff1 = 0.012 # mV offset voltage

Vcorr1 =[]
for i in range(len(V1)):
    Vcorr1.append(V1[i]-Voff1)
R_or = 6.48e-5 # ohm

R1 = np.array(Vcorr1)/Ip1 # ohm

del_R1 = []
for i in range(len(R1)):
    R1[i] = (R1[i]-R_or)/R_or
    del_R1.append(R1[i])
# polyfitting 
coeffs = np.polyfit(B1, del_R1, 2) # quadratic fit
# PLOTTING 
plt.figure(figsize=(8,6))
plt.scatter(B1, del_R1, marker='o', linestyle='-', color='b',label='Data Points')
plt.plot(B1, np.polyval(coeffs, B1), color='r', label='Quadratic Fit')
plt.legend()
plt.title('Magnetoresistance of Bismuth Sample(at probe current='+str(Ip1)+' mA)', fontsize=16)
plt.xlabel('Magnetic Field B (KGauss)', fontsize=14)
plt.ylabel('Relative Change in Resistance ΔR/R₀', fontsize=14)
plt.grid(True)
plt.show()
# plot of log(del_R/R) vs log(B) 
log_r = np.log10(np.abs(del_R1[11:]))
log_B = np.log10(np.abs(B1[11:]))

coeffs_log = np.polyfit(log_B, log_r, 1) # linear fit
plt.scatter(log_B, log_r, marker='o', linestyle='-', color='b',label='Data Points')
plt.plot(log_B, np.polyval(coeffs_log, log_B), color='r', label='Linear Fit')
plt.legend()
plt.title('Log-Log Plot of Magnetoresistance of Bismuth Sample(at probe current='+str(Ip1)+' mA)', fontsize=16)
plt.xlabel('log(B) (kGauss)', fontsize=14)
plt.ylabel('log(ΔR/R₀)', fontsize=14)
plt.grid(True)
plt.show()





# DATA
Ip = 152.5 # mA probe current
Voff = 0.006 # mV offset voltage
B = [-5.54,-5.29,-4.93,-4.56,-4.07,-3.61,-3.12,-2.06,-1.545,-1.023,-0.513,0.508,1.088,1.616,2.13,3.18,3.74,4.16,4.63,5.01,5.37,5.61]# KGauss
V = [0.019,0.018,0.017,0.016,0.015,0.014,0.013,0.012,0.011,0.010,0.009,0.007,0.008,0.009,0.010,0.013,0.015,0.016,0.017,0.019,0.020,0.021] # mV
Vcorr =[]
for i in range(len(V)):
    Vcorr.append(V[i]-Voff)
R_or = 3.93e-5 # ohm meter

R = []
for i in range(len(Vcorr)):
    R.append((Vcorr[i]*1e-3)/(Ip*1e-3)) # ohm

del_R = []
for i in range(len(R)):
    R[i] = (R[i]-R_or)/R_or
    del_R.append(R[i])
# ploy fitting
coeffs = np.polyfit(B, del_R, 2) # quadratic fit

# PLOTTING
# plt.figure(figsize=(8,6))
# plt.scatter(B, del_R, marker='o', linestyle='-', color='b',label='Data Points')
# plt.plot(B, np.polyval(coeffs, B), color='r', label='Quadratic Fit')
# plt.legend()
# plt.title('Magnetoresistance of Bismuth Sample(at probe current='+str(Ip)+' mA)', fontsize=16)
# plt.xlabel('Magnetic Field B (KGauss)', fontsize=14)
# plt.ylabel('Relative Change in Resistance ΔR/R₀', fontsize=14)
# plt.grid(True)
# plt.show()
