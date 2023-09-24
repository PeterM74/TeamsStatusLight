import random
from blinkstick import blinkstick
from Functions.HelperFunctions import *

# Set BlinkStick colour
def fSetBlinkColour(RGBArray, Mode='All'):

  try:
    BSObj = blinkstick.find_first()

    data = []
  
    if Mode == 'All':
      for i in range(8):
        data = data + [RGBArray[1], RGBArray[0], RGBArray[2]]
      
    elif Mode == 'Half':
      OddEvenLEDs = random.getrandbits(1)
    
      for i in range(8):
        if (i % 2) == OddEvenLEDs:
          data = data + [RGBArray[1], RGBArray[0], RGBArray[2]]
        else:
          data = data + [0, 0, 0]
  

    BSObj.set_led_data(0, data)

  except:
    pass


# BlinkStick default colours
TeamsStatusColours = {
  "Available": [0, 255, 0],
  "Away": [194, 194, 4],
  "Busy": [255, 0, 0]
}

# Log line list
AvailableStatusPattern = ['StatusIndicatorStateService: Added Available',
    'Setting the taskbar overlay icon - Available',
    'StatusIndicatorStateService: Added NewActivity (current state: Available -> NewActivity']
	  
BusyStatusPattern = ['Setting the taskbar overlay icon - Busy',
    'StatusIndicatorStateService: Added Busy',
    'Setting the taskbar overlay icon - On the phone',
    'StatusIndicatorStateService: Added OnThePhone',
    'StatusIndicatorStateService: Added NewActivity (current state: OnThePhone -> NewActivity',
    'StatusIndicatorStateService: Added NewActivity (current state: Busy -> NewActivity',
    'Setting the taskbar overlay icon - Do not disturb',
    'StatusIndicatorStateService: Added DoNotDisturb',
    'StatusIndicatorStateService: Added NewActivity (current state: DoNotDisturb -> NewActivity',
    'Setting the taskbar overlay icon - Focusing',
    'StatusIndicatorStateService: Added Focusing',
    'StatusIndicatorStateService: Added NewActivity (current state: Focusing -> NewActivity',
    'Setting the taskbar overlay icon - Presenting',
    'StatusIndicatorStateService: Added Presenting',
    'StatusIndicatorStateService: Added NewActivity (current state: Presenting -> NewActivity',
    'Setting the taskbar overlay icon - In a meeting',
    'StatusIndicatorStateService: Added InAMeeting',
    'StatusIndicatorStateService: Added NewActivity (current state: InAMeeting -> NewActivity']
      
AwayStatusPattern = ['Setting the taskbar overlay icon - Away',
    'StatusIndicatorStateService: Added Away',
    'StatusIndicatorStateService: Added NewActivity (current state: Away -> NewActivity',
    'Setting the taskbar overlay icon - Be right back',
    'StatusIndicatorStateService: Added BeRightBack',
    'StatusIndicatorStateService: Added NewActivity (current state: BeRightBack -> NewActivity']
