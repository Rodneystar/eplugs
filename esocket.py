#!/usr/bin/python
#import the required modules
import RPi.GPIO as GPIO
import time
import sys
    
def esocket_cli():
    valid_onoff = ['on', 'off']
    valid_plug_id = ['0', '1', '2', '3', '4', 'all']
    plug_id = sys.argv[1]
    onoff = sys.argv[2]
    if ( plug_id in valid_plug_id ) and ( onoff in valid_onoff ):
        esocket(plug_id, onoff)

def esocket(plug_id, onoff):
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
    
    try:
        if  plug_id == "1":
            if onoff == "on":
                # Set K0-K3
                print "sending code 1111 socket 1 on"
                GPIO.output (11, True)
                GPIO.output (15, True)
                GPIO.output (16, True)
                GPIO.output (13, True)
                # let it settle, encoder requires this
                time.sleep(0.1)    
                # Enable the modulator
                GPIO.output (22, True)
                # keep enabled for a period
                time.sleep(0.25)
                # Disable the modulator
                GPIO.output (22, False)
    
        if  plug_id == "1":
            if  onoff == "off":
                # Set K0-K3
                print "sending code 0111 Socket 1 off"
                GPIO.output (11, True)
                GPIO.output (15, True)
                GPIO.output (16, True)
                GPIO.output (13, False)
                # let it settle, encoder requires this
                time.sleep(0.1)
                # Enable the modulator
                GPIO.output (22, True)
                # keep enabled for a period
                time.sleep(0.25)
                # Disable the modulator
                GPIO.output (22, False)
    
        if plug_id == "2":
            if onoff == "on":
                # Set K0-K3
                print "sending code 1110 socket 2 on"
                GPIO.output (11, False)
                GPIO.output (15, True)
                GPIO.output (16, True)
                GPIO.output (13, True)
                # let it settle, encoder requires this
                time.sleep(0.1)    
                # Enable the modulator
                GPIO.output (22, True)
                # keep enabled for a period
                time.sleep(0.25)
                # Disable the modulator
                GPIO.output (22, False)
    
        if plug_id == "2":
            if onoff == "off":
                # Set K0-K3
                print "sending code 0110 socket 2 off"
                GPIO.output (11, False)
                GPIO.output (15, True)
                GPIO.output (16, True)
                GPIO.output (13, False)
                # let it settle, encoder requires this
                time.sleep(0.1)
                # Enable the modulator
                GPIO.output (22, True)
                # keep enabled for a period
                time.sleep(0.25)
                # Disable the modulator
                GPIO.output (22, False)
    
        if plug_id == "3":
            if  onoff == "on":
                # Set K0-K3
                print "sending code 1101 socket 3 on"
                GPIO.output (11, True)
                GPIO.output (15, True)
                GPIO.output (16, False)
                GPIO.output (13, True)
                # let it settle, encoder requires this
                time.sleep(0.1)
                # Enable the modulator
                GPIO.output (22, True)
                # keep enabled for a period
                time.sleep(0.25)
                # Disable the modulator
                GPIO.output (22, False)
    
        if  plug_id == "3":
            if  onoff == "off":
                # Set K0-K3
                print "sending code 0101 socket 3 off"
                GPIO.output (11, False)
                GPIO.output (15, True)
                GPIO.output (16, False)
                GPIO.output (13, True)
                # let it settle, encoder requires this
                time.sleep(0.1)
                # Enable the modulator
                GPIO.output (22, True)
                # keep enabled for a period
                time.sleep(0.25)
                # Disable the modulator
                GPIO.output (22, False)
        
        if plug_id == "4":
            if onoff == "on":
                # Set K0-K3
                print "sending code 1100 socket 4 on"
                GPIO.output (11, True)
                GPIO.output (15, True)
                GPIO.output (16, False)
                GPIO.output (13, False)
                # let it settle, encoder requires this
                time.sleep(0.1)
                # Enable the modulator
                GPIO.output (22, True)
                # keep enabled for a period
                time.sleep(0.25)
                # Disable the modulator
                GPIO.output (22, False)
    
    
        if  plug_id == "4":
            if onoff == "off":
                # Set K0-K3
                print "sending code 0100 socket 4 off"
                GPIO.output (11, False)
                GPIO.output (15, True)
                GPIO.output (16, False)
                GPIO.output (13, False)
                # let it settle, encoder requires this
                time.sleep(0.1)
                # Enable the modulator
                GPIO.output (22, True)
                # keep enabled for a period
                time.sleep(0.25)
                # Disable the modulator
                GPIO.output (22, False)
    
        if ( plug_id == "all" ) or ( plug_id == "0" ):
            if onoff == "on":
                # Set K0-K3
                print "sending code 1011 ALL on"
                GPIO.output (11, True)
                GPIO.output (15, True)
                GPIO.output (16, False)
                GPIO.output (13, True)
                # let it settle, encoder requires this
                time.sleep(0.1)
                # Enable the modulator
                GPIO.output (22, True)
                # keep enabled for a period
                time.sleep(0.25)
                # Disable the modulator
                GPIO.output (22, False)
        
        if ( plug_id == "all" ) or ( plug_id == "0" ):
            if onoff == "off":
                # Set K0-K3
                print "sending code 0011 All off"
                GPIO.output (11, True)
                GPIO.output (15, True)
                GPIO.output (16, False)
                GPIO.output (13, False)
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

if __name__ == ('__main__'):
    esocket_cli()
