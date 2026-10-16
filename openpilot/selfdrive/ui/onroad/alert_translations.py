"""HunPilot: translate driving alerts at render time.

The alert texts are created in selfdrived/events.py in English. Instead of changing every
alert there, the UI looks the text up in the normal translation files (app_<lang>.po).
Texts with a number in them (speed, percent, minutes) are matched with "{}" templates.
"""
import re

from openpilot.system.ui.lib.multilang import multilang, tr, tr_noop

ALERT_STRINGS = [
  tr_noop("BRAKE!"),
  tr_noop("CAN Bus Disconnected"),
  tr_noop("Controls Mismatch"),
  tr_noop("Cruise Fault: Restart the Car"),
  tr_noop("Cruise Is Off"),
  tr_noop("DISENGAGE IMMEDIATELY"),
  tr_noop("Driver Distracted"),
  tr_noop("Driver Unresponsive"),
  tr_noop("Emergency Braking: Risk of Collision"),
  tr_noop("Harness Relay Malfunction"),
  tr_noop("LKAS Fault: Restart the Car"),
  tr_noop("locationd Permanent Error"),
  tr_noop("paramsd Permanent Error"),
  tr_noop("Reverse"),
  tr_noop("Reverse Gear"),
  tr_noop("Risk of Collision"),
  tr_noop("Stock AEB: Risk of Collision"),
  tr_noop("TAKE CONTROL IMMEDIATELY"),
  tr_noop("Unknown Vehicle Variant"),
  tr_noop("Vehicle Sensors Invalid"),
  tr_noop("Big Model Failed"),
  tr_noop("Calibration Incomplete"),
  tr_noop("Calibration Invalid: Remount Device & Recalibrate"),
  tr_noop("Camera Frame Rate Low"),
  tr_noop("Camera Malfunction"),
  tr_noop("Car Detected in Blindspot"),
  tr_noop("Car in Blindspot"),
  tr_noop("Communication Issue Between Processes"),
  tr_noop("Device Remount Detected: Recalibrating"),
  tr_noop("Door Open"),
  tr_noop("Driving Model Lagging"),
  tr_noop("Electronic Stability Control Active"),
  tr_noop("Electronic Stability Control Disabled"),
  tr_noop("Excessive Actuation"),
  tr_noop("Gear not D"),
  tr_noop("Lane Departure Detected"),
  tr_noop("locationd Temporary Error"),
  tr_noop("Low Communication Rate Between Processes"),
  tr_noop("Low Memory: Reboot Your Device"),
  tr_noop("Model uncertain at this speed"),
  tr_noop("openpilot will disengage"),
  tr_noop("paramsd Temporary Error"),
  tr_noop("Pay Attention"),
  tr_noop("Posenet Speed Invalid"),
  tr_noop("Press Resume"),
  tr_noop("Press Resume to Exit Brake Hold"),
  tr_noop("Press Resume to Exit Standstill"),
  tr_noop("Process Not Running"),
  tr_noop("Radar Error: Restart the Car"),
  tr_noop("Radar Temporarily Unavailable"),
  tr_noop("Resume Driving Manually"),
  tr_noop("Seatbelt Unlatched"),
  tr_noop("Sensor Data Invalid"),
  tr_noop("Speed Too High"),
  tr_noop("Steer Assist Unavailable Below {}"),
  tr_noop("Steering Assist Temporarily Unavailable"),
  tr_noop("System Lagging"),
  tr_noop("System Overheated"),
  tr_noop("TAKE CONTROL"),
  tr_noop("Take Control"),
  tr_noop("take control"),
  tr_noop("Touch Steering Wheel"),
  tr_noop("turn exceeds limit"),
  tr_noop("Turn Exceeds Steering Limit"),
  tr_noop("Vehicle Steering Time Limit"),
  tr_noop("Adaptive Cruise Disabled"),
  tr_noop("AEB: Risk of Collision"),
  tr_noop("Always keep hands on wheel and eyes on road"),
  tr_noop("Be ready to take over at any time"),
  tr_noop("Big Model Failed "),
  tr_noop("Big Model Loading"),
  tr_noop("Bookmark Saved"),
  tr_noop("Calibrating"),
  tr_noop("Calibrating: {}%"),
  tr_noop("Calibration in Progress"),
  tr_noop("Calibration Invalid"),
  tr_noop("Camera Frame Rate Low: Reboot Your Device"),
  tr_noop("Camera Malfunction: Reboot Your Device"),
  tr_noop("CAN Bus Disconnected: Check Connections"),
  tr_noop("CAN Bus Disconnected: Likely Faulty Cable"),
  tr_noop("Cancel Pressed"),
  tr_noop("Car Not Ready"),
  tr_noop("Car Unrecognized"),
  tr_noop("Changing Lanes"),
  tr_noop("Confirm Lane Change"),
  tr_noop("Contact comma.ai/support"),
  tr_noop("Cruise Fault: Restart the car to engage"),
  tr_noop("Dashcam mode"),
  tr_noop("Dashcam Mode"),
  tr_noop("Dashcam mode for unsupported car"),
  tr_noop("Drive Above {}"),
  tr_noop("Drive above {} to engage"),
  tr_noop("Drive to Calibrate"),
  tr_noop("Ensure road ahead is clear"),
  tr_noop("Fan Malfunction"),
  tr_noop("Following Distance: {}"),
  tr_noop("Invalid LKAS setting"),
  tr_noop("Joystick Mode"),
  tr_noop("Lateral Maneuver Mode"),
  tr_noop("LKAS Fault: Restart the car to engage"),
  tr_noop("Longitudinal Maneuver Mode"),
  tr_noop("Low Memory"),
  tr_noop("openpilot Canceled"),
  tr_noop("openpilot Unavailable"),
  tr_noop("Out of Storage"),
  tr_noop("pair to connect\nto view"),
  tr_noop("Parking Brake Engaged"),
  tr_noop("Pay Attention to Engage"),
  tr_noop("Pedal Pressed"),
  tr_noop("Press Set to Engage"),
  tr_noop("Reboot your Device"),
  tr_noop("Recalibrating: {}%"),
  tr_noop("Release Brake to Engage"),
  tr_noop("Remount Detected: Recalibrating"),
  tr_noop("Restart the car to retry,\nsmall model is still available"),
  tr_noop("Reverse\nGear"),
  tr_noop("Security Key Not Available"),
  tr_noop("Selfdrive Process Lagging: Reboot Your Device"),
  tr_noop("Slow down to engage"),
  tr_noop("Speed Error: {} m/s"),
  tr_noop("Speed too low"),
  tr_noop("Steer Left"),
  tr_noop("Steer Left to Start Lane Change Once Safe"),
  tr_noop("Steer Right"),
  tr_noop("Steer Right to Start Lane Change Once Safe"),
  tr_noop("Steering Pressed"),
  tr_noop("Steering Temporarily Unavailable"),
  tr_noop("Stock LKAS: Lane Departure Detected"),
  tr_noop("System Initializing"),
  tr_noop("Too Distracted"),
  tr_noop("Touch Steering Wheel: No Face Detected"),
  tr_noop("Vehicle Sensors Calibrating"),
  tr_noop("WARNING: This branch is not tested"),
  tr_noop("{} minute Left"),
  tr_noop("{} minutes Left"),
  tr_noop("{} °C"),
  tr_noop("{}% frames dropped"),
  tr_noop("{}% full"),
  tr_noop("{}% used"),
  tr_noop("Steering misalignment detected"),
  tr_noop("Steer ratio mismatch"),
  tr_noop("Abnormal tire stiffness"),
  tr_noop("Angle offset too high (Offset: {}°)"),
  tr_noop("Steering rack geometry may be off (Ratio: {})"),
  tr_noop("Check tires, pressure, or alignment (Factor: {})"),
  tr_noop("Remount Device (Pitch: {}°, Yaw: {}°)"),
  tr_noop("Gas: {}%, Steer: {}%"),
  tr_noop("Enable Adaptive Cruise to Engage"),
  tr_noop("Enable Main Switch to Engage"),
  tr_noop("Disable your car's stock LKAS to engage"),
  tr_noop("Enable your car's LKAS to engage"),
  tr_noop("Switch to Traffic-Aware Cruise Control to engage"),
  tr_noop("Toggle stock LKAS on or off to engage"),
]

_TEMPLATES = [(s, re.compile("^" + re.escape(s).replace(re.escape("{}"), "(.+?)") + "$", re.DOTALL))
              for s in ALERT_STRINGS if "{}" in s]
_cache: dict[tuple[str, str], str] = {}


def _translate(text: str) -> str:
  translated = tr(text)
  if translated != text:
    return translated
  for template, regex in _TEMPLATES:
    m = regex.match(text)
    if m is None:
      continue
    fmt = tr(template)
    if fmt == template:
      return text
    return fmt.format(*(tr(g) for g in m.groups()))
  return text


def tr_alert(text: str) -> str:
  """Translate an alert text from selfdriveState into the selected UI language."""
  if not text or multilang.language == "en":
    return text
  key = (multilang.language, text)
  if key not in _cache:
    if len(_cache) > 512:
      _cache.clear()
    _cache[key] = _translate(text)
  return _cache[key]
