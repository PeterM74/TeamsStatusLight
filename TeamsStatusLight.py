import os
import tailer
import time
import random
import uiautomation as auto
from blinkstick import blinkstick
from Functions.HelperFunctions import *

# Settings
Method = 'UIAutomation'
BaseLogFile = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Teams', 'logs.txt')
CurrentStatus = "Available"

fSetBlinkColour(TeamsStatusColours[CurrentStatus], Mode='Half')

while (True):

  StatusChanged = False
  PreviousStatus = CurrentStatus
  
  # Method: UI Automation
  if Method == 'UIAutomation':
    # This method doesn't seem robust - wrapping in tryCatch
    try:
      TeamsWindow = auto.WindowControl(searchDepth=1, ClassName='TeamsWebView')
      ChatWindow = TeamsWindow.PaneControl(searchDepth=3, ClassName='Chrome_WidgetWin_1')
      SideBar = ChatWindow.PaneControl(searchDepth=5, ClassName='SidebarContentsSplitView')
      Button = SideBar.ButtonControl(searchDepth=15, AutomationId='idna-me-control-avatar-trigger')
      
      Status = Button.Name
      StatusWords = Status.split()
      CurrentStatus = StatusWords[(StatusWords.index('status') + 1):StatusWords.index('for')]
      CurrentStatus = ''.join(CurrentStatus)
    except Exception as error:
      print("An exception occurred:", error)
  
  # Method: Log
  elif Method == 'Log':
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
  time.sleep(4)

