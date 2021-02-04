from evdev import InputDevice, categorize, ecodes

GAMEPAD_LOCATION = '/dev/input/event0'

gamepad = InputDevice(GAMEPAD_LOCATION)

#prints out device info at start
print(gamepad)

#evdev takes care of polling the controller in a loop
for event in gamepad.read_loop():
    print(categorize(event))