# UAS-LiveVideoStreaming
Live video streaming via WiFi-Direct using the Udon Neo platform. 
This project will be used for the 2016 UAS competition.

<h3> Dependencies </h3>
<table>
  <tr>
    <td>
    <b>
    Technology
    </b>
    </td>
    <td>
    <b>
    Website
    </b>
    </td>
    <td>
    <b>
    Installation
    </b>
    </td>
  </tr>
  <tr>
    <td>
    Flask
    </td>
    <td>
    http://flask.pocoo.org
    </td>
    <td>
    sudo pip install -U Flask
    </td>
  </tr>
  
  <tr>
    <td>
    AngularJS
    </td>
    <td>
    https://angularjs.org
    </td>
    <td>
    N/A
    </td>
  </tr>

  <tr>
    <td>
    OpenCV
    </td>
    <td>
    http://opencv.org
    </td>
    <td>
    sudo apt-get install python-opencv
    </td>
  </tr>
  
  <tr>
    <td>
    flask-cors
    </td>
    <td>
    https://github.com/corydolphin/flask-cors
    </td>
    <td>
    sudo pip install -U flask-cors
    </td>
  </tr>
</table>

<h3> How To Run </h3>
 `python server.py`
- Open index.html on the client side

<h3>Potential Issues</h3>
- When running the python server, if an error is thrown stating: `module compiled against API version a but this version of numpy is 9`
- Open a python shell
- type the commands `import numpy` and `print(numpy.__path__)` (This will give you a path to your numpy directory)
- Navigate to and remove this directory using `sudo rm -rf numpy`
