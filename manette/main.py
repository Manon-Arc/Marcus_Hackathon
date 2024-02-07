import time
import espnow
from machine import Pin, ADC
import network
import _thread

# @"\xd8\xea\xd5\x10

PIN_BTN_ACCESSOIRE = Pin(16, Pin.IN, Pin.PULL_UP)


PIN_INTERRUPT_GIRO = Pin(19, Pin.OUT)
PIN_INTERRUPT_GIRO2 = Pin(15, Pin.IN)


JOYSTICK_X = ADC(Pin(35))
JOYSTICK_Y = ADC(Pin(34))

JOYSTICK_X.atten(ADC.ATTN_11DB)
JOYSTICK_Y.atten(ADC.ATTN_11DB)


PIN_BTN_ROTATION_GAUCHE = Pin(12, Pin.IN, Pin.PULL_UP)
PIN_BTN_ROTATION_DROITE = Pin(13, Pin.IN, Pin.PULL_UP)

PIN_BTN_CANON_UP = Pin(27, Pin.IN, Pin.PULL_UP)
PIN_BTN_CANON_DOWN = Pin(14, Pin.IN, Pin.PULL_UP)

PIN_BTN_CANON_TIR = Pin(25, Pin.IN, Pin.PULL_UP)
PIN_BTN_PLOT = Pin(26, Pin.IN, Pin.PULL_UP)




COMMUNICATION = espnow.ESPNow()
COMMUNICATION.active(True)

def JoystickInput(i):
    centerX = (1965, 1995)
    centerY = (1830, 1855)
    while True:
        A = False
        R = False
        G = False
        D = False

        xValue = JOYSTICK_X.read()
        yValue = JOYSTICK_Y.read()

        if (xValue > centerX[1]):
            A = True
        if (yValue > centerY[1]):
            D = True
        if (yValue < centerY[0]):
            G = True
        if (xValue < centerX[0]):
            R = True

        if A:
            if D:
                COMMUNICATION.send(peer, "DD", True)

            elif G:
                COMMUNICATION.send(peer, "DG", True)

            else:
                COMMUNICATION.send(peer, "A", True)

        elif R:
            if D:
                COMMUNICATION.send(peer, "DBD", True)

            elif G:
                COMMUNICATION.send(peer, "DBG", True)

            else:
                COMMUNICATION.send(peer, "R", True)

        elif D:
            COMMUNICATION.send(peer, "TD", True)

        elif G:
            COMMUNICATION.send(peer, "TG", True)

        else:
            COMMUNICATION.send(peer, "STOP", True)
                

        time.sleep(0.1)

def HauteurCanonInput(i):
    while True:
        if not PIN_BTN_CANON_UP.value():
            print("canon up")
            COMMUNICATION.send(peer, "UP", True)


        if not PIN_BTN_CANON_DOWN.value():
            print("Canon down")
            COMMUNICATION.send(peer, "DOWN", True)
        time.sleep(0.1)

def RotationBaseInput(i):
    while True:
        if not PIN_BTN_ROTATION_GAUCHE.value():
            print("rotation gauche")
            COMMUNICATION.send(peer, "RG", True)


        if not PIN_BTN_ROTATION_DROITE.value():
            print("rotation droite")
            COMMUNICATION.send(peer, "RD", True)

        time.sleep(0.1)


wlan_sta = network.WLAN(network.STA_IF)
wlan_sta.active(True)
wlan_mac = wlan_sta.config('mac')
print(wlan_mac)

host, msg = COMMUNICATION.recv()
if msg == b'PLEASE':  # msg == None if timeout in recv()
   print(host, msg)
   peer = host
   COMMUNICATION.add_peer(peer)
   COMMUNICATION.send(peer, "CONNECTED", True)

_thread.start_new_thread(JoystickInput,(1,))
_thread.start_new_thread(HauteurCanonInput,(1,))
_thread.start_new_thread(RotationBaseInput,(1,))

while True:
    if not PIN_BTN_ACCESSOIRE.value():
        print("btn sos")
        COMMUNICATION.send(peer, "SOS", True)

    if not PIN_INTERRUPT_GIRO2.value():
        print("Giro On")
        COMMUNICATION.send(peer, "GIRO ON", True)
    else:
        COMMUNICATION.send(peer, "GIRO OFF", True)
        print("off")
    time.sleep(0.1)

    if not PIN_BTN_CANON_TIR.value():
        print("tir")
        COMMUNICATION.send(peer, "TIR", True)
    else:
        COMMUNICATION.send(peer, "STOP TIR", True)
        pass

    if not PIN_BTN_PLOT.value():
        print("plot")
        COMMUNICATION.send(peer, "PLOT", True)