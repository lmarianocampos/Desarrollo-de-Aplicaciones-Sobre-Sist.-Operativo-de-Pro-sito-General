from gpio import Gpio
pin = Gpio(1)
print("Pin"+ str(pin.get_nPin()))
pin.set_state(True)
if pin.get_state():
    print("state = 1 ")
else:
    print("state =0 ")
pin0 = Gpio(0)
print("Pin"+str(pin0.get_nPin()))
pin0.set_state(False)

if pin0.get_state():
    print("state = 1 ")
else:
    print("state = 0 ")
pin0.set_state(True)
if pin0.get_state():
    print("state = 1 ")
else:
    print("state = 0 ")
