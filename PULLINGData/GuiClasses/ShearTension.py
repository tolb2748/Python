'''
Created on Nov 30, 2018

@author: Brandon
'''
import math;


class ShearTension:
    '''Constructor//////////////////////////////////////////////////////////////////////////////'''
    def __init__(self, yieldStress,minimumDiameter,
                 shearOneComponent, shearTwoComponent,
                 axialComponent, safetyFactor = 1.15, 
                 shearYield = None, preload = None):
        
        self.yieldStress = yieldStress;
        self.minimumDiameter = minimumDiameter;
        self.shearOneComponent = shearOneComponent;
        self.shearTwoComponent = shearTwoComponent;
        self.axialComponent = axialComponent;
        self.safetyFactor = safetyFactor;
        
        'Checks to see if preloads and shear yield stress is specified'
        if shearYield is None:
            self.shearYield = 0.577*self.yieldStress;
        else:
            self.shearYield = shearYield;
        
        if preload is None:
            self.preload = 0.65*self.yieldStress*(math.pi/4)*self.minimumDiameter**2;
        else:
            self.preload = preload;
    
    "Methods////////////////////////////////////////////////////////////////////////////////////"        
    
    def getShearYield(self):
        return self.shearYield;
        
    def Area(self):
        return (math.pi/4)*self.minimumDiameter**2;
    
    def getPreload(self):
        return self.preload;
    
    def totalShear(self):
        return math.sqrt(self.shearOneComponent**2 + self.shearTwoComponent**2)
    
    def axialForce(self):
        return self.preload + self.safetyFactor*self.axialComponent;
    
    def shearLoadRatio(self):
        return self.safetyFactor*(self.totalShear()/self.Area())/self.shearYield
    
    def axialLoadRatio(self):
        return (self.axialForce()/self.Area())/self.yieldStress;
    
    def marginOfSafety(self):
        return (1/(math.sqrt(self.axialLoadRatio()**2 + self.shearLoadRatio()**3)))-1;
