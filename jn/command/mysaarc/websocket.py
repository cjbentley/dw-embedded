import asyncio
import websockets
import socket
from control_law import control_law

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
target = 'command-network', 10000


async def echo(websocket):
    async for message in websocket:
        await websocket.send(message)
        motor_L, motor_R = control_law(message.split('/'))
        packaged = str(motor_L) + '/' + str(motor_R)
        print(packaged)
        s.sendto(packaged.encode(), target)

async def main():
    async with websockets.serve(echo, "0.0.0.0", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())