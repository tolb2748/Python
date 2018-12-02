'''
Created on Nov 30, 2018

@author: Brandon
'''
import math

class ShearTearOut:
    
    def __init__(self, shearStrength, nominalDiameter, e, thickness, 
                 shearOneComponent, shearTwoComponent, safetyFactor = 1.15  ):
        
        self.shearStrength = shearStrength;
        self.nominalDiameter = nominalDiameter;
        self.e = e;
        self.thickness = thickness;
        self.shearOneComponent = shearOneComponent;
        self.shearTwoComponent = shearTwoComponent;
        self.safetyFactor = safetyFactor;
        
    def shearArea(self):
        return 2*self.thickness*(self.e - (self.nominalDiameter/2));
    
    def totalShear(self):
        return math.sqrt(self.shearOneComponent**2 + self.shearTwoComponent**2)
        
    def safetyMargin(self): 
        return (self.shearStrength/(self.safetyFactor*(self.totalShear()/self.shearArea())))-1
    