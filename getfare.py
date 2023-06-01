# #calculating fare:
# bustop = ["delhi", "mumbai", "hyderabad", "bangluru", "chattisgarh"]
# distance = [630, 800, 927, 550, 1075]
# source =input("enter the source")
# destination =input("enter the destination") 
# def getfare(source, destination):
#        for i in range(len(bustop)):
#            if source == bustop(i):
#               pass
#               for j in range(len(bustop)):
#                   if destination == bustop(j):
#                      total = distance(i+1) + distance(j)
#                      fare = (1/200) * total
#                      print(fare)
#            else:
#                 print("enter valid bustop")
#                 break
# getfare(source, destination)
    

import math
def getFare(source, destination):
    route = [["channi", "janipur", "narwal", "sainik colony", "airport road", "sidra", "bathindi", "kathua"],
             [800, 600, 750, 900, 1400, 1200, 1100, 1500]
    fare = 0.0
    if not (source in route[0] and destination in route[0]):
        print("Invalid Input")
        exit()
    if route[0].index(source) < route[0].index(destination):
        for i in range(route[0].index(source), route[0].index(destination) + 1):
            fare += route[1][i]
    elif route[0].index(destination) < route[0].index(source):
        for i in range(route[0].index(source) + 1, len(route[0])):
            fare += route[1][i]
        for i in range(0, route[0].index(destination) + 1):
            fare += route[1][i]
    return float(math.ceil(fare * 0.005))
source = input()
destination = input()
fare = getFare(source, destination)
if fare == 0:
    print("Invalid Input")
else:
    print(fare)

#printing all the even numbers in python:
#using bitwise operators