import WebSocket from 'ws';

// Create WebSocket connection.
const socket = new WebSocket('ws://100.114.64.87:8765');

// Connection opened
socket.on('open', function open() {
    socket.send('Hello Server!');
});

// Listen for messages
socket.on('message', function message(data) {
    console.log('Message from server ', data);
});