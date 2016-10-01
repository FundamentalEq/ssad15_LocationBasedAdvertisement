import math  #for floor funciton

#limiting longitutde and latitde around THE INDIA
# left_extreme = 68.03215
# right_extreme = 97.16712
# top_extreme = 33.24902
# bottom_extreme = 8.06890
#limiting values for hyderabad (for purpose of testing)
left_extreme = 78.2311237
right_extreme = 78.692392
top_extreme = 17.599900
bottom_extreme = 17.2015163

#SIZE OF EACH SQUARE
delx = 5.0/111 # width of zone = 5Km
dely = 5.0/111 # height of zone = 5Km

zonesAlongX =  math.floor((right_extreme - left_extreme )/delx)
zonesAlongY = math.floor((top_extreme - bottom_extreme)/dely)
