# Teams Status Light
***An LED peripheral that reflects the computer's current Microsoft Teams status***  
![](https://img.shields.io/badge/version-1.0.0-green)

---

**<p>The latest Teams update has removed the logging system that this script is reliant upon. The Microsoft Graph API could solve this with the `me/presence` endpoint but requires the [Presence.Read permission](https://learn.microsoft.com/en-us/graph/api/presence-get?view=graph-rest-1.0&tabs=http) which is disabled by default and requires admin approval, which proves difficult in my current organisation. I have a few ideas for how to restore functionality but until then, this project will only work with older installations of Teams.</p>**

---


Following the shift to a hybrid working environment post-COVID, it can be difficult for colleagues to determine whether I am on a Teams call or available for a discussion (usually because I have headphones in for music). This script determines the computer's current Microsoft Teams status and sends the relevant colour to the [BlinkStick Square](https://www.blinkstick.com/products/blinkstick-square) LED positioned on the desk, discretely indicating to nearby colleagues my availability if they need me.

There exist [expensive pre-built solutions](https://embrava.com/pages/microsoft-teams-busy-light) but the BlinkStick is useful as it requires no drivers (useful for corporate installation restrictions) and is simpler than constructing via Arduino, soldering and building/printing associated housing.

Unfortunately Microsoft Teams doesn't have an API accessible by the local computer unless your organisation provides access to the Graph API so instead it monitors the continuously-updated log file in AppData (in Windows or adjust for a similar location for other operating systems). Many thanks to [this PowerShell script](https://github.com/AntoineGS/TeamsStatusV2) which provided the backbone of the log scraping.

## Getting Started
The Blinkstick has in-built USB firmware so it will run out of the box without the need to install any drivers. You will need a MicroUSB cable and USB port on your device. You need to install [Python](https://www.python.org/) and the `blinkstick` library:

```
pip install blinkstick
```

Purchase a [BlinkStick Square](https://www.blinkstick.com/products/blinkstick-square), plug and play! You could use another Blinkstick product but you will need to slightly tweak the code for the BlinkStick controller.
