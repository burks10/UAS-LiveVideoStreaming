from flask import Flask
from flask import send_file
from flask import make_response

app = Flask(__name__)

#Alternating between 2 Images as a proof of concept
@app.route("/get_image/<imgId>")
def get_image(imgId):
    global count
    imgId = count
    count += 1
    if(count % 2 == 0):
        response = make_response(send_file("A.gif", mimetype='image/gif'))
        response.headers["imgId"] = imgId
        return response
    else:
        response = make_response(send_file("B.gif", mimetype='image/gif'))
        response.headers["imgId"] = imgId
        return response

@app.route("/test_connection/")
def test_connection():
    response = make_response("Everything is ready to go!")
    return response

if __name__ == "__main__":
    global count
    count = 0
    app.run(debug=True)
