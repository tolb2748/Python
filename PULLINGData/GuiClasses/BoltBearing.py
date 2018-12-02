'''
Created on Nov 30, 2018

@author: Brandon
'''
import math
import numpy as np;

class BoltBearing():
    def __init__(self, bearingStrengthUpper, bearingStrengthLower, 
                 nominalDiameter, e, thickness, shearOneComponent, shearTwoComponent, 
                 safetyFactor = 1.15 ):
        
        self.bearingStrengthUpper = bearingStrengthUpper;
        self.bearingStrenghtLower = bearingStrengthLower;
        self.nominalDiameter = nominalDiameter;
        self.e = e;
        self.thickness = thickness;
        self.shearOneComponent = shearOneComponent;
        self.shearTwoComponent = shearTwoComponent;
        self.safetyFactor = safetyFactor;
        
    
    def bearingStrengthinterpolation(self):
        eOverD = self.e/self.nominalDiameter;
        return np.interp(eOverD, [1.5,2], [self.bearingStrenghtLower, self.bearingStrengthUpper])
    
    def bearingArea(self):
        return self.nominalDiameter*self.thickness;
    
    def totalShear(self):
        return math.sqrt(self.shearOneComponent**2 + self.shearTwoComponent**2)
    
    def safetyMargin(self):
        return (self.bearingStrengthinterpolation()/(self.safetyFactor*(self.totalShear()/self.bearingArea()))) - 1;
