TARGET = False

try:
    import RPi.GPIO as GPIO
    TARGET = True
except ModuleNotFoundError:
    pass
