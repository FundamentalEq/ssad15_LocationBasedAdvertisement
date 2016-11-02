import math  #for floor funciton
kmTodegree = 111.0
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
BUSSINESS_ZONE_SIZE = 5.0
delx = 1.0/kmTodegree # width of zone = 5Km
dely = 1.0/kmTodegree # height of zone = 5Km
DELX = BUSSINESS_ZONE_SIZE/(kmTodegree)
DELY = BUSSINESS_ZONE_SIZE/(kmTodegree)
zonesAlongX =  math.ceil((right_extreme - left_extreme )/delx)
zonesAlongY = math.ceil((top_extreme - bottom_extreme)/dely)
BAREA= 25.0

MAX_SLOTS = 120
DEFAULT_BUNDLES = 10
DEFAULT_COST = 100
