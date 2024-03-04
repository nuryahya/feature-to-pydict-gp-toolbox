"""Main module."""
import arcpy
import os
import logging

class Toolbox(object):
    def __init__(self):
        self.label = "Dict toolbox"
        self.alias = "Feature to Dict Tool"
        self.tools = [FeatureToDictionary]

class FeatureToDictionary(object):
    def __init__(self,in_feature,directory):
        self.label = "Dire Dictionary"
        self.description = "Sinuosity measures the amount that a river " + \
                           "meanders within its valley, calculated by " + \
                           "dividing total stream length by valley length."
        self.in_feature = in_feature
        self.directory = directory
        # in_feature.value = input("infrea")
        # directory.value = input("dirrrr")
        # object = in_feature.value,directory.value
        # return object

    def execute(self):
        in_Feaure = self.in_feature
        directory = self.directory

        listFields = arcpy.ListFields(in_Feaure)
        fields = [field.name for field in listFields]
        fields.append("SHAPE@")
        Cursor = arcpy.SearchCursor(in_Feaure)
        CursorDa = arcpy.da.SearchCursor(in_Feaure, fields)
        featureDict = dict()

        for row, rowDa in zip(Cursor, CursorDa):
            k = rowDa[0]
            v1 = row.getValue(fields[1])
            v2 = rowDa[1:]
            vtoken = rowDa[-1]
            value = [v1, v2, vtoken]
            featureDict[k] = value
        del Cursor
        del CursorDa

        os.chdir(directory)
        logging.basicConfig(filename= 'FeatureDictionary.log', level=logging.INFO)
        logging.info("It is Me")
        with open('FeatureDictionary.log','w') as textWriter:
            textWriter.write(str(featureDict))
        return featureDict

st = FeatureToDictionary(in_feature=arcpy.GetParameterAsText(0),directory=arcpy.GetParameterAsText(1))
st.execute()




