import struct

devadr     = "eb:17:b5:64:23:b0"

uuid_service_led = "e95dd91d-251d-470a-a062-fa1922dfa9a8"
uuid_led_text    = "e95d93ee-251d-470a-a062-fa1922dfa9a8"

# UART SERVICE
uart_service = "6E400001-B5A3-F393-E0A9-E50E24DCCA9E"
uartTX = "6E400002-B5A3-F393-E0A9-E50E24DCCA9E"
uartRX = "6E400003-B5A3-F393-E0A9-E50E24DCCA9E"

iopin   = "E95D127B-251D-470A-A062-FA1922DFA9A8"
pinmask = "E95D5899-251D-470A-A062-FA1922DFA9A8"
pwm_ctl = "E95DD822-251D-470A-A062-FA1922DFA9A8"

per = btle.Peripheral(devadr, btle.ADDR_TYPE_RANDOM)

# LED SERVICE
#svcLed = per.getServiceByUUID(uuid_service_led)
#chLedText = svcLed.getCharacteristics(uuid_led_text)[0]
#chLedText.write("Hello".encode("utf-8"))
#time.sleep(1)

svcio = per.getServiceByUUID(iopin)

# pin0 as Output
#chPIOC = svcio.getCharacteristics("E95DB9FE-251D-470A-A062-FA1922DFA9A8")[0]
#chPIOC.write(b"\x00\x00\x00\x00")

# pin0 as AD Config / Digital
#chADC = svcio.getCharacteristics(pinmask)[0]
#chADC.write(b"\x00\x00\x00\x00")

# pin0 data
#chPIOC = svcio.getCharacteristics("E95D8D00-251D-470A-A062-FA1922DFA9A8")[0]
#chPIOC.write(b"\x00\x01")

#chPWM = svcio.getCharacteristics(pwm_ctl)[0]
#chPWM.write(b"\x00\x00\x01\x14\x00\x00\x00")

print("Write: bluetooth.".format())

svcUart = per.getServiceByUUID(uart_service)
chTX = svcUart.getCharacteristics(uartTX)[0]
#ch_cccd=chTX.getDescriptors(forUUID=0x2902)[0]

def set_degree(p0, p1):
    # Format is CH0,DEGREE, CH1, DEGREE,XXX\n
    # CH0 is 0 , CH1 is 1
    barg = bytes('0,{},1,{},NOP\n'.format(p0,p1),'utf-8')
    if len(barg) > 20:
        print("Warning: Length > 20(MAX) \n")
    return barg

def set_servo(deg0, deg1):
    per.writeCharacteristic(0x002a, set_degree(deg0,deg1), False)
    time.sleep(1) # You need some time !

set_servo(0, 0)
set_servo(90, 90)
set_servo(180, 180)
set_servo(0, 0)
