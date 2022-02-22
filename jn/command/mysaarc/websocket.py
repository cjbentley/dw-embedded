import asyncio
import websockets
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
target = 'network', 10000


async def echo(websocket):
    async for message in websocket:
        await websocket.send(message)
        s.sendto(message.encode(), target)

async def main():
    async with websockets.serve(echo, "0.0.0.0", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())