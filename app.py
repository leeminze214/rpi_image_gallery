from flask import Flask, render_template,redirect,url_for
import json
#from picamera import PiCamera
from datetime import datetime
from time import sleep

app = Flask(__name__)

#camera = PiCamera()

@app.route('/gallery')
def gallery():
    image_list = []
    with open('images.txt','r') as f:
        for image in f:
            image_list.append(image)
            #https://flask.palletsprojects.com/en/2.2.x/patterns/javascript/
    return render_template('home.html', data = json.dumps(image_list))

@app.route('/take_pic')
def take_photo():
    #camera.start_preview()
    #camera.start_recording(f'/home/pi/Pictures/{datetime.now()}.h264')
    #sleep(3)
    time = str(datetime.now())
    name = f'/home/pi/coding/rpi_pic_website/static/{time}.jpg'
    #camera.capture(name)
    with open('images.txt','a') as f:
        f.write(f'{name}\n')
    #camera.stop_recording()
    #camera.stop_preview()
    return redirect(url_for('gallery'))

if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(debug=True)