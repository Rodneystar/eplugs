#!/usr/bin/env python 

import esocket as es
from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/<int:plug_id>/<onoff>")
def eplug_switch(plug_id, onoff):
    valid_onoff = ['on', 'off']
    valid_plug_id = [0, 1, 2, 3, 4]
    if ( plug_id in valid_plug_id ) and ( onoff in valid_onoff ):
        es.esocket(plug_id, onoff)
    return "all good"

if __name__ == "__main__":
    # app.debug = True
    app.run(host='0.0.0.0')

