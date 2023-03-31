#This file will be the base file that calls all other functions. 
# from Hardware import Hardware as dev
import numpy as np
import pandas as pd



#States:
class state:
    #Finite States:
    currentState = 0

    #possible states:
    init = 0            #initialize hardware and move to the proper location
    follow_wall = 1     #follow the wall once, send info to stepper motors
    map = 2             #map located boll
    harvest = 3         #harvest boll(s)
    corner_in = 4       #turn arround inside a row
    corner_out = 5      #turn arround a wall
    sample = 6          #will sample data points and make a disicion 
    finish = 7          #Move from the end of the last row to the final location. Store the map to a file

#   switch commands

#   init - 0
#   Run set up code
#   Done -> sample
    
#   follow wall - 1
#   using data, will get commands for stepper motors and sent them
#   Done -> sample

#   map - 2
#   mark done boll on map
#   Done -> sample

#   harvest - 3
#   will harves cotton boll
#   Done -> map

#   corner_in - 4
#   turn around inside a row
#   Done -> sample

#   corner_out - 5
#   turn around a wall
#   Done -> sample

#   sample - 6
#   sample points and decide action
#   Data -> follow_wall, harvest, corner_in, corner_out, finish

#   finish - 7
#   recognise end of the map and save map to a file. 
    
    #Location tracking
    loc_phys = np.zeros((1,2), float) #X and Y coordinates
    loc_map = np.zeros((1,2), int) # row and plant location

#initialize a dataframe of 0s the size of the map
#6 rows, 9 plants
map = pd.DataFrame(np.zeros((6,9)), 
                   index=[1,2,3,4,5,6], 
                   columns=['P1','P2','P3','P4','P5','P6','P7','P8','P9'])

# switch statement
state = "init";

while state != finish
    match state:
        case "init":
    #         Run set up code
            state = "sample"


        case "follow_wall":
    #         get setteper commands
    #         send to motors
    #         wait till done

            state = "sample"

        case "map":
    #         update map with current information
            state = "sample"

        case "harvest"
    #         run code to harvest cotton
            state = "map"

        case "corner_in":
    #   turn around inside a row
            state = "sample"

        case "corner_out":
    #   turn around a wall
            state = "sample"

        case "sample":
    #         if the map is full
            state = "finish"
    #         else call the determine action function
            state = "/determine action/"

        case "finish":
#             just coming here breaks the loop
        
# run finishing code



#export CSV file in the prescribed format:
map.to_csv("map.csv", index_label="Row:")
