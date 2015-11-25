var DEBUG_MODE = true;
var client;


if(!DEBUG_MODE){
  client = new BinaryClient('ws://10.42.0.20:9000');
}else{
  client = new BinaryClient('ws://localhost:9000');
}



// Received new stream from server!
client.on('stream', function(stream, meta){
  // Buffer for parts
  var parts = [];
  // Got new data
  stream.on('data', function(data){
    parts.push(data);
  });
  stream.on('end', function(){
    // Display new data in browser!
    var img = document.createElement("img");
    img.src = (window.URL || window.webkitURL).createObjectURL(new Blob(parts));
    document.body.appendChild(img);
  });
});
