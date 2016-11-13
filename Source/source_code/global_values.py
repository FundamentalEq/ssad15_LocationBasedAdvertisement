import math  #for floor funciton
from decimal import *
kmTodegree = Decimal(111.0)
#limiting longitutde and latitde around THE INDIA
# left_extreme = 68.03215
# right_extreme = 97.16712
# top_extreme = 33.24902
# bottom_extreme = 8.06890
#limiting values for hyderabad (for purpose of testing)
left_extreme = Decimal(78.2311237)
right_extreme = Decimal(78.692392)
top_extreme = Decimal(17.599900)
bottom_extreme = Decimal(17.2015163)

#SIZE OF EACH SQUARE
BUSSINESS_ZONE_SIZE = Decimal(5.0)
delx = Decimal(1)/kmTodegree # width of zone = 5Km
dely = Decimal(1)/kmTodegree # height of zone = 5Km
DELX = BUSSINESS_ZONE_SIZE/(kmTodegree)
DELY = BUSSINESS_ZONE_SIZE/(kmTodegree)
zonesAlongX =  math.ceil((right_extreme - left_extreme )/delx)
zonesAlongY = math.ceil((top_extreme - bottom_extreme)/dely)
BAREA= Decimal(25)

MAX_SLOTS = 120
DEFAULT_BUNDLES = Decimal(10)
DEFAULT_COST = 100
