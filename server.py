from flask import Flask
from flask import send_file
from flask import make_response
from flask.ext.cors import CORS
import cv2

from frame import create_capture


app = Flask(__name__)
CORS(app)

#Alternating between 2 Images as a proof of concept
@app.route("/get_image/<imgId>")
def get_image(imgId, cpuTemp, cpuFreq):
    global count
    global webCam
    imgId = count
    count += 1

    #Read Sensor Values
    cpuFreqFile = open("path/to/freq", "r")
    cpuFreq = ( int(cpuFreqFile.read()) / 1000)
    cpuTempFile = open("path/to/temp", "r")
    cpuTemp = ( int(cpuTempFile.read()) / 1000 )

    #Capture Image on WebCam
    create_capture(webCam)

    #Create Response
    response = make_response(send_file("frame.jpg", mimetype='image/jpeg'))
    response.headers["Access-Control-Expose-Headers"] = "img-id, cpu-temp, cpu-freq"
    response.headers["img-id"] = imgId
    response.headers["cpu-temp"] = cpuTemp
    response.headers["cpu-freq"] = cpuFreq
    return response

@app.route("/test_connection/")
def test_connection():
    response = make_response("Everything is ready to go!")
    return response

if __name__ == "__main__":
    global count
    global webCam
    webCam = cv2.VideoCapture(0)
    count = 0
    app.run(host="127.0.0.1", port=5000)
