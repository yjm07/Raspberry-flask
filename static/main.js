var socket = io.connect('http://' + document.domain + ':' + location.port);

socket.on('ssid_list', function() {
    $('button').emit
})