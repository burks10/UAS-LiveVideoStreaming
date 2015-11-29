# UAS-LiveVideoStreaming
Live video streaming via WiFi-Direct using the Udon Neo platform. 
This project will be used for the 2016 UAS competition.

<h3> Dependencies </h3>
- Flask
- AngularJS
- OpenCV

<h3> How To Run </h3>
```
In order to start the server, run the command:
python server.py

Open index.html on the client side
```

<h3>Potential Issues</h3>
When running the python server, if an error is thrown stating:
"module compiled against API version a but this version of numpy is 9"
- Open a python shell
- type the commands `import numpy` and `print(numpy.__path__)` (This will give you a path to your numpy directory)
- Navigate to and remove this directory using `sudo rm -rf numpy`
