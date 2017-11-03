import os
import numpy as np
os.chdir('C:\stuff\Studies\Fall 17\Elements of AI\Assignment 1\Problem 1')

w={"house":{"Name":"Haus","Address":"Bloomington"},"bungalow":{"Name":"Black Sheep","Address":"Bloomington"}}

w["house"]["Address"]
c="house"
w[c]
w={"house":"Haus","cat":"Katze","red":"rot"}

#Structure of dictionary
w={"V1":{"Latitude":23, "Longitude":98,"Segment":{"V2":{"Length":44,"Speed_Limit":77,"Highway":"US_71"},"V3":{"Length":72,"Speed_Limit":100,"Highway":"ME_16"}}}}

#Reading files and loading into dictionary

w["V1"]["Segment"]  #To access segment
w["V1"]["Segment"]["V2"]["Length"] #To get a length of V2

(w["V1"]["Segment"].keys()) # To get connected cities

for cities in w["V1"]["Segment"]:
    print(cities)
    print(w["V1"]["Segment"][cities]["Length"])
    #Above, we printed city name and length
type(cities) #str
type(w["V1"]["Segment"][cities]["Length"]) #int

#Problem Start Demo
#Adding 2 cities
route_problem={"V1":{"Latitude":23, "Longitude":98, "Visited":0,"Path":"","Total_Distance":0,"Total_Time":0, \
         "Segment":{"V2":{"Length":44,"Speed_Limit":77,"Highway":"US_71"}, \
                    "V3":{"Length":72,"Speed_Limit":100,"Highway":"ME_16"}}}, \
    "V2":{"Latitude":21,"Longitude":120, "Visited":0,"Path":"","Total_Distance":0,"Total_Time":0, \
          "Segment": {"V1":{"Length":44, "Speed_Limit":77,"Highway":"US_71"}, \
                      "V4":{"Length":77,"Speed_Limit":90,"Highway":"WI_29"}}}, \
          "V3":{"Latitude":27,"Longitude":99,"Visited":0,"Path":"","Total_Distance":0,"Total_Time":0, \
                "Segment":{"V1":{"Length":72,"Speed_Limit":100,"Highway":"ME_16"}, \
                           "V5":{"Length":99,"Speed_Limit":90,"Highway":"US_56"}}}, \
                "V4":{"Latitude":21,"Longitude":166,"Visited":0,"Path":"","Total_Distance":0,"Total_Time":0, \
                      "Segment":{"V2":{"Length":77,"Speed_Limit":90,"Highway":"WI_29"}}}, \
                      "V5":{"Latitude":33,"Longitude":200, "Visited":0,"Path":"","Total_Distance":0,"Total_Time":0, \
                            "Segment":{"V3":{"Length":99,"Speed_Limit":90,"Highway":"US_56"}}}}
    
    
#Traversing from V1 to V4
goal=0
initial_city="V5"
goal_city="V4"
route_problem[initial_city]["Visited"]=1
route_problem[initial_city]["Path"] = initial_city
#current_city=initial_city
fringe=[initial_city]
#t=fringe.pop() #Need to see the architecture
while len(fringe)>0 and goal ==0:
   current_city=fringe.pop() 
   for cities in route_problem[current_city]["Segment"]:
       if route_problem[cities]["Visited"]==0:
          if cities==goal_city:
              print("Goal Reached")
              goal=1
              
          else:
              fringe.append(cities)
          route_problem[cities]["Visited"]=1
          route_problem[cities]["Path"]= route_problem[current_city]["Path"] + "->" + cities
          #Total Distance
          route_problem[cities]["Total_Distance"]= \
          route_problem[current_city]["Segment"][cities]["Length"] + \
          route_problem[current_city]["Total_Distance"]
          #Total Time
          route_problem[cities]["Total_Time"]= \
          route_problem[current_city]["Segment"][cities]["Length"]/route_problem[current_city]["Segment"][cities]["Speed_Limit"] + \
          route_problem[current_city]["Total_Time"]

#route_problem
if goal==0:
    print("Sorry, No Path Found")
else:
    print("Path: " + route_problem[goal_city]["Path"])
    print("Distance: " + str(route_problem[goal_city]["Total_Distance"]))
    print("Time: " + str(route_problem[goal_city]["Total_Time"]))
    
    
    
    
#Fair
route_problem={}
###route_problem[3]=9  #Example of adding key-val
###del route_problem[3]
f=open("city-gps.txt")
for line in f:
    route_problem[(line.split()[0])]={}
    route_problem[(line.split()[0])]["Latitude"]=float(line.split()[1])
    route_problem[(line.split()[0])]["Longitude"]=float(line.split()[2])
    route_problem[(line.split()[0])]["Segment"]={}
    route_problem[(line.split()[0])]["Path"]=""
    route_problem[(line.split()[0])]["Total_Distance"]=0
    route_problem[(line.split()[0])]["Total_Time"]=0
    route_problem[(line.split()[0])]["Visited"]=0
