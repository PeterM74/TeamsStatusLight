import os
import tailer
import time
import random
from blinkstick import blinkstick
from Functions.HelperFunctions import *

BaseLogFile = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Teams', 'logs.txt')
CurrentStatus = "Available"

fSetBlinkColour(TeamsStatusColours[CurrentStatus], Mode='Half')

while (True):

  StatusChanged = False
  PreviousStatus = CurrentStatus
  with open(BaseLogFile) as L:
    Lines = tailer.tail(L, 200)
  
  # Read through most recent updates for relevant option
  Lines.reverse()
      
  for LogLine in Lines:
     
    if any([x in LogLine for x in AvailableStatusPattern]):
	
      StatusChanged = True
      CurrentStatus = 'Available'
		
    elif any([x in LogLine for x in BusyStatusPattern]):
		
      StatusChanged = True
      CurrentStatus = 'Busy'
	  
    elif any([x in LogLine for x in AwayStatusPattern]):
		
      StatusChanged = True
      CurrentStatus = 'Away'
		
    # Check if status has changed and break loop early if true
    if (StatusChanged):
      break

  # Submit change to LED
  if (CurrentStatus != PreviousStatus):
    
    fSetBlinkColour(TeamsStatusColours[CurrentStatus], Mode='Half')

  # Adjust for faster or slower updates
  time.sleep(5)

