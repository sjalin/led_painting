from evdev import InputDevice, categorize, ecodes

GAMEPAD_LOCATION = '/dev/input/event0'

gamepad = InputDevice(GAMEPAD_LOCATION)

print(f'Gamepad info: {gamepad}')

for event in gamepad.read_loop():
    # Print stuff about gamepad events
    print('Raw data:')
    print(categorize(event))

    print('Specific data:')
    print(f'Type: {event.type} Code: {event.code} Value: {event.value}')