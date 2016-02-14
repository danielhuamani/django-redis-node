var express = require('express');
var http    = require('http');
var redis   = require('redis');

var app = express();


var apps_socket =http.createServer(app).listen(3000)

sockjs = require('socket.io').listen(apps_socket)

sockjs.on('connection', function(){
	var client = redis.createClient();
	client.subscribe('hola_mundo');

})
