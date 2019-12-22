#!/usr/bin/python
#import the required modules
import RPi.GPIO as GPIO
import time
import sys


sockets = {
    0: {
        "on": [True, True, False, True],
        "off": [True, True, False, False]
    },
    1: {
        "on": [True, True, True, True],
        "off": [True, True, True, False]
    },
    2:{
        "on": [False, True, True, True],
        "off": [False, True, True, False]
    },
    3:{
        "on": [True, True, False, True],
        "off": [False, True, False, True]
    },
    4:{
        "on": [True, True, False, False],
        "off": [False, True, False, False]
    }
}

def initialiseGpio() :
        # set the pins numbering mode
    GPIO.setmode(GPIO.BOARD)

    # Select the GPIO pins used for the encoder K0-K3 data inputs
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)

    # Select the signal to select ASK/FSK
    GPIO.setup(18, GPIO.OUT)

    # Select the signal used to enable/disable the modulator
    GPIO.setup(22, GPIO.OUT)

    # Disable the modulator by setting CE pin lo
    GPIO.output (22, False)

    # Set the modulator to ASK for On Off Keying 
    # by setting MODSEL pin lo
    GPIO.output (18, False)

    # Initialise K0-K3 inputs of the encoder to 0000
    GPIO.output (11, False)
    GPIO.output (15, False)
    GPIO.output (16, False)
    GPIO.output (13, False)

    # The On/Off code pairs correspond to the hand controller codes.
    # True = '1', False ='0'

def esocket(plug_id, onoff):
    initialiseGpio()
    # The On/Off code pairs correspond to the hand controller codes.
    # True = '1', False ='0'
    try:        # Set K0-K3
        print("sending code 1111 socket 1 on")
        GPIO.output(11, sockets[plug_id][onoff][0])
        GPIO.output (15, sockets[plug_id][onoff][1])
        GPIO.output (16, sockets[plug_id][onoff][2])
        GPIO.output (13, sockets[plug_id][onoff][3])
        # let it settle, encoder requires this
        time.sleep(0.1)    
        # Enable the modulator
        GPIO.output (22, True)
        # keep enabled for a period
        time.sleep(0.25)
        # Disable the modulator
        GPIO.output (22, False)

    # Clean up the GPIOs for next time
    except KeyboardInterrupt:
        GPIO.cleanup()
    GPIO.cleanup()


def esocket_cli():
    valid_onoff = ['on', 'off']
    valid_plug_id = ['0', '1', '2', '3', '4']
    plug_id = sys.argv[1]
    onoff = sys.argv[2]
    if ( plug_id in valid_plug_id ) and ( onoff in valid_onoff ):
        esocket(int(plug_id), onoff)

if __name__ == ('__main__'):
    esocket_cli()
