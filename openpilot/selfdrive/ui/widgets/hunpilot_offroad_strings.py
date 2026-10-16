"""HunPilot: offroad alert texts (selfdrived/alerts_offroad.json) for translation.

Both UIs translate the alert text with tr() before the %1 placeholder is filled in.
"""
from openpilot.system.ui.lib.multilang import tr_noop

OFFROAD_STRINGS = [
  tr_noop("Device temperature too high. System cooling down before starting. Current internal component temperature: %1"),
  tr_noop("Immediately connect to the internet to check for updates. If you do not connect to the internet, openpilot won't engage in %1"),
  tr_noop("Connect to internet to check for updates. openpilot won't automatically start until it connects to internet to check for updates."),
  tr_noop("Unable to download updates\n%1"),
  tr_noop("Chestnut detected! Switch to the release-chestnut branch to use chestnut-class models."),
  tr_noop("Chestnut model error. Restart the car to retry."),
  tr_noop("Chestnut not detected. Check USB and 12V connections, then restart the car."),
  tr_noop("Chestnut overheated. Ensure good airflow."),
  tr_noop("Chestnut update failed. Check the USB cable."),
  tr_noop("Chestnut USB link is slow. Check the USB cable. The current speed is %1."),
  tr_noop("Failed to register with comma.ai backend. It will not connect or upload to comma.ai servers, and receives no support from comma.ai. If this is a device purchased at comma.ai/shop, open a ticket at https://comma.ai/support."),
  tr_noop("openpilot was unable to identify your car. Your car is either unsupported or its ECUs are not recognized. Please submit a pull request to add the firmware versions to the proper vehicle. Need help? Join discord.comma.ai."),
  tr_noop("openpilot detected a change in the device's mounting position. Ensure the device is fully seated in the mount and the mount is firmly secured to the windshield."),
  tr_noop("Poor visibility detected for driver monitoring. Ensure the device has a clear view of the driver. This can be checked in the device settings. Extreme lighting conditions and/or unconventional mounting positions may also trigger this alert."),
  tr_noop("Excessive %1 actuation detected on your last drive. Please contact support at https://comma.ai/support and share your device's Dongle ID for troubleshooting."),
  tr_noop("Finish setup. Pair your device with comma connect to view recent drives and bookmarked routes."),
]