f.close()

f=open("road-segments.txt")
for line in f:
    if line.split()[0]==line.split()[1]:
        continue
    #If city 1 not found in dictionary, add to dictionary
    if line.split()[0] not in route_problem:
        route_problem[(line.split()[0])]={}
        route_problem[(line.split()[0])]["Latitude"]=0
        route_problem[(line.split()[0])]["Longitude"]=0
        route_problem[(line.split()[0])]["Segment"]={}
        route_problem[(line.split()[0])]["Path"]=""
        route_problem[(line.split()[0])]["Total_Distance"]=0
        route_problem[(line.split()[0])]["Total_Time"]=0
        route_problem[(line.split()[0])]["Visited"]=0
    #If ends
    # if city 2 not found in dictionary, add to dictionary
    if line.split()[1] not in route_problem:
        route_problem[(line.split()[1])]={}
        route_problem[(line.split()[1])]["Latitude"]=0
        route_problem[(line.split()[1])]["Longitude"]=0
        route_problem[(line.split()[1])]["Segment"]={}
        route_problem[(line.split()[1])]["Path"]=""
        route_problem[(line.split()[1])]["Total_Distance"]=0
        route_problem[(line.split()[1])]["Total_Time"]=0
        route_problem[(line.split()[1])]["Visited"]=0
    #If ends
    #Add to city 1 key - length, speed limit and highway    
    route_problem[line.split()[0]]["Segment"][line.split()[1]]={}
    route_problem[line.split()[0]]["Segment"][line.split()[1]]["Length"]=float(line.split()[2])
    #Handling Missing Speed and 0 speed
    if len(line.split())==5 and float(line.split()[3])>0:
        route_problem[line.split()[0]]["Segment"][line.split()[1]]["Speed_Limit"]=float(line.split()[3])
        route_problem[line.split()[0]]["Segment"][line.split()[1]]["Highway"]=line.split()[4]
    else:
        route_problem[line.split()[0]]["Segment"][line.split()[1]]["Speed_Limit"]=40
        route_problem[line.split()[0]]["Segment"][line.split()[1]]["Highway"]=line.split()[3]
    #Add to city 2 key    
    route_problem[line.split()[1]]["Segment"][line.split()[0]]={}
    route_problem[line.split()[1]]["Segment"][line.split()[0]]["Length"]=float(line.split()[2])
    #Handling missing speed and 0 speed
    if len(line.split())==5 and float(line.split()[3])>0:
        route_problem[line.split()[1]]["Segment"][line.split()[0]]["Speed_Limit"]=float(line.split()[3])
        route_problem[line.split()[1]]["Segment"][line.split()[0]]["Highway"]=line.split()[4]
    else:
        route_problem[line.split()[1]]["Segment"][line.split()[0]]["Speed_Limit"]=40  
        route_problem[line.split()[1]]["Segment"][line.split()[0]]["Highway"]=line.split()[3]
        
f.close()



#Routing Problem

#Traversing from V1 to V4
goal=0
initial_city="Bloomington,_Indiana"
goal_city="Indianapolis,_Indiana"
route_problem[initial_city]["Visited"]=1
route_problem[initial_city]["Path"] = initial_city
#current_city=initial_city
fringe=[initial_city]
#t=fringe.pop() #Need to see the architecture
while len(fringe)>0 and goal ==0:
   current_city=fringe.pop(0) 
   for cities in route_problem[current_city]["Segment"]:
       if route_problem[cities]["Visited"]==0:
          if cities==goal_city:
              print("Goal Reached")
              goal=1
              
          else:
              fringe.append(cities)
          route_problem[cities]["Visited"]=1
          route_problem[cities]["Path"]= route_problem[current_city]["Path"] + "->" + cities
          #Total Distance
          route_problem[cities]["Total_Distance"]= \
          route_problem[current_city]["Segment"][cities]["Length"] + \
          route_problem[current_city]["Total_Distance"]
          #Total Time
          route_problem[cities]["Total_Time"]= \
          route_problem[current_city]["Segment"][cities]["Length"]/route_problem[current_city]["Segment"][cities]["Speed_Limit"] + \
          route_problem[current_city]["Total_Time"]

#route_problem
if goal==0:
    print("Sorry, No Path Found")
else:
    print("Path: " + route_problem[goal_city]["Path"])
    print("Distance: " + str(route_problem[goal_city]["Total_Distance"]))
    print("Time: " + str(route_problem[goal_city]["Total_Time"]))