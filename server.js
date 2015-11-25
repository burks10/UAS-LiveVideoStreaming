var DEBUG_MODE = true;
var server;

var BinaryServer = require('binaryjs').BinaryServer;
var fs = require('fs');

if(!DEBUG_MODE){
  server = BinaryServer({host: "10.42.0.20", port: 9000});
}else{
  server = BinaryServer({port: 9000});
}

// Wait for new user connections
server.on('connection', function(client){
  // Stream a flower as a hello!
  var file = fs.createReadStream(__dirname + '/flower.png');
  client.send(file);
});
