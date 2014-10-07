#!/usr/bin/env python
import esocket as es
from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('eplugs.html')

@app.route("/<int:plug_id>/<onoff>")
def eplug_switch(plug_id, onoff):
    valid_onoff = ['on', 'off']
    valid_plug_id = ['0', '1', '2', '3', '4']
    print plug_id
    print onoff
    if ( str(plug_id) in valid_plug_id ) and ( onoff in valid_onoff ):
        print 'if statement'
        es.esocket(str(plug_id), onoff)
    return redirect('/', code=302)

if __name__ == "__main__":
    # app.debug = True
    app.run(host='0.0.0.0')

