#################################################
#RASTERTHING
#Creates tool for ArcMap that:
##Performs slope and aspect operations on a raster
#See readmerastertool.txt for more info
#By Brady Goodwin, 3/2016
#################################################

try:
    #Import necessary libraries and extensions/ set up environments
    import arcpy 
    arcpy.CheckOutExtension("management")
    arcpy.CheckOutExtension("Spatial") 
    arcpy.env.overwriteOutput=True 
    from arcpy.sa import *   
    
    InputFile="U:/usefulstuff/TinyDEM/Tiny_elevation.img"
    OutputFileAspect="U:/PythonProjects/trashfiles/trashsaspect.img"
    OutputFileSlope="U:/PythonProjects/trashfiles/trashslope.img"
    
    
    Debug=False
    
    if Debug==False:
        
        #These will be the parameters entered via the script in arc map
        #InputFile is the DEM to be operated on
        #OutputSlope/Aspect are the output file directories
        InputFile=arcpy.GetParameterAsText(0)  #InputFile
        OutputFileAspect=arcpy.GetParameterAsText(1) #Output File for Aspect
        OutputFileSlope=arcpy.GetParameterAsText(2)  #Output File for Slope
        
    
    #The script will tell user the following information as it runs
    arcpy.AddMessage("InputRaster="+InputFile)
    arcpy.AddMessage("Aspect Output="+OutputFileAspect)
    arcpy.AddMessage("Slope Output="+OutputFileSlope)
    
    
    #Tells the script to run aspect tool on InputFile
    AspectRaster=arcpy.sa.Aspect(InputFile)
    AspectRaster.save(OutputFileAspect)
    print("Aspect Done")
    
    
    
    #Tells the script to run aspect tool on InputFile
    SlopeRaster=arcpy.sa.Slope(InputFile)
    SlopeRaster.save(OutputFileSlope)
    print("slope done")
except:
    print("Something has gone horribly wrong")