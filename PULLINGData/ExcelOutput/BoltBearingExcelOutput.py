'''
Created on Dec 2, 2018

@author: Brandon
'''

#This class takes rows from an excel file, converts them to a list of row objects,
#Takes the data from the row object, and uses it to make a calculation
#using another object. The results are then appended to a dataframe and then displayed in an
#Excel file

import pandas as pd;
from GuiClasses.BoltBearing import BoltBearing

class ExcelOutput():
    def __init__(self, ExcelInput):
        try:
            #Excel Input File
            test = pd.read_excel(ExcelInput);
            
            list1 = [];
            #Create row objects and store in a list array of objects
            for row in test.itertuples(index =False, name ='None'):
                list1.append(row);
            
            #Create a list of  BoltBearing Objects and pass parameters
            list2 =[]
            for row in list:
                x = BoltBearing(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                list2.append(x);
            
            #Access the values in the objects and create an output file    
            output = [] #Empty dictionary
            for x in list2:
                output.append({'Safety Factor':x.safetyMargin(),
                               'Area': x.bearingArea()});
            
            #Creates Data Frame Object
            df2 = pd.DataFrame(output);
            
            #Writes the output file
            df2.to_excel('df2.xlsx');
        except:
            print("Input File is incorrect");
            
