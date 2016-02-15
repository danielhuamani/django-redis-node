var express = require('express');
var http    = require('http');
var redis   = require('redis');

var app = express();


var apps_socket =http.createServer(app).listen(3000)

sockjs = require('socket.io').listen(apps_socket)

sockjs.on('connect', function(socket){
	var client = redis.createClient();
	client.subscribe('mundo');
	client.on("message", function(channel, message) {
        socket.emit(channel, message);
    });
})
