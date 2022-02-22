window.addEventListener("gamepadconnected", function(e) {
  console.log("Gamepad connected at index %d: %s. %d buttons, %d axes.",
    e.gamepad.index, e.gamepad.id,
    e.gamepad.buttons.length, e.gamepad.axes.length);
});

const websocket = new WebSocket("ws://172.20.22.118:8765/");
websocket.onopen = () => {
  console.log("OK");
  websocket.send("1/1");
}
