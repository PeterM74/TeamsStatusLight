# Teams Status Light
***An LED peripheral that reflects the computer's current Microsoft Teams status***  
![](https://img.shields.io/badge/version-1.1.0-green)

Following the shift to a hybrid working environment post-COVID, it can be difficult for colleagues to determine whether I am on a Teams call or available for a discussion (usually because I have headphones in for music). This script determines the computer's current Microsoft Teams status and sends the relevant colour to the [BlinkStick Square](https://www.blinkstick.com/products/blinkstick-square) LED positioned on the desk, discretely indicating to nearby colleagues my availability if they need me.

There exist [expensive pre-built solutions](https://embrava.com/pages/microsoft-teams-busy-light) but the BlinkStick is useful as it requires no drivers (useful for corporate installation restrictions) and is simpler than constructing via Arduino, soldering and building/printing associated housing.

While the Microsoft Teams' status is accessible from the Microsoft Graph API (via the `me/presence` endpoint), it requires `Presence.Read` permission which is denied by default permission settings and requires admin organisational permission to approve. The old '[Classic](https://learn.microsoft.com/en-us/officeupdates/teams-app-versioning)' versions of Teams output a log file which could be parsed for status changes, however the latest 'New' Teams removed this feature. Instead, the in-built Windows UI Automation service is used to read the Teams' status (only available on Windows machines). Both the UI Automation and Log methods are implemented. If you are able to use the Graph API instead (recommended), please see the [documentation](https://learn.microsoft.com/en-us/graph/api/presence-get?view=graph-rest-1.0&tabs=http) to request.

Many thanks to [this PowerShell script](https://github.com/AntoineGS/TeamsStatusV2) and [this .NET implementation](https://github.com/miscalencu/OnlineStatusLight) which provided the backbone of this script.

## Getting Started
The Blinkstick has in-built USB firmware so it will run out of the box without the need to install any drivers. You will need a MicroUSB cable and USB port on your device. You need to install [Python](https://www.python.org/) and the required libraries:

```
pip install -r requirements.txt
```

Purchase a [BlinkStick Square](https://www.blinkstick.com/products/blinkstick-square), plug and play! You could use another Blinkstick product but you will need to slightly tweak the code for any other BlinkStick product.

The UIAutomation method has only been tested on my Windows laptop and as such, the UIAutomation classes/IDs used to extract data may be different on another machine. If the code is not finding the data, it may be referencing an out-of-date UI tree structure or one that is unique to my machine. To evaluate your own, you can view the UI for your device after installing the `uiautomation` library and running from cmd (while only having the Windows Teams application open):

```
pyautomation.exe -r
```

If you are having trouble interpretting the output, open an issue and attach the `@AutomationLog.txt` that was generated in your user folder and I will try to help.
