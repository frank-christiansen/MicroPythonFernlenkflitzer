import machine

for gpio in [5, 0, 16, 14, 12, 13]:
    machine.Pin(gpio, machine.Pin.OUT).off()

machine.Pin(15, machine.Pin.OUT).on()