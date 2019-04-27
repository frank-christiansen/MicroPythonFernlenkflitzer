import machine
import time

forwardPin = machine.Pin(5, machine.Pin.OUT)
backwardPin = machine.Pin(0, machine.Pin.OUT)
leftPin = machine.Pin(16, machine.Pin.OUT)
rightPin = machine.Pin(14, machine.Pin.OUT)

forwardPin.off()
backwardPin.off()
leftPin.off()
rightPin.off()

machine.Pin(15, machine.Pin.OUT).off()
machine.Pin(12, machine.Pin.OUT).on()

def move():
    forwardPin.on()
    time.sleep(1)
    forwardPin.off()

def moveleft():
    leftPin.on()
    forwardPin.on()
    time.sleep(1)
    forwardPin.off()
    leftPin.off()

def moveright():
    rightPin.on()
    forwardPin.on()
    time.sleep(1)
    forwardPin.off()
    rightPin.off()