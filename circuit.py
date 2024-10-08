# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams['font.size'] = 15

'''using the python physics video on circuits by Dot Physics on youtube'''


'''plot how time series of variables in LRC circuit'''
class LRC:
    
    '''choose to use AC frequency by providing a
    different f_AC (frequency) value'''
    def __init__(self, dt, L, R, C, DC, f_AC=0):
        self.dt, self.L, self.R, self.C, self.DC, self.f_AC = dt, L, R, C, DC, f_AC
        
    '''get data for t_end seconds'''
    def run(self, t_end): 
        t=0
        I=0
        Q=0
        emf=self.DC
        
        self.varColumns = ['t', 'I', 'Q', 'V_C', 'V_R']
        self.varTitles = ['Time [s]', 'Current [A]',
                           'Charge [C]', 'V_capacitor [V]',
                           'V_resistor [V]']
        self.data = ([t, I, Q, 0, 0])
        
        while t<t_end:
            if self.f_AC != 0:
                emf = self.DC * np.cos(self.f_AC * t)
            
            V_C=Q/self.C
            V_R=I*self.R
            dI=(self.dt/self.L)*(emf-V_C-V_R)
            
            I+=dI
            t+=self.dt
            Q+=(I*self.dt)
            
            dataRow = ([t, I, Q, V_C, V_R])
            self.data = np.vstack((self.data, dataRow))
    
    '''plot variable change over t_end seconds
    var options: 'I', 'Q', 'V_C', 'V_R' 
    use num to plot a variable from differnet 
    circuits on the same graph'''
    def plot(self, var, t_end, num=None):
        
        self.run(t_end)
        t = self.data[:,self.varColumns.index('t')]
        varIndex = self.varColumns.index(var)
        varData = self.data[:,varIndex]
        
        fig = plt.figure(figsize=(10,7), num=num)
        plt.plot(t, varData, label=f'L={self.L}, R={self.R}, C={self.C}')
        plt.xlabel('Time [s]')
        plt.ylabel(self.varTitles[varIndex])
        plt.legend()
        plt.show()
    
    
if __name__ == "__main__":
    
    t=30
    
    circuit_A = LRC(0.001, 0.3, 0.1, 1, 3)
    circuit_A.plot('Q', t, 'Comp 1')
    circuit_A.plot('I', t, 'Comp 2')
    
    circuit_B = LRC(0.001, 0.1, 0.1, 1, 3)
    circuit_B.plot('Q', t, 'Comp 1')
    circuit_B.plot('I', t, 'Comp 2')

    
    