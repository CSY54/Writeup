const socket = require('socket.io-client')('https://woooosh.2020.chall.actf.co');

socket.on('connect', () => socket.emit('start'));

socket.on('shapes', shapes => {
  for (let i = 0; i < 20; i++) {
    socket.emit('click', shapes[0].x, shapes[1].y);
  }      
});

socket.on('disp', res => {
    console.log(res);
    socket.disconnect();
});
