'''
Adapted excerpt from Getting Started with Raspberry Pi by Matt Richardson
Modified by Rui Santos
Complete project details: http://randomnerdtutorials.com
'''

import cv2
import datetime, time
import RPi.GPIO as GPIO
from flask import Flask, render_template, request
from flask import Flask, render_template, Response
import flask


app = Flask(__name__)

def gen_frames():  # generate frame by frame from camera
    camera = cv2.VideoCapture(0)
    while True:
        # Capture frame-by-frame
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    #Video streaming route. Put this in the src attribute of an img tag
    camera = cv2.VideoCapture(0)
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT) 
GPIO.setup(4, GPIO.OUT)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT) 
GPIO.setup(17, GPIO.OUT) 
GPIO.setup(18, GPIO.OUT) 
GPIO.setup(27, GPIO.OUT) 
GPIO.setup(22, GPIO.OUT) 
GPIO.setup(23, GPIO.OUT) 
GPIO.setup(24, GPIO.OUT) 
GPIO.setup(10, GPIO.OUT) 
GPIO.setup(9, GPIO.OUT) 
GPIO.setup(25, GPIO.OUT) 
GPIO.setup(11, GPIO.OUT) 
GPIO.setup(8, GPIO.OUT) 
GPIO.setup(7, GPIO.OUT) 
GPIO.setup(0, GPIO.OUT) 
GPIO.setup(1, GPIO.OUT) 
GPIO.setup(5, GPIO.OUT) 
GPIO.setup(6, GPIO.OUT) 
GPIO.setup(12, GPIO.OUT) 
GPIO.setup(13, GPIO.OUT) 




# Create a dictionary called pins to store the pin number name and pin state:
pins = {
   2 : {'name' : '', 'state' : GPIO.LOW},
   3 : {'name' : '', 'state' : GPIO.LOW},
   4 : {'name' : '', 'state' : GPIO.LOW},
   14 : {'name' : '', 'state' : GPIO.LOW},
   15 : {'name' : '', 'state' : GPIO.LOW},
   17 : {'name' : '', 'state' : GPIO.LOW},
   18 : {'name' : '', 'state' : GPIO.LOW},
   27 : {'name' : '', 'state' : GPIO.LOW},
   22 : {'name' : '', 'state' : GPIO.LOW},
   23 : {'name' : '', 'state' : GPIO.LOW},
   24 : {'name' : '', 'state' : GPIO.LOW}, #
   10 : {'name' : '', 'state' : GPIO.LOW},
   9 : {'name' : '', 'state' : GPIO.LOW},
   25 : {'name' : '', 'state' : GPIO.LOW},
   11 : {'name' : '', 'state' : GPIO.LOW},
   8 : {'name' : '', 'state' : GPIO.LOW},
   7 : {'name' : '', 'state' : GPIO.LOW},
   0 : {'name' : '', 'state' : GPIO.LOW},
   1 : {'name' : '', 'state' : GPIO.LOW},
   5 : {'name' : '', 'state' : GPIO.LOW},
   6 : {'name' : '', 'state' : GPIO.LOW},
   12 : {'name' : '', 'state' : GPIO.LOW},
   13 : {'name' : '', 'state' : GPIO.LOW},
   }

# Set each pin as an output/input and make it low:
#for pin in pins:
#   GPIO.setup(pin, GPIO.OUT)
#   GPIO.output(pin, GPIO.LOW)
GPIO.setup(20, GPIO.IN)



def event_stream():
    print("event_stream")
    count = 0
    while True:

        mybutton = GPIO.input(20)
        print("while")
        if mybutton == True:
            count += 1
            print ("mybutton")
            time.sleep(0.5)

        break



@app.route('/stream')
def stream():
    print("stream")
    return flask.Response(event_stream(), mimetype="text/event-stream")

@app.route("/")
def main():
   print("main")
   # For each pin, read the pin state and store it in the pins dictionary:
   for pin in pins:
      pins[pin]['state'] = GPIO.input(pin)


   # Put the pin dictionary into the template data dictionary:
   templateData = {
      'pins': pins,
   }



   # Pass the template data into the template main.html and return it to the user
   return render_template('main.html', **templateData)
   camera.release()






# The function below is executed when someone requests a URL with the pin number and action in it:
@app.route("/<changePin>/<action>")
def action(changePin, action):
   # Convert the pin from the URL into an integer:
   changePin = int(changePin)
   # Get the device name for the pin being changed:
   deviceName = pins[changePin]['name']
   # If the action part of the URL is "on," execute the code indented below:
   if action == "on":
      # Set the pin high:
      GPIO.output(changePin, GPIO.HIGH)
      # Save the status message to be passed into the template:
      message = "Turned " + deviceName + " on."
   if action == "off":
      GPIO.output(changePin, GPIO.LOW)
      message = "Turned " + deviceName + " off."

   # For each pin, read the pin state and store it in the pins dictionary:
   for pin in pins:
      pins[pin]['state'] = GPIO.input(pin)
      

   # Along with the pin dictionary, put the message into the template data dictionary:
   templateData = {
      'pins' : pins
   }


   return render_template('main.html', **templateData)
   camera.release()

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)