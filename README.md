eplugs
======

Web based controls for the energenie4u Pi-mote Control, written in python and using
the flask web framework.

Designed to provide a really simple web interface for the Raspberry Pi compatible
Pi-mote controller for Energenie's remote control sockets.

Some of the code for this project is adapted from the following Energenie supplied 
controller script: https://energenie4u.co.uk/res/software/ENER002-2PI.py

This project is in no way affiliated with energenie4u.co.uk


Dependencies
------------
* A Raspberry Pi computer
* The Energenie Pi-mote remote controller
* 1 or more Energenie remote control sockets - The Pi-mote supports up to 4

To run the scripts supplied here you'll need flask and the RasPi Python GPIO library

```
sudo apt-get install python-flask python-rpi.gpio
```


Quick Start
-----------
Change into the installation directory and run:

```
sudo ./eplugsctl start
```

Assuming all the dependencies are met and you receive no errors, you can now visit 
http://<your Pi's IP or domain name>:5000 in a browser and start turning things on and off.

To stop the server, just run:

```
sudo ./eplugsctl stop
```


A note on security
------------------
Please never, ever expose this application to the open internet. It is intended for use inside
your home network only.


Adding more sockets/renaming sockets
------------------------------------
By default eplugs is configured for 2 sockets, as this matches what you get in Energenie's
starter kit. This means the web UI displays 3 groups of on/off buttons, 'All', 'Socket 1'
and 'Socket 2'. If you have a look in './templates/eplugs.html' you'll find that buttons for sockets 
3 and 4 are currently commented out. uncomment if you need them. You can also play with the sizes 
and designs of the buttons on here, as well as the names of the sockets. The button graphics are
in './static/'.


Using with monit
----------------
I'm a big fan of monit and if you'd like to use it with monit, create a new file in
your monit/conf.d directory and add the following, adjusting to suit your installation
where necessary

```
check process eplugs with pidfile /var/run/eplugs.pid
    start program = "/path/to/eplugs/eplugsctl start"
    stop program = "/path/to/eplugs/eplugsctl stop"
```
