#################################################
#Attribute Analyzer
#Creates tool for ArcMap that:
##Calculates mean, sum, and total number of attributes 
## in a field
#See readmeshapefiletool.txt for more info
#By Brady Goodwin, 3/2016
#################################################

try:
    #Import necessary libraries and extensions/ set up environments
    import arcpy
    arcpy.env.overwriteOutput=True
    
    
    #These are fileds used in debugging so I don't have to go into arcmap
    # each time I want to test the tool
    Shapefile="U:/usefulstuff/usefulshapefiles/humboldtcounty/apnhum52sp.shp"
    Field="PERIMETER"
    
    
    
    
    
    #Turn Debug on or off
    Debugging=False   
    
    
    if (Debugging==False):
        #These will be the parameters entered via the script in arc map
        #ShapeFile is the DEM to be operated on
        #Field is the field to be analyzed    
        #This is stuff like distance, file name, etc. Rename to something better. Parameters from ArcMap Environments in ArcMap
        Shapefile=arcpy.GetParameterAsText(0)     #InputLayer
        Field=arcpy.GetParameterAsText(1)    #Attribute Field     
    
    
    
    #Prints out messages in tool so you can see what you put in.
    arcpy.AddMessage("Shapefile="+Shapefile)
    arcpy.AddMessage("Field="+Field)
    
    
    #Create a search cursor based on the shapefile
    #Looks through the Shapefile qq
    TheRows=arcpy.SearchCursor(Shapefile)
    
    
    #This loop operates as follows-
    #TheList is created and is empty, and has a length (lens) of zero
    #NumElements is the length of the list (0 at the start)
    #Count counter is started at 0 so it is same length as NumElements
    #Sum starts at zero, values from the field will be added to this as the loop iterates
    #TheRow is "searchcursored" for by TheRows
    #TheValue is then set as the current iteration through TheRows
    #TheValue is appended to TheList
    #TheValue is then added to Sum, which does not reset and is thus cumulative
    #NumElements is updated to correspond to the length of the new list
    #Count is increased by one
    #Loop runs while NumElements and Count are the same, so when no more field attributes
    ## Num Elements wont be updated and count counter will be 1 higher, ending loop
    #Figured this out w/ Destiny
    try:    
        TheList=[]
        NumElements=len(TheList)
        count=0
        Sum=0
        if (NumElements==count):
            for TheRow in TheRows:
                TheValue=TheRow.getValue(Field)
                TheList.append(TheValue)
                Sum=Sum+TheValue
                NumElements=len(TheList)
                count=count+1
    except:
        print("Failed Loop")
    
    #Does basic math on final Value and prints pertinent info to arcmap        
    arcpy.AddMessage("The Count is:")
    arcpy.AddMessage(NumElements)
    
    arcpy.AddMessage("The Sum is:")
    arcpy.AddMessage(Sum)
    
    Mean=(Sum / NumElements)
    arcpy.AddMessage("The Mean is:")
    arcpy.AddMessage(Mean)
except:
    print("something has gone horribly wrong")





